from typing import TypedDict, List, Dict, Optional

class TravelState(TypedDict):
    """
    The global state for the TripGenie LangGraph workflow.
    This state is passed between all agents.
    """
    user_request: str
    destination: Optional[str]
    days: Optional[int]
    travelers: Optional[int]
    budget_type: Optional[str]
    budget: Optional[Dict]
    hotels: Optional[List[Dict]]
    activities: Optional[List[Dict]]
    itinerary: Optional[str]
    logs: List[str]
