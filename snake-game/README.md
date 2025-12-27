# Snake — README

A lightweight Snake game implemented in Python. This README explains the project purpose, how to run it, and where to find the core parts of the code.

## Project overview
- Classic grid-based Snake: move, eat food to grow, avoid collisions.
- Intended for learning game loops, input handling, simple rendering, and game state management.

## Features
- Grid-based movement
- Growing snake with food consumption
- Collision detection (self and walls)
- Score tracking and basic restart

## Prerequisites
- Python 3.8+  
- Recommended: pygame (if using an SDL-based renderer)

Install pygame:
```
pip install pygame
```

## Run
Typical command:
```
python -m src.main
```
(or `python src/main.py` depending on layout)

## Suggested project structure
A clear separation of concerns makes the game easier to maintain and test.

Recommended tree:
```
snake-game/
├─ src/
│  ├─ main.py         # entry point, initializes and runs the game loop
│  ├─ config.py       # constants (GRID_SIZE, CELL_SIZE, FPS, COLORS)
│  ├─ game.py         # Game class: state transitions, update/tick logic
│  ├─ snake.py        # Snake class: position, move, grow, collision checks
│  ├─ food.py         # Food spawning and placement logic
│  ├─ input_handler.py# decoupled input processing and buffering
│  ├─ renderer.py     # drawing code (pygame or terminal renderer)
│  └─ utils.py        # small helpers (random position, vector math)
├─ assets/            # optional images, fonts, sounds
├─ tests/             # unit/integration tests
└─ README.md
```

## Core structures and responsibilities
- src/main.py
    - Creates window, sets up systems (game, renderer), starts the main loop.
- src/config.py
    - Single place for tunable constants: grid dimensions, colors, initial speed.
- src/game.py
    - Holds current score, running flag, and orchestrates update -> input -> render.
    - Handles game-over and restart logic.
- src/snake.py
    - Maintains a deque/list of positions, current direction, move/grow, and self-collision detection.
- src/food.py
    - Generates food in unoccupied grid cells and exposes food position(s).
- src/input_handler.py
    - Maps raw OS events to game actions and implements an input buffer to avoid instant-reverse moves.
- src/renderer.py
    - Encapsulates rendering logic so engine can be swapped (pygame, curses, ASCII).
- tests/
    - Unit tests for snake movement, growth, collision, and food placement.

## Implementation tips
- Use a fixed-timestep game loop (tick at fixed FPS) to keep movement deterministic.
- Represent positions as integer grid coordinates, not pixels; convert to pixels only in renderer.
- Prevent immediate 180° turns by buffering input and validating new direction before applying.
- Keep rendering and game logic separate for easier testing.
- Spawn food by sampling from all free cells (or random trial-regenerate while in a loop).
- Use a deque for the snake body for efficient head/tail operations.
- Keep config values near the top of the repo for quick tuning (speed, grid size).

## Testing & debugging
- Add unit tests for:
    - move() resulting positions
    - grow() increases length as expected
    - collisions detected correctly
    - food not placed on snake
- Add a debug mode: show grid coordinates, spawn food at fixed locations, or a slow FPS.

## Helpful extensions
- Add levels or increasing speed as score thresholds are reached.
- Add walls/obstacles map loaded from file.
- Add persistent high-score storage (simple JSON file).

## License & contributions
- Include a LICENSE file (e.g., MIT) if you plan to share.
- Small PRs and issues welcome — keep changes scoped (one feature/fix per PR).