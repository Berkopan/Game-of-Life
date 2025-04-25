# 🧬 Game of Life (Pygame)

---

## Features

- Interactive cell editing with mouse
- Real-time Conway's Game of Life simulation
- Start/Stop control via spacebar
- 60 FPS smooth rendering
- Supports classic patterns (Glider, LWSS, Pulsar, etc.)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Berkopan/Game-of-Life.git
cd Game-of-Life
```

2. (Optional but recommended) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
# .\venv\Scripts\activate   # Windows
```

3. Install dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

4. Run the simulation:
```bash
python main.py
```

---

## Usage
| Control         | Action                                           |
|-----------------|--------------------------------------------------|
| `Left Click`    | Toggle cell state (alive/dead)                   |
| `Space`         | Start / Stop simulation                          |
| `Close Window`  | Exit the application                             |
|-----------------|--------------------------------------------------|