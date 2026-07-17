# Agentic AI-Based Banking Fraud Detection and Investigation System

## Overview

The Agentic AI-Based Banking Fraud Detection and Investigation System is a backend-focused application that simulates how banks investigate suspicious financial transactions using multiple AI agents. The system is designed to automate the investigation process by verifying transaction details, analyzing customer history, evaluating fraud indicators, and generating an AI-assisted investigation report.

The application follows a modular architecture developed with FastAPI and PostgreSQL. Instead of relying only on fraud prediction, it performs a complete investigation workflow and produces a human-readable explanation to support the final decision.

---

## Key Features

- Multi-agent fraud investigation workflow
- Transaction verification
- Customer verification
- Fraud risk analysis
- AI-generated investigation summary using Groq Llama 3.1
- PostgreSQL database integration
- RESTful API with FastAPI
- Interactive web interface
- Modular and maintainable project architecture

---

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Groq (Llama 3.1)
- Pandas
- Pydantic
- HTML
- CSS
- JavaScript
- Uvicorn
- Git & GitHub

---

## Project Workflow

The investigation begins when a user enters a transaction ID through the web interface.

The FastAPI backend receives the request and forwards it to the Coordinator Agent. The coordinator manages the complete investigation by invoking specialized agents responsible for transaction verification, customer verification, and fraud analysis.

Each agent performs its assigned responsibility using data stored in PostgreSQL. After collecting the outputs from all agents, the Decision Agent evaluates the results and uses the Groq Large Language Model to generate a final investigation report containing the fraud score, risk level, recommendation, and AI-generated explanation.

The completed report is then returned to the frontend for display.

---

## AI Agents

### Coordinator Agent

Coordinates the complete investigation process by invoking all specialized agents and collecting their outputs before forwarding them to the Decision Agent.

### Transaction Verification Agent

Retrieves and validates transaction information from the database.

### Customer Verification Agent

Retrieves customer information and analyzes previous transaction history.

### Fraud Analysis Agent

Evaluates fraud indicators such as transaction amount, previous fraud history, unusual transaction timing, failed transactions, international transactions, and merchant-related risk factors.

### Decision Agent

Combines the outputs of all agents and generates the final investigation report using the Groq Large Language Model.

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd https://github.com/uroojjunaid628-oss/Agentic_AI_banking_fraud_app.git
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and configure the following variables.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=banking_agentic_ai_db
DB_USER=postgres
DB_PASSWORD=your_password

GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the FastAPI development server.

```bash
uvicorn api.api:app --reload
```

Open the application in your browser.

```
http://127.0.0.1:8000
```

---

## API Endpoint

### Investigate Transaction

**POST**

```
/investigate
```

Example request

```json
{
    "transaction_id": 108721
}
```

Example response

```json
{
    "decision": "Investigation Completed",
    "transaction_id": 108721,
    "customer_id": 32056,
    "fraud_score": 65,
    "risk_level": "High",
    "recommendation": "Block Transaction",
    "ai_explanation": "The transaction exhibits multiple fraud indicators and requires immediate investigation."
}
```

---

## Dataset

The project uses a banking fraud detection dataset obtained from Kaggle. The dataset contains transaction details, customer information, historical activity, and fraud-related indicators. After preprocessing, the data is imported into PostgreSQL, allowing AI agents to retrieve relevant information through SQL queries during the investigation process.

---

## Future Improvements

Potential enhancements for future versions include:

- Investigation history management
- User authentication and authorization
- Real-time fraud monitoring
- Docker deployment
- Cloud deployment
- Automated audit logging
- Email notification service
- Dashboard analytics

---

## Author

**Urooj Junaid**

Backend Developer | Python Developer | FastAPI | PostgreSQL | AI Applications

---

## License

This project was developed for educational and internship purposes.