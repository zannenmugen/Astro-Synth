from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from astrosynth import simulate

app = FastAPI()

@app.get("/simulate")
def run_simulation(
    system: str = Query("solar_system", description="Preset system name"),
    steps:  int = Query(1000, ge=1, le=100000),
    dt:     float = Query(0.01, gt=0),
):
    result = simulate(system=system, steps=steps, dt=dt)
    return JSONResponse(content=result)

@app.get("/health")
def health_check():
    return {"status": "ok"}
