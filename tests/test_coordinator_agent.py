import pytest
from agents.coordinator_agent import coordinator_node

# NOTE: These tests require Ollama to be running locally with the "llama3" model.

def test_coordinator_agent_basic_extraction():
    """
    Tests the coordinator agent with a straightforward query.
    This acts as an LLM-as-a-judge implicit test, validating the output schema and accuracy.
    """
    initial_state = {
        "user_request": "Plan a 5 day luxury trip to Galle for 4 people.",
        "logs": []
    }
    
    # Run the LangGraph Node function
    final_state = coordinator_node(initial_state)
    
    # Assertions to ensure LLM accuracy and tool validation
    assert final_state.get("destination", "").lower() == "galle"
    assert final_state.get("days") == 5
    assert final_state.get("travelers") == 4
    assert final_state.get("budget_type") == "luxury"

def test_coordinator_agent_edge_case():
    """
    Tests the coordinator agent's ability to handle missing info and fallback to safe defaults.
    """
    initial_state = {
        "user_request": "I want to go to Ella.",
        "logs": []
    }
    
    final_state = coordinator_node(initial_state)
    
    # Check that defaults and tool validations kicked in safely
    assert final_state.get("destination", "").lower() == "ella"
    assert final_state.get("days") >= 1
    assert final_state.get("travelers") >= 1
    assert final_state.get("budget_type") in ["budget", "standard", "luxury"]
