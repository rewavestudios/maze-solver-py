# Maze Solver Game

<div align="center">
<img src="assets/maze-solver.gif" width="500" height="400">
</div>

## Setup

Before we dive into the project, let's make sure you are all set up properly. You will need:

- A code editor. I use [VS Code](https://code.visualstudio.com/), though you can use whatever you're comfortable with.
- A command line. If you work on macOS/Linux, the instructions will be in Bash. If you're on Windows, I recommend [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) because it will allow you to use Linux commands.
- [Python 3](https://www.python.org/downloads/) installed.

### What Are We Building?

We'll be building this awesome maze generator and solver!

## Tkinter

Let's just get a graphical window up and running. [Tkinter](https://docs.python.org/3/library/tkinter.html) is a Python library that allows us to create simple graphical user interfaces (GUIs) for our programs. It isn’t game-specific like Pygame. Instead, it’s more tailored toward creating desktop applications. In our case, however, we’ll mainly use it as a simple canvas for drawing lines. When we run our code, it should open a new window with a blank canvas that our program can then draw on.

Let's start by just making sure that your `tkinter` installation is working. Run the following command in your terminal to see if it's installed:

```
python3 -m tkinter
```

You should see a little window pop up with some buttons inside.

Current code status:

- The implementation lives under `src/` now. Key modules are:
	- `src/graphics.py` — `Window`, `Point`, `Line`, and `Cell` primitives used for drawing.
	- `src/cell.py` — alternative `Cell` implementation used by the `Maze` demo.
	- `src/maze.py` — `Maze` class that creates a grid of `Cell` instances and animates their drawing.
	- `src/main.py` — demo script that constructs a Maze and displays it.

How to run the demos:

- Quick maze demo (3x4) — uses `src` imports via a small wrapper:

```bash
python3 run_maze_demo.py
```

- Full maze demo (12x16) — run the src demo directly (executes with `src` on sys.path):

```bash
python3 src/main.py
```

Both will open a Tkinter window and animate the drawing of the maze; close the window to exit (you should see `window closed...` printed).

### Randomness / Seeding

The maze generation uses randomness to carve passages. For reproducible mazes (useful while testing or debugging), `Maze` accepts an optional `seed` parameter. When you pass a fixed integer (for example `10`) the same maze will be generated every run. If you omit the `seed` argument, a different maze will be produced each run.

Example (see `src/main.py`):

```python
maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=10)
```

For automated tests, the `Cell` object exposes a `visited` flag that the generator uses internally to track progress while carving passages.

#### Troubleshooting

If you're seeing an error like this:

```
ModuleNotFoundError: No module named '_tkinter'
```

You're missing the dependency. Check to see which version of Python you're using:

```
python3 --version
```

You should be on 3.10 or higher. If you're not, update your Python version and try `python3 -m tkinter` again.

If that's still not working, it's important to understand that `tkinter` depends on the Tcl/Tk library. Installing the `tk-dev` or `python3-tk` packages are usually the easiest way to install and link it to your Python version. On Ubuntu (Linux), run:

```
sudo apt-get install python3-tk
```

On macOS, make sure you have [Homebrew](https://brew.sh/) installed, and then run:

```
brew install python-tk
```

Your versions of `python-tk` and Python should match!

If `python3 -m tkinter` still isn't working, try uninstalling and reinstalling Python so that it links to the now-available Tcl/Tk library.

### Current status (repository):

- `graphics.py` includes `Window.draw_move(to_cell, undo=False, from_cell=None)` which computes centers via `Cell.center()` and draws a `Line` between them in the correct color. The window tracks the last cell so successive `draw_move` calls draw a path.
- `main.py` demonstrates forward moves and an undo/backtrack between sample cells. Run `python3 main.py` to see it visually.

Manual test steps (quick):

```bash
python3 main.py
```

Close the window to finish; the program will print `window closed...` when it exits.

## Running Unit Tests

We added a simple test suite that checks Maze creation without requiring a GUI.

Run the tests from the repository root (they add `src/` to `sys.path` automatically):

```bash
python3 tests.py
```

The tests use Python's `unittest` module and verify that `Maze` constructs the expected 2D `__cells` structure for several sizes.

## 👏 Contributing

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.