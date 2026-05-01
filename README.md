# ✈️ TripGenie: AI-Powered Multi-Agent Travel Planner

TripGenie is a locally hosted, offline Multi-Agent System (MAS) that automates the complex process of travel planning. Built with **LangGraph** and **Ollama (Llama 3)**, TripGenie functions as an autonomous team of 4 specialized AI agents that collaboratively perceive a user's travel constraints, reason about budgets and accommodations, utilize custom python tools, and synthesize a complete, day-by-day travel itinerary.

This project was built to satisfy the core architectural components of Agentic AI, running entirely locally with zero cloud costs and ensuring absolute data privacy.

---

## 🏗️ System Architecture & Orchestration

The system utilizes **LangGraph** to orchestrate a deterministic, sequential pipeline of agents. A global `TravelState` dictionary is passed securely between nodes, ensuring complete context retention without data loss.

### The Workflow:
`User Request` ➔ **Coordinator Agent** ➔ **Budget Agent** ➔ **Accommodation Agent** ➔ **Itinerary Agent** ➔ `Final Itinerary`

1. **FastAPI Backend**: Serves as the API layer to invoke the LangGraph execution asynchronously.
2. **Vanilla HTML/JS Frontend**: A modern, glassmorphism-styled UI that communicates with the backend, displaying loading states and rendering the final markdown itinerary.
3. **Observability**: A custom Python `logger` traces all inputs, outputs, LLM reasoning, and tool invocations, saving them to `logs/execution.log`.

---

## 🤖 The Agents & Tools

The workload is distributed among 4 distinct autonomous agents, each equipped with custom, strictly typed Python tools.

### 1. Coordinator Agent (Student 1)
- **Responsibility**: Acts as the entry point. Parses natural language requests to extract strict constraints (destination, days, travelers, budget tier).
- **Custom Tool**: `validate_travel_constraints()` normalizes and validates the LLM's output, ensuring no negative integers or unsupported budget tiers proceed down the pipeline.
- **LLM Prompt Strategy**: Strictly enforces JSON-only output with zero hallucinations.

### 2. Budget Agent (Student 2)
- **Responsibility**: Analyzes the travel constraints to allocate a realistic budget and provides personalized financial tips.
- **Custom Tool**: `calculate_trip_budget()` performs heavy deterministic math (since LLMs struggle with calculations), outputting exact LKR breakdowns for hotels, food, transport, and activities.
- **LLM Prompt Strategy**: Evaluates the final cost to generate a contextual 1-sentence financial tip.

### 3. Accommodation Agent (Student 3)
- **Responsibility**: Recommends the best hotel based on the user's destination and budget constraints.
- **Custom Tool**: `search_hotels()` queries a local JSON dataset, strictly filtering out invalid options and sorting the remainder by rating.
- **LLM Prompt Strategy**: Instructed to evaluate the filtered array of hotels and select the absolute best one based on rating, returning the choice as structured JSON.

### 4. Itinerary Agent (Student 4)
- **Responsibility**: Maps activities into a schedule and generates the final user-facing travel itinerary.
- **Custom Tool**: 
  - `get_local_activities()`: Fetches relevant attractions from the local dataset.
  - `generate_daily_schedule()`: Deterministically divides activities across the requested days into a bare-bones markdown skeleton.
- **LLM Prompt Strategy**: Acts as an expert travel writer, taking the dry skeleton schedule and rewriting it into an exciting, engaging, and personalized travel itinerary.

---

## 🚀 Setup Guide

### Prerequisites
1. **Python 3.10+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com/)

### 1. Download the Local LLM
Ensure Ollama is running in the background, then pull the Llama 3 model by running this command in your terminal:
```bash
ollama run llama3
```
*Note: This downloads a ~4.7GB model to your local machine. You only need to do this once.*

### 2. Install Dependencies
Navigate to this repository's root folder in your terminal and install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## 🎮 Run Guide

### 1. Start the Server
Run the FastAPI application from the root directory:
```bash
python server.py
```

### 2. Access the Application
Open your web browser and navigate to:
**http://localhost:8000/frontend**

### 3. Generate a Trip
Type a natural language prompt into the text box. For example:
> *"Plan a 3-day luxury trip to Kandy for 2 people."*
> *"I want to go to Ella for 4 days on a budget with my 3 friends."*

Watch the UI as the agents collaborate in the background, and view the final generated itinerary!

---

## 🧪 Testing

The project includes an automated testing suite using `pytest`. Each student has contributed specific unit tests, property-based tests, or LLM-as-a-judge tests for their respective agents and tools.

To run the tests:
```bash
pytest tests/
```

---
*Built for SE4010 – CTSE Assignment 2 (Machine Learning)*