from state.travel_state import TravelState
from utils.logger import setup_logger

logger = setup_logger("AccommodationAgent")

def accommodation_node(state: TravelState) -> TravelState:
    """
    Accommodation Agent: Finds and recommends hotels.
    (Student 3 will implement the LLM call and logic here).
    """
    logger.info("Accommodation Agent Started")
    
    # TODO: Implement tool call to tools.hotel_tool and update state
    # e.g., result = search_hotels(state["destination"], state["budget"]["hotel_cost"])
    
    # Mocking the state update for scaffolding
    state["hotels"] = []
    
    logger.info("Accommodation Agent Finished")
    return state
