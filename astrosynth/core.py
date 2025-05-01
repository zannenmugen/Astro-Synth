# astrosynth/core.py

from settings import Settings
from simulator import Simulator
from stats import Stats
from camera import Camera
from grav_obj import Grav_obj
import math

def simulate(system: str = "solar_system", steps: int = 1000, dt: float = 0.01):
    """
    Run `steps` timesteps of size `dt` on the named preset, 
    then return final positions, velocities, and energy.
    """
    # 1. Create a dummy Settings (resolution doesn’t matter)
    settings = Settings(screen_width=1, screen_height=1)
    settings.load_system(system)     # you’ll need to expose your presets here

    # 2. Build initial objects
    grav_objs = []
    for spec in settings.initial_bodies:
        grav_objs.append(Grav_obj.from_spec(spec))

    # 3. Wire up Stats, Camera, Simulator
    stats    = Stats(settings)
    camera   = Camera()
    simulator= Simulator(settings, stats, camera, grav_objs)
    simulator.dt = dt

    # 4. Step the sim headlessly
    for _ in range(steps):
        simulator.run_simulation()
        simulator.unload_value()
        if math.isnan(stats.total_energy):
            break

    # 5. Collect results
    return {
        "positions":  [ (o.pos.x, o.pos.y) for o in grav_objs ],
        "velocities": [ (o.vel.x, o.vel.y) for o in grav_objs ],
        "energy":     stats.total_energy,
        "steps":      steps,
        "dt":         dt
    }
