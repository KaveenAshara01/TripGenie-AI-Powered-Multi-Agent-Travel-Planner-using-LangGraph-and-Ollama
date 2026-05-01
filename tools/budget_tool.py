def calculate_trip_budget(destination: str, days: int, travelers: int, budget_type: str) -> dict[str, int]:
    """
    Calculates the estimated travel expenses for a given destination and duration.
    
    Args:
        destination (str): The target destination (e.g., 'Galle', 'Kandy').
        days (int): Number of days for the trip.
        travelers (int): Number of people traveling.
        budget_type (str): The tier of budget ('budget', 'standard', 'luxury').
        
    Returns:
        dict: A breakdown of estimated costs in LKR.
    """
    # Define base daily costs per person (in LKR) based on budget type
    base_costs = {
        "budget": {"hotel": 5000, "food": 3000, "transport": 2000, "activities": 2000},
        "standard": {"hotel": 15000, "food": 8000, "transport": 5000, "activities": 5000},
        "luxury": {"hotel": 40000, "food": 20000, "transport": 15000, "activities": 15000}
    }
    
    tier = budget_type.lower()
    if tier not in base_costs:
        tier = "standard"
        
    rates = base_costs[tier]
    
    # Calculate costs
    rooms_needed = (travelers + 1) // 2  # Assume 2 people per room
    
    hotel_cost = rates["hotel"] * days * rooms_needed
    food_cost = rates["food"] * days * travelers
    transport_cost = rates["transport"] * days
    activities_cost = rates["activities"] * days * travelers
    
    total_cost = hotel_cost + food_cost + transport_cost + activities_cost
    
    return {
        "total_cost": total_cost,
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "transport_cost": transport_cost,
        "activities_cost": activities_cost
    }
