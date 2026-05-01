import json
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from state.travel_state import TravelState
from utils.logger import setup_logger
from tools.hotel_tool import search_hotels

logger = setup_logger("AccommodationAgent")

# Initialize the local LLM
llm = ChatOllama(model="llama3", temperature=0)

SYSTEM_PROMPT = """
You are the Accommodation Agent for TripGenie.
Given a list of available hotels matching the user's constraints, you must select the absolute best one based on rating.
Return ONLY a JSON object of your chosen hotel. Do not include any conversational text, markdown formatting, or backticks.
If the list is empty, return: {"name": "No hotel found", "price_per_night": 0, "rating": 0}
"""

def accommodation_node(state: TravelState) -> TravelState:
    """
    Accommodation Agent: Finds and recommends hotels using the tool and Llama3.
    """
    logger.info("Accommodation Agent Started")
    
    destination = state.get("destination", "Unknown")
    budget_type = state.get("budget_type", "standard")
    
    # 1. Use the custom tool to fetch filtered data
    available_hotels = search_hotels(destination, budget_type)
    logger.info(f"Tool Found Hotels: {len(available_hotels)}")
    
    if not available_hotels:
        state["hotels"] = [{"name": f"No {budget_type} hotel found in {destination}", "price_per_night": 0, "rating": 0}]
        return state
        
    # 2. Use LLM to reason and pick the best option
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Here are the available hotels: {json.dumps(available_hotels)}")
    ]
    
    try:
        logger.info("Calling Llama3 LLM to select the best hotel...")
        response = llm.invoke(messages)
        content = response.content.strip()
        
        # Clean up markdown if the LLM hallucinates it
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        chosen_hotel = json.loads(content.strip())
        logger.info(f"LLM Chosen Hotel: {chosen_hotel}")
        
        state["hotels"] = [chosen_hotel]
        
    except Exception as e:
        logger.warning(f"LLM selection failed. Defaulting to top tool result. Error: {e}")
        # Fallback to the top result from the tool's deterministic sorting
        state["hotels"] = [available_hotels[0]]
        
    logger.info("Accommodation Agent Finished")
    return state
