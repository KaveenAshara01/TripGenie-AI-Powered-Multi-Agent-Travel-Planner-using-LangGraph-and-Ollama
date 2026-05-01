def calculate_trip_budget(destination: str, days: int, travelers: int, budget_type: str) -> dict[str, int]:
    """
    Calculates the estimated travel expenses for a given destination and duration.
    (Student 2 will implement the specific logic).
    
    Args:
        destination (str): The target destination (e.g., 'Galle', 'Kandy').
        days (int): Number of days for the trip.
        travelers (int): Number of people traveling.
        budget_type (str): The tier of budget ('budget', 'standard', 'luxury').
        
    Returns:
        dict: A breakdown of estimated costs (total, hotel, food, transport, activities).
    """
    # TODO: Implement calculation logic based on inputs
    return {
        "total_cost": 0,
        "hotel_cost": 0,
        "food_cost": 0,
        "transport_cost": 0,
        "activities_cost": 0
    }
