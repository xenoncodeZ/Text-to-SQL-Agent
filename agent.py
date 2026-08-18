import sqlite3
from google import genai
import pandas as pd

def get_database_schema(db_path: str) -> str:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    schema_string = "Database Schema:\n"
    for table_name, table_creation_sql in tables:
        schema_string += f"{table_creation_sql}\n"
        
    conn.close() 
    return schema_string

def generate_sql_query(user_question : str , schema : str , api_key : str, error_msg : str = "") -> str:
    ''' generating sql query '''
    
    client = genai.Client(api_key=api_key)
    # 1. Build the prompt using an f-string to inject our variables
    prompt = f"""
    You are a highly skilled SQL database expert. 
    Your only job is to write SQLite queries based on the user's request.
    
    {schema}
    
    Rules:
    1. ONLY return the raw SQL query.
    2. Do not include markdown formatting (like ```sql).
    3. Do not include any explanations or conversational text.
    """
    if error_msg != '':
        prompt += f"\n Warning your last answer gave error : {error_msg}"
        
    prompt += f'\n User Question : {user_question}'
    
    # 2. Call the Gemini API
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    # 3. Clean and return the output
    return response.text.strip()

def execute_query(sql_query: str, db_path: str):
    '''Executes the SQL query on the dynamically provided database.'''
    try:
        # 1. Manually open
        conn = sqlite3.connect(db_path)
        
        # 2. Run query
        df = pd.read_sql(sql_query, conn)
        
        # 3. Manually close
        conn.close() 
        
        return df
        
    except Exception as e:
        # Safety net: Ensure it closes even if the SQL query is bad!
        if 'conn' in locals():
            conn.close()
        return f"Database Error: {e}"
    
def run_agent(user_question: str, db_path: str, api_key: str, max_retries: int = 3):
    ''' Orchestrates the AI and DB, Retries if failed '''
    
    # 1. Dynamically extract the schema
    schema = get_database_schema(db_path)
    last_error = ""
    
    for i in range(0, max_retries):
        # 2. Pass the api_key to the AI
        generated_sql = generate_sql_query(user_question, schema, api_key, error_msg=last_error)
        
        # 3. Pass the db_path to the executor
        result = execute_query(generated_sql, db_path)
        
        if isinstance(result, pd.DataFrame):
            return result
        else:
            last_error = result
            print(f'Attempt {i+1} failed. Retrying...')
            
    return f"Agent failed. The last error was: {last_error}"
