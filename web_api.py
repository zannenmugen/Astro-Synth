from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Import your headless simulation function
from astrosynth import simulate

app = FastAPI(
    title="AstroSynth API",
    version="1.0",
    description="HTTP API for running N-body gravity simulations"
)

# Enable CORS for any origin (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    """Simple health check endpoint"""
    return {"status": "ok"}

@app.get("/simulate", tags=["Simulation"])
async def run_simulation(
    system: str = Query(
        "solar_system", 
        description="Preset system name (e.g., solar_system, figure-8, pyth-3-body)"
    ),
    steps: int = Query(
        1000, ge=1, le=100000,
        description="Number of timesteps to simulate"
    ),
    dt: float = Query(
        0.01, gt=0,
        description="Time step size (days)"
    ),
):
    """
    Run the N-body simulation and return the final state.

    Returns a JSON object containing:
      - positions: list of [x, y] coordinates for each body
      - velocities: list of [vx, vy] for each body
      - energy: total system energy
      - steps: number of steps executed
      - dt: timestep size used
    """
    result = simulate(system=system, steps=steps, dt=dt)
    return JSONResponse(content=result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "web_api:app",
        host="0.0.0.0",
        port=int(
            __import__('os').environ.get('PORT', 8000)
        ),
        log_level="info"
    )
