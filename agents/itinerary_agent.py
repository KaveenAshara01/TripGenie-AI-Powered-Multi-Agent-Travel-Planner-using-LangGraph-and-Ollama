from state.travel_state import TravelState
from utils.logger import setup_logger

logger = setup_logger("ItineraryAgent")

def itinerary_node(state: TravelState) -> TravelState:
    """
    Itinerary Agent: Recommends activities and formats the final schedule.
    (Student 4 will implement the LLM call and logic here).
    """
    logger.info("Itinerary Agent Started")
    
    # TODO: Implement tool call to tools.activity_tool and schedule_tool
    
    # Mocking the state update for scaffolding
    state["activities"] = []
    state["itinerary"] = "Mock Itinerary"
    
    logger.info("Itinerary Agent Finished")
    return state
