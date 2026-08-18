<div align="center">
  
# 🚀 AI Text-to-SQL Agent

**A full-stack, AI-powered data analytics platform that dynamically converts natural language into executable SQL queries.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](#)
[![Gemini](https://img.shields.io/badge/Google%20GenAI-4285F4.svg?style=for-the-badge&logo=google&logoColor=white)](#)
[![Vanilla JS](https://img.shields.io/badge/Vanilla%20JS-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)](#)

*Upload a database. Ask a question in plain English. Get instant data.*

</div>

---

## 📖 Overview

This application bridges the gap between raw data and actionable insights. By leveraging the Google GenAI SDK, it allows users to upload any SQLite database and query it using natural language. The AI engine automatically reads the database schema, engineers the correct SQL query, executes it, and returns the data in a responsive, modern web interface.

### ✨ Key Features

* **Natural Language Processing:** Translate complex business questions (e.g., "Who are the top 3 customers by sales?") into perfectly structured SQL.
* **Dynamic Schema Extraction:** Automatically parses the architecture, tables, and columns of any uploaded .db or .sqlite file on the fly.
* **Self-Healing AI Execution:** The agent evaluates its own SQL for runtime errors, automatically correcting and retrying up to 3 times if a query fails.
* **Stateless API Backend:** Built with FastAPI to securely handle asynchronous file uploads, process AI logic, and automatically clean up temporary server files.
* **Custom Glassmorphism UI:** A responsive, dark-mode frontend built entirely without heavy frameworks, featuring custom CSS animations and dynamic DOM manipulation.
* **Database Seeding:** Includes a lightweight Python script to instantly generate a robust e-commerce mock database for quick local testing.

---

## 🏗️ Project Architecture

Text-to-SQL-Agent/
├── frontend/
│   ├── index.html        # Main web interface (Form & Data Table)
│   ├── style.css         # Custom animations and dark-mode styling
│   └── app.js            # Asynchronous logic, API fetching, and UI rendering
├── agent.py              # Core AI logic, prompt engineering, and SQLite execution
├── api.py                # FastAPI server, CORS routing, and file management
├── setup_sqlite.py       # Database seed script for generating local test data
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

---

## ⚙️ Local Setup & Installation

### Prerequisites
* Python 3.8+
* Git

### Step-by-Step Guide

**1. Clone the repository**
git clone https://github.com/xenoncodeZ/Text-to-SQL-Agent.git
cd Text-to-SQL-Agent

**2. Set up a Virtual Environment**
Creating an isolated environment ensures clean dependency management.
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

**3. Install Dependencies**
pip install -r requirements.txt

**4. Generate the Test Database**
Run the included seed script to generate a robust, 15-row e-commerce mock database for instant local testing. This creates a sales_data.db file in your root folder.
python setup_sqlite.py

**5. Run the Application Server**
Launch the FastAPI backend.
python -m uvicorn api:app --reload

---

## 💡 Usage Guide

1. Open frontend/index.html directly in your web browser.
2. Input your **Gemini API Key** securely into the designated field.
3. Upload the generated sales_data.db file (or any custom SQLite database).
4. Ask an analytical question in plain English, such as:
   * "Show me all transactions sorted by amount."
   * "What is the total amount spent by Emma Watson?"
   * "List the top 3 most expensive products."
5. Click **Run Query** and watch the AI dynamically generate your data table!

---

## 🗺️ Future Roadmap

- [ ] Transition frontend to React/Next.js for state management.
- [ ] Add data visualization capabilities (Chart.js/D3) directly in the UI.
- [ ] Deploy backend to a containerized cloud environment (Render/Railway).

---

*Note: The API key is used strictly client-side for the current session and is never permanently stored on the server.*