from state.travel_state import TravelState
from utils.logger import setup_logger

logger = setup_logger("BudgetAgent")

def budget_node(state: TravelState) -> TravelState:
    """
    Budget Agent: Estimates costs based on constraints.
    (Student 2 will implement the LLM call and logic here).
    """
    logger.info("Budget Agent Started")
    
    # TODO: Implement tool call to tools.budget_tool and update state
    # e.g., result = calculate_trip_budget(state["destination"], ...)
    
    # Mocking the state update for scaffolding
    state["budget"] = {
        "total_cost": 0,
        "hotel_cost": 0,
        "food_cost": 0,
        "transport_cost": 0,
        "activities_cost": 0
    }
    
    logger.info("Budget Agent Finished")
    return state
