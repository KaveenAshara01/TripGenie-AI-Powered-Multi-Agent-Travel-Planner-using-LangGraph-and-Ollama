import json
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from state.travel_state import TravelState
from utils.logger import setup_logger
from tools.input_parser import validate_travel_constraints

logger = setup_logger("CoordinatorAgent")

# Initialize the local LLM. (Assuming Ollama is running on localhost:11434 with llama3 installed)
llm = ChatOllama(model="llama3", temperature=0)

SYSTEM_PROMPT = """
You are the Coordinator Agent for TripGenie. Your job is to extract specific travel constraints from the user's natural language request.
Extract the following information:
- destination: The name of the city or location.
- days: The number of days (integer).
- travelers: The number of people (integer).
- budget_type: Must be exactly one of: "budget", "standard", "luxury". If not specified, guess based on context or default to "standard".

You MUST return ONLY a valid JSON object matching this schema. Do not output any markdown formatting, backticks, or conversational text.
Example Output:
{"destination": "Kandy", "days": 3, "travelers": 2, "budget_type": "luxury"}
"""

def coordinator_node(state: TravelState) -> TravelState:
    """
    Coordinator Agent: Parses user input and populates initial constraints using Llama3.
    """
    logger.info("Coordinator Agent Started")
    user_request = state.get('user_request', '')
    logger.info(f"Input request: {user_request}")
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_request)
    ]
    
    try:
        # Call Ollama
        logger.info("Calling Llama3 LLM to extract constraints...")
        response = llm.invoke(messages)
        content = response.content.strip()
        
        # Clean up any potential markdown formatting the LLM hallucinates
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        extracted_data = json.loads(content.strip())
        logger.info(f"LLM Extracted Raw Data: {extracted_data}")
        
        # Call the Custom Tool to strictly validate the data (Requirement 2)
        validated_data = validate_travel_constraints(
            destination=extracted_data.get("destination", "Unknown"),
            days=extracted_data.get("days", 1),
            travelers=extracted_data.get("travelers", 1),
            budget_type=extracted_data.get("budget_type", "standard")
        )
        logger.info(f"Tool Validated Data: {validated_data}")
        
        # Pass data into Global State (Requirement 3)
        state["destination"] = validated_data["destination"]
        state["days"] = validated_data["days"]
        state["travelers"] = validated_data["travelers"]
        state["budget_type"] = validated_data["budget_type"]
        
    except Exception as e:
        logger.error(f"Failed to parse user request: {e}")
        # Default fallback so the graph doesn't crash entirely
        state["destination"] = "Unknown"
        state["days"] = 1
        state["travelers"] = 1
        state["budget_type"] = "standard"
        
    logger.info("Coordinator Agent Finished")
    return state
