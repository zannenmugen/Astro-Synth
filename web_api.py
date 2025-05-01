# web_api.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from astrosynth.simulator import Simulator
from astrosynth.grav_obj import Grav_obj

app = FastAPI()

def simulate(system: str, steps: int, dt: float):
    # 1. Make a dummy GravitySimulator and populate it:
    from astrosynth.__main__ import GravitySimulator
    grav_sim = GravitySimulator()
    
    # 2. Clear any pre-existing objects and create the requested preset:
    grav_sim.grav_objs.empty()
    getattr(Grav_obj, f"create_{'solor_system' if system=='solar_system' else system}")(grav_sim)
    grav_sim.stats.reset(grav_sim)
    
    # 3. Run the integrator for `steps` timesteps of size dt:
    sim = Simulator(grav_sim)
    for _ in range(steps):
        sim.run_simulation(grav_sim)
    
    # 4. Extract state arrays:
    positions = sim.x.tolist()
    velocities = sim.v.tolist()
    return {"positions": positions, "velocities": velocities}

@app.get("/simulate")
async def run_sim(system: str = Query("solar_system"), 
                  steps: int = Query(1000), 
                  dt: float = Query(0.01)):
    return JSONResponse(content=simulate(system, steps, dt))
