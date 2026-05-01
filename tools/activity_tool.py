import json
import os

def get_local_activities(destination: str) -> list[dict[str, str | int]]:
    """
    Finds attractions and activities for a given destination from the local database.
    
    Args:
        destination (str): The target city.
        
    Returns:
        list[dict]: A list of activity dictionaries for that destination.
    """
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'attractions.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            activities = json.load(f)
    except FileNotFoundError:
        return []

    target_loc = destination.lower()
    
    # Filter by destination
    results = [a for a in activities if target_loc in a['location'].lower()]
    return results

def generate_daily_schedule(days: int, destination: str, hotel_name: str, activities: list[dict[str, str | int]]) -> str:
    """
    Creates a basic markdown string skeleton for an itinerary.
    (The LLM will rewrite this to be exciting, but this tool provides the strict structure)
    """
    schedule = f"# 🌴 Your {days}-Day Trip to {destination}\n\n"
    schedule += f"**🏨 Accommodation**: {hotel_name}\n\n"
    
    if not activities:
        schedule += "No specific activities found for this location. Enjoy a relaxing stay!"
        return schedule
        
    # Simple deterministic distribution of activities across days
    activities_per_day = max(1, len(activities) // days)
    
    for day in range(1, days + 1):
        schedule += f"### Day {day}\n"
        start_idx = (day - 1) * activities_per_day
        end_idx = start_idx + activities_per_day
        
        # If it's the last day, dump all remaining activities
        if day == days:
            day_activities = activities[start_idx:]
        else:
            day_activities = activities[start_idx:end_idx]
            
        if not day_activities:
            schedule += "- Free time to explore or relax.\n"
        else:
            for act in day_activities:
                schedule += f"- **{act['name']}** ({act['duration_hours']} hours) - *{act['type'].capitalize()}*\n"
        schedule += "\n"
        
    return schedule
