"""
Main entry point for maze sovler visualizer.
"""
from pygame import init, quit

# local import
from src.gui.gui import GUI


if __name__ == "__main__":
    # initialize all imported pygame modules
    init()
    # start pygame main loop
    gui = GUI()
    gui.loop()
    # uninitialize all pygame modules
    quit()
