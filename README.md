# Maze solver Game

## Setup

Before we dive into the project, let's make sure you are all set up properly. You will need:

- A code editor. I use VS Code, though you can use whatever you're comfortable with.
- A command line. I work on macOS/Linux, so instructions will be in Bash. I recommend WSL if you're on Windows because it will allow you to use Linux commands. That said, you can use native Windows if you choose; you may just have to convert some commands on your own.
- Python 3 installed.

### What Are We Building?

We'll be building this awesome maze generator and solver! By the end, your code will be rendering mazes like this one:

### Tkinter

Let's start by just making sure that your `tkinter` installation is working. `tkinter` is a Python library that allows us to create simple graphical user interfaces (GUIs) for our programs. It's not game-specific like Pygame; instead it's more tailored to creating desktop GUIs... but in our case we'll really just be using it as a simple canvas to draw lines on.

### Assignment

For most systems, `tkinter` will work out of the box... but let's make sure that it's working for you.

Run the following command in your terminal to see if it's installed:

```
python3 -m tkinter
```

You should see a little window pop up with some buttons inside. If you do, you're done — just submit the CLI tests. Otherwise, continue.

### Troubleshooting

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

On macOS, make sure you have Homebrew installed, and then run:

```
brew install python-tk
```

Your versions of `python-tk` and Python should match!

If `python3 -m tkinter` still isn't working, try uninstalling and reinstalling Python so that it links to the now-available Tcl/Tk library.


## 👏 Contributing

I would love your help! Contribute by forking the repo and opening pull requests. Please ensure that your code passes the existing tests and linting, and write tests to test your changes if applicable.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.