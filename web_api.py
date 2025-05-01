# web_api.py
import io
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
# or FileResponse if you want to return images/snapshots
from astrosynth import simulate  # import your main simulation function

app = FastAPI()

@app.get("/simulate")
def run_simulation(
    system: str = Query("solar_system", description="Which preset system to load"),
    steps: int = Query(1000, ge=1, le=100000, description="Number of timesteps"),
    dt: float = Query(0.01, gt=0, description="Timestep size")
):
    """
    Run the simulation and return final positions and velocities as JSON.
    """
    result = simulate(system=system, steps=steps, dt=dt)
    # assume simulate() returns a dict or serializable structure
    return JSONResponse(content=result)

@app.get("/health")
def health_check():
    return {"status": "ok"}
