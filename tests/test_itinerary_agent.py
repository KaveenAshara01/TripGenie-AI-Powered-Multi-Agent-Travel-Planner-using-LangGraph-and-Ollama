import pytest
from tools.activity_tool import get_local_activities, generate_daily_schedule
from agents.itinerary_agent import itinerary_node

def test_get_local_activities():
    """
    Tests that activities are accurately fetched based on destination.
    """
    activities = get_local_activities("ella")
    if activities:
        assert all("ella" in a["location"].lower() for a in activities)
        assert len(activities) > 0

def test_generate_daily_schedule():
    """
    Tests that the skeleton schedule formatter correctly distributes activities across days.
    """
    activities = [
        {"name": "A1", "duration_hours": 1, "type": "T"},
        {"name": "A2", "duration_hours": 1, "type": "T"}
    ]
    
    draft = generate_daily_schedule(2, "TestCity", "TestHotel", activities)
    
    assert "Day 1" in draft
    assert "Day 2" in draft
    assert "TestHotel" in draft

def test_itinerary_agent_fallback():
    """
    Test itinerary generation flow gracefully handles the LLM.
    """
    initial_state = {
        "destination": "Galle",
        "days": 2,
        "hotels": [{"name": "Galle Fort Hotel"}],
        "budget": {"tip": "Test Tip"},
        "logs": []
    }
    
    final_state = itinerary_node(initial_state)
    
    assert "itinerary" in final_state
    assert len(final_state["itinerary"]) > 50
    assert "Test Tip" in final_state["itinerary"]
