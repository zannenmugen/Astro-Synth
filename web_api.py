# web_api.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

# import simulate from wherever you defined it
from astrosynth.core import simulate  

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/simulate")
async def run_simulation(
    system: str = Query("solar_system"),
    steps: int = Query(1000, ge=1),
    dt: float = Query(0.01, gt=0)
):
    result = simulate(system=system, steps=steps, dt=dt)
    return JSONResponse(content=result)
