from langgraph.graph import StateGraph, END
from state.travel_state import TravelState
from agents.coordinator_agent import coordinator_node
from agents.budget_agent import budget_node
from agents.accommodation_agent import accommodation_node
from agents.itinerary_agent import itinerary_node

def create_tripgenie_graph():
    """
    Builds the LangGraph state machine.
    """
    workflow = StateGraph(TravelState)

    # Add Nodes
    workflow.add_node("Coordinator", coordinator_node)
    workflow.add_node("Budget", budget_node)
    workflow.add_node("Accommodation", accommodation_node)
    workflow.add_node("Itinerary", itinerary_node)

    # Add Edges
    workflow.set_entry_point("Coordinator")
    workflow.add_edge("Coordinator", "Budget")
    workflow.add_edge("Budget", "Accommodation")
    workflow.add_edge("Accommodation", "Itinerary")
    workflow.add_edge("Itinerary", END)

    # Compile Graph
    return workflow.compile()
