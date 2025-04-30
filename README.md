# Astro-Synth

A high-performance N-body gravity simulator in Python, with an optional C-accelerated core for real-time visualization of planetary and custom star systems.

---

## 🔧 Requirements

- **Python** ≥ 3.10  
- (Optional) A C compiler for the native integration backend

---

## 🚀 Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/zannenmugen/Astro-Synth.git
   cd AstroSynth
   ```
2. Install dependencies:
   ```bash
   pip install .
   ```

---

## 🏃‍♀️ Usage

```bash
python orbit_sim [--numpy] [--resolution WIDTH HEIGHT]
```

- `--numpy` (or `-n`): Run the simulation using NumPy instead of the C backend.
- `--resolution` (or `-r`): Override the default window size:
  ```bash
  python astrosynth --resolution 1280 720
  ```

---

## 🌌 Available Systems

| System         | Description                                                 |
| -------------- | ----------------------------------------------------------- |
| `Void`         | An empty space for custom setups                            |
| `figure-8`     | Three bodies tracing a stable figure-8 trajectory           |
| `pyth-3-body`  | Three stars at the sides of a 3–4–5 triangle                |
| `solar_system` | The Sun and planets, using JPL Horizon ephemerides (2024)   |

---

## 🎮 Controls

| Action                         | Key / Mouse                             |
| ------------------------------ | --------------------------------------- |
| Move camera                    | W A S D / ↑ ↓ ← →                       |
| Open menu                      | Esc                                     |
| Pause                          | P                                       |
| Toggle full-screen             | F                                       |
| Hide UI                        | H                                       |
| Reset simulation               | R                                       |
| Spawn a new star               | Right-click & drag for initial velocity |
| Adjust parameter (hover + scroll) | Left-click parameter in the sidebar |
| Switch integrator              | Left-click integrator in the sidebar    |

---

## 🔢 Integrators

### Fixed-step methods
- **Euler**
- **Euler–Cromer**
- **Runge–Kutta 4 (RK4)**
- **Leapfrog**

### Adaptive-step methods  
Recommended tolerances are shown in parentheses:

| Method                                | Order  | Tolerance Range   |
| ------------------------------------- | ------ | ----------------- |
| RKF 4(5) (Runge–Kutta–Fehlberg)       | 4(5)   | 1e-8 – 1e-14      |
| DOPRI 5(4) (Dormand–Prince)           | 5(4)   | 1e-8 – 1e-14      |
| DVERK 6(5) (Verner’s)                 | 6(5)   | 1e-8 – 1e-14      |
| RKF 7(8)                              | 7(8)   | 1e-4 – 1e-8       |
| **IAS15** (Implicit, 15th-order)      | 15     | ~1e-9 (recommended)|

> 💡 **Tip:** For chaotic setups (e.g., the Pythagorean three-body), RK4 needs dt ≤ 2×10⁻⁸ days to maintain accuracy.

> ⚠️ **Warning:** Changing integrators or dt mid-simulation can introduce numerical artifacts.

---


