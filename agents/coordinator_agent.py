from state.travel_state import TravelState
from utils.logger import setup_logger

logger = setup_logger("CoordinatorAgent")

def coordinator_node(state: TravelState) -> TravelState:
    """
    Coordinator Agent: Parses user input and populates initial constraints.
    (Student 1 will implement the LLM call and logic here).
    """
    logger.info("Coordinator Agent Started")
    logger.info(f"Input request: {state.get('user_request')}")
    
    # TODO: Implement tool call to tools.input_parser and update state
    # e.g., result = parse_travel_request(state["user_request"])
    
    # Mocking the state update for scaffolding
    state["destination"] = "Unknown"
    state["days"] = 0
    state["travelers"] = 0
    state["budget_type"] = "standard"
    
    logger.info("Coordinator Agent Finished")
    return state
