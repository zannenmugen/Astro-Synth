from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from astrosynth import simulate

app = FastAPI(title="AstroSynth Simulation API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/simulate")
async def run_simulation(
    system: str = Query("solar_system", description="Preset system name"),
    steps: int = Query(1000, ge=1, le=100000, description="Number of timesteps"),
    dt: float = Query(0.01, gt=0, description="Time step size")
):
    """
    Run an N-body simulation and return the final state.
    """
    # simulate() should return a JSON-serializable dict,
    # e.g. {"positions": [...], "velocities": [...], "metadata": {...}}
    result = simulate(system=system, steps=steps, dt=dt)
    return JSONResponse(content=result)
