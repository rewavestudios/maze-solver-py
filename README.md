# Maze Solver Game

<div align="center">
<img src="maze-solver.gif" width="500" height="400">
</div>

## Setup

Before we dive into the project, let's make sure you are all set up properly. You will need:

- A code editor. I use [VS Code](https://code.visualstudio.com/), though you can use whatever you're comfortable with.
- A command line. I you work on macOS/Linux, the instructions will be in Bash. If you're on Windows, I recommend [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) because it will allow you to use Linux commands.
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

- The repository already contains an implementation matching these requirements in `graphics.py`.
- The `main.py` entrypoint creates the window and waits for it to close:

```python
from graphics import Window

def main():
		win = Window(800, 600)
		win.wait_for_close()

if __name__ == '__main__':
		main()
```

How to run:

```bash
python3 main.py
```

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

- `graphics.py` implements the `Window` class and also includes `Point` and `Line` classes. The `Line.draw()` method calls `create_line(...)` with `width=2`.
- `Window.draw_line(line, fill_color)` is implemented and forwards the call to `Line.draw()`.
- `main.py` draws several sample lines (a frame, cross lines, and extra samples) and uses `win.redraw()` then `win.wait_for_close()` to display and keep the window open until closed.

## 👏 Contributing

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.