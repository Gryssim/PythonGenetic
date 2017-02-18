from AllObjects import *
from Scene import *
from Gui import *

def main():
    gui = TheGui(800, 800)
    scene = Scene()
    cube = CubeObject()
    grid = GridObject(gui.width, gui.height)
    scene.addObject(cube, "cube")
    scene.addObject(grid, "grid")
    gui.start(scene)

main()

