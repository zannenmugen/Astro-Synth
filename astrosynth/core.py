# astrosynth/core.py

import math
from grav_obj import Grav_obj
from settings import Settings
from simulator import Simulator
from stats import Stats
from camera import Camera

def simulate(system: str="solar_system", steps: int=1000, dt: float=0.01):
    """
    Run a headless N-body sim for `steps` timesteps of size `dt`
    on the preset `system`, and return a JSON-serializable snapshot.
    """
    # 1) Initialize settings & stats
    settings = Settings(1, 1)    # dummy resolution
    settings.load_system(system) # you’ll need a helper to preset bodies
    stats    = Stats(None)       # no UI, just energy tracking
    camera   = Camera()          # unused, but Simulator depends on it
    
    # 2) Create the initial bodies from your presets
    grav_objs = []
    for spec in settings.initial_bodies:
        grav_objs.append( Grav_obj.from_spec(spec) )
    
    # 3) Wrap them in your Simulator
    sim = Simulator(
        settings=settings,
        stats=stats,
        camera=camera,
        grav_objs=grav_objs
    )
    sim.dt = dt
    
    # 4) Step the sim
    for _ in range(steps):
        sim.run_simulation()
        if math.isnan(stats.total_energy):
            break
    
    # 5) Collect final data
    output = {
        "positions": [ (o.pos.x, o.pos.y) for o in grav_objs ],
        "velocities": [ (o.vel.x, o.vel.y) for o in grav_objs ],
        "energy": stats.total_energy,
        "steps": steps,
        "dt": dt
    }
    return output
