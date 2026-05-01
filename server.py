from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from graph import create_tripgenie_graph

app = FastAPI(title="TripGenie API")

# Mount the static frontend files so they are served at the root
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

class TravelRequest(BaseModel):
    user_request: str

# Initialize LangGraph
trip_graph = create_tripgenie_graph()

@app.post("/api/plan-trip")
async def plan_trip(request: TravelRequest):
    initial_state = {
        "user_request": request.user_request,
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
    
    try:
        final_output = None
        # Stream through the LangGraph agents
        for output in trip_graph.stream(initial_state):
            for node_name, state in output.items():
                final_output = state
                
        # Return the processed state to the frontend
        return JSONResponse(content={
            "status": "success",
            "destination": final_output.get("destination"),
            "days": final_output.get("days"),
            "travelers": final_output.get("travelers"),
            "budget_type": final_output.get("budget_type"),
            "budget": final_output.get("budget"),
            "hotels": final_output.get("hotels"),
            "activities": final_output.get("activities"),
            "itinerary": final_output.get("itinerary", "No itinerary generated yet. (Other agents are mocked)")
        })
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)

if __name__ == "__main__":
    print("=========================================================")
    print("🚀 Starting TripGenie Server")
    print("👉 Open your browser to: http://localhost:8000/frontend")
    print("=========================================================")
    uvicorn.run(app, host="0.0.0.0", port=8000)
