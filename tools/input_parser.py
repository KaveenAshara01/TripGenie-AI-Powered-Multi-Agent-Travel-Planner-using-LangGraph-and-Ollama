import json

def validate_travel_constraints(destination: str, days: int, travelers: int, budget_type: str) -> dict[str, str | int]:
    """
    Validates and normalizes the travel constraints extracted by the LLM.
    Strictly checks for positive integers and supported budget types.
    
    Args:
        destination (str): The target city.
        days (int): Number of days for the trip. Must be > 0.
        travelers (int): Number of people traveling. Must be > 0.
        budget_type (str): The tier of budget ('budget', 'standard', 'luxury').
        
    Returns:
        dict: A validated dictionary containing the normalized constraints.
              If validation fails for an item, defaults or error messages are provided.
    """
    # Normalize inputs
    days = int(days) if str(days).isdigit() or isinstance(days, int) else 1
    travelers = int(travelers) if str(travelers).isdigit() or isinstance(travelers, int) else 1
    budget_type = str(budget_type).lower()
    
    # Enforce constraints
    if days < 1:
        days = 1
    if travelers < 1:
        travelers = 1
        
    valid_budgets = ["budget", "standard", "luxury"]
    if budget_type not in valid_budgets:
        budget_type = "standard"
        
    return {
        "destination": str(destination).strip(),
        "days": days,
        "travelers": travelers,
        "budget_type": budget_type
    }
