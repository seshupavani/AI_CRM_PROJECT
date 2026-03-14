🧠 AI-First CRM – HCP Interaction Logging System


📌 Project Overview

This project implements an AI-First Customer Relationship Management (CRM) system designed to log interactions between pharmaceutical Field Representatives and Healthcare Professionals (HCPs).

In traditional CRM systems, representatives manually enter interaction details after meeting doctors. This project demonstrates how Artificial Intelligence can automate interaction logging using natural language and voice input.

The system allows users to log interaction details using:

📄 Structured Interaction Form

💬 AI Conversational Assistant

🎤 Voice Note Transcription

The AI automatically extracts important information from conversations and stores it in a database.

🧠 AI-First CRM – HCP Interaction Logging System


📌 Project Overview

This project implements an AI-First Customer Relationship Management (CRM) system designed to log interactions between pharmaceutical Field Representatives and Healthcare Professionals (HCPs).

In traditional CRM systems, representatives manually enter interaction details after meeting doctors. This project demonstrates how Artificial Intelligence can automate interaction logging using natural language and voice input.

The system allows users to log interaction details using:

📄 Structured Interaction Form

💬 AI Conversational Assistant

🎤 Voice Note Transcription

The AI automatically extracts important information from conversations and stores it in a database.



🚀 Key Features


1️⃣ HCP Interaction Logging

Representatives can log details of meetings with healthcare professionals.

The system captures:

HCP Name

Interaction Type

Topics Discussed

Materials Shared

Samples Distributed

HCP Sentiment

Outcomes of the discussion

Follow-up actions

5️⃣ Interaction History

All logged interactions are stored in a database and can be viewed later for reference.

This allows organizations to track:

Doctor engagement history

Follow-up activities

Discussion topics

5️⃣ Interaction History

All logged interactions are stored in a database and can be viewed later for reference.

This allows organizations to track:

Doctor engagement history

Follow-up activities

Discussion topics

🏗️ System Architecture

React Frontend
       │
       ▼
FastAPI Backend
       │
       ▼
LangGraph AI Agent
       │
       ▼
AI Tools
       │
       ▼
Groq LLM (gemma2-9b-it)
       │
       ▼
SQL Database


🛠️ Technology Stack

Frontend

React.js

Axios (API communication)

Used for building the interactive UI including:

Interaction Form

AI Assistant

Voice Recorder

Interaction History



Backend

FastAPI (Python)

Handles:

API endpoints

interaction processing

voice transcription

AI workflow execution


AI Framework


LangGraph

LangGraph orchestrates the AI workflow and coordinates multiple tools such as:

summarizing interactions

generating follow-ups

logging interaction data

Large Language Model

Groq – gemma2-9b-it

Used for:

interaction summarization

entity extraction

follow-up generation

Database

SQLite + SQLAlchemy

Stores structured interaction records including:

doctor name

topics discussed

materials shared

samples distributed

sentiment

outcomes

follow-up actions


📂 Project Structure

ai-first-crm
│
├── backend
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── requirements.txt
│
│   ├── agents
│   │   └── langgraph_agent.py
│
│   ├── tools
│   │   ├── summarize_interaction.py
│   │   ├── suggest_followups.py
│   │   ├── log_interaction.py
│   │   ├── search_hcp.py
│   │   └── voice_transcribe.py
│
│   ├── models
│   │   └── interaction_model.py
│
│   ├── schemas
│   │   └── interaction_schema.py
│
│   └── routes
│       ├── interaction_routes.py
│       └── voice_routes.py
│
├── frontend
│   └── src
│       ├── App.js
│       └── components
│           ├── InteractionForm.js
│           ├── AIAssistant.js
│           ├── VoiceRecorder.js
│           └── InteractionHistory.js
│
└── README.md

📈 Benefits of AI-First CRM

Reduces manual data entry

Automates interaction summarization

Generates intelligent follow-up suggestions

Maintains structured interaction records

Improves efficiency for pharmaceutical representatives

🔮 Future Improvements

Integration with real hospital databases

AI-powered analytics dashboard

Mobile application for field representatives

Meeting audio transcription automation

👩‍💻 Author

Kotha Seshupavani
Computer Science Engineering

AI-First CRM – HCP Interaction
