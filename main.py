from graph import create_tripgenie_graph

def run_tripgenie():
    print("==============================")
    print("   Welcome to TripGenie!      ")
    print("==============================")
    user_input = input("Enter your travel request:\n> ")

    graph = create_tripgenie_graph()
    
    initial_state = {
        "user_request": user_input,
        "destination": None,
        "days": None,
        "travelers": None,
        "budget_type": None,
        "budget": None,
        "hotels": None,
        "activities": None,
        "itinerary": None,
        "logs": []
    }

    print("\n--- Planning your trip, please wait... ---\n")
    
    # Stream the graph execution
    final_output = None
    for output in graph.stream(initial_state):
        for node_name, state in output.items():
            print(f"[{node_name}] processed...")
            final_output = state
            
    print("\n==============================")
    print("       Final Itinerary        ")
    print("==============================")
    
    if final_output and final_output.get("itinerary"):
        print(final_output["itinerary"])
    else:
        print("No itinerary was generated. The agents are still under construction!")

if __name__ == "__main__":
    run_tripgenie()
