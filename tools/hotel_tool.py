import json
import os

def search_hotels(destination: str, budget_type: str) -> list[dict[str, str | int | float]]:
    """
    Searches the local hotel database for accommodations matching the destination and budget tier.
    
    Args:
        destination (str): The target city (e.g., 'Galle', 'Kandy').
        budget_type (str): The budget tier ('budget', 'standard', 'luxury').
        
    Returns:
        list[dict]: A list of hotel dictionaries matching the criteria, sorted by rating.
    """
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'hotels.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            hotels = json.load(f)
    except FileNotFoundError:
        return []

    target_loc = destination.lower()
    target_tier = budget_type.lower()
    
    # Filter hotels by location and tier
    results = [
        h for h in hotels 
        if target_loc in h['location'].lower() and h['tier'].lower() == target_tier
    ]
    
    # Sort by rating descending so the best options are first
    results.sort(key=lambda x: x.get('rating', 0), reverse=True)
    
    return results
