from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import pandas as pd
from agent import run_agent

app = FastAPI()

# --- NEW CORS BLOCK ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False, 
    allow_methods=["*"],  
    allow_headers=["*"],  
)
# ----------------------

@app.get("/")
def message():
    return {"message": "ai agent app"}

@app.post("/ask")
def ask(
    question: str = Form(...), 
    api_key: str = Form(...), 
    db_file: UploadFile = File(...)
):
    # 1. Save the file temporarily
    temp_path = f"temp_{db_file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(db_file.file, buffer)
        
    # 2. Run the AI
    result = run_agent(user_question=question, db_path=temp_path, api_key=api_key)
    
    # 3. Clean up
    os.remove(temp_path)
    
    # 4. Return the data
    if isinstance(result, pd.DataFrame):
        return {"status": "success", "data": result.to_dict(orient="records")}
    else:
        return {"status": "error", "message": result}