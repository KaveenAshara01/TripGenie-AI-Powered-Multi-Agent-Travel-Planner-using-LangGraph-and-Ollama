def parse_travel_request(request: str) -> dict[str, str | int]:
    """
    Parses the user's natural language request to extract constraints.
    (Student 1 will implement the actual parsing logic here using LLM or Regex).
    
    Args:
        request (str): The raw input from the user.
        
    Returns:
        dict: A dictionary containing 'destination', 'days', 'travelers', and 'budget_type'.
    """
    # TODO: Implement extraction logic
    return {
        "destination": "Unknown",
        "days": 0,
        "travelers": 0,
        "budget_type": "standard"
    }
