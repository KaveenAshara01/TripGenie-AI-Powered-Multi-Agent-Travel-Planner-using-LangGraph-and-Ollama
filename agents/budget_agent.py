import json
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from state.travel_state import TravelState
from utils.logger import setup_logger
from tools.budget_tool import calculate_trip_budget

logger = setup_logger("BudgetAgent")

# Initialize the local LLM
llm = ChatOllama(model="llama3", temperature=0.7)

SYSTEM_PROMPT = """
You are the Budget Agent for TripGenie. Your job is to review the calculated budget for the trip and provide a short, single-sentence financial tip for the travelers based on their destination and budget type.
Do NOT include any markdown, formatting, or conversational filler. Just return the sentence.
"""

def budget_node(state: TravelState) -> TravelState:
    """
    Budget Agent: Estimates costs based on constraints and generates a personalized tip.
    """
    logger.info("Budget Agent Started")
    
    destination = state.get("destination", "Unknown")
    days = state.get("days", 1)
    travelers = state.get("travelers", 1)
    budget_type = state.get("budget_type", "standard")
    
    # 1. Use the Custom Tool to do the deterministic math (Requirement 2)
    budget_result = calculate_trip_budget(
        destination=destination,
        days=days,
        travelers=travelers,
        budget_type=budget_type
    )
    logger.info(f"Tool Calculated Budget: {budget_result}")
    
    state["budget"] = budget_result
    
    # 2. Use the LLM to generate a contextual budget tip (Requirement 1)
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Trip: {days} days to {destination} for {travelers} people on a {budget_type} budget. Total Cost: LKR {budget_result['total_cost']}.")
    ]
    
    try:
        logger.info("Calling Llama3 LLM to generate budget tip...")
        response = llm.invoke(messages)
        tip = response.content.strip()
        
        # Clean up any quotes
        if tip.startswith('"') and tip.endswith('"'):
            tip = tip[1:-1]
            
        logger.info(f"LLM Budget Tip: {tip}")
        state["budget"]["tip"] = tip
    except Exception as e:
        logger.warning(f"Ollama failed or is offline. Defaulting tip. Error: {e}")
        state["budget"]["tip"] = "Try booking accommodations early to save money!"
    
    logger.info("Budget Agent Finished")
    return state
