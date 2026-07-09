from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="AthletIQ Data Pipeline API")

# Allow CORS for the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AthletIQ FastAPI Backend"}

@app.get("/api/metrics/pipeline")
def get_pipeline_metrics():
    # Mock data representing the grassroots-to-podium pipeline
    return {
        "active_profiles": "34K+",
        "talent_clusters": 9,
        "live_leagues": random.randint(15, 30),
        "pipeline_drops": {
            "state_to_zonal": "42%",
            "national_to_elite": "68%"
        }
    }

@app.get("/api/metrics/opportunities")
def get_opportunities():
    return [
        {"id": 1, "type": "Sponsorship", "title": "Elite Archers Need Kit Funding", "urgency": "High"},
        {"id": 2, "type": "Coaching", "title": "NIS Certified Wrestling Coaches Needed", "urgency": "Critical"},
        {"id": 3, "type": "Infrastructure", "title": "Platform Shortage in Assam", "urgency": "Medium"}
    ]
