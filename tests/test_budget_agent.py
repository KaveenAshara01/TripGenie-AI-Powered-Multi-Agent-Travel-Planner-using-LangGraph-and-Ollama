import pytest
from agents.budget_agent import budget_node
from tools.budget_tool import calculate_trip_budget

def test_calculate_trip_budget_logic():
    """
    Unit test for the budget tool to ensure math is deterministic.
    (Student 2 Testing Requirement)
    """
    result = calculate_trip_budget("Colombo", 2, 2, "budget")
    
    assert result["total_cost"] > 0
    # 2 travelers = 1 room. Budget hotel is 5000/day. 2 days = 10000
    assert result["hotel_cost"] == 5000 * 2 * 1 
    # Budget food is 3000/day/person. 2 days * 2 pax = 12000
    assert result["food_cost"] == 3000 * 2 * 2

def test_budget_agent_flow():
    """
    Test the Budget Agent node flow with LLM invocation.
    """
    initial_state = {
        "destination": "Galle",
        "days": 3,
        "travelers": 2,
        "budget_type": "luxury",
        "logs": []
    }
    
    final_state = budget_node(initial_state)
    
    assert "budget" in final_state
    assert final_state["budget"]["total_cost"] > 0
    assert "tip" in final_state["budget"]
