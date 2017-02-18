import sys
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class GridObject:
    def __init__(self, screenWidth, screenHeight):
        self.originX = 0.0
        self.originY = 0.0
        self.originZ = 0.0
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def drawX(self):
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(self.screenWidth/2.0, 0, 0)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(self.screenWidth/-2.0, 0, 0)
        glEnd()

    def drawY(self):
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, self.screenHeight/2.0, 0)
        glEnd()
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(0.0, self.screenHeight/-2.0, 0)
        glEnd()    

    def draw(self):
        glLineWidth(0.5)
        glColor3f(0.0, 1.0, 0.0)
        self.drawX()
        self.drawY()
       

class CubeObject:
    
    def __init__(self):
        self.verticies = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )
        self.edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
            )

    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glLineWidth(1.0)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()

class Scene:

    def __init__(self):
        self.objects = {}

    def addObject(self, newObject, objectName):
        self.objects[objectName] = newObject

    def render(self):
        for k, obj in self.objects.items():
            obj.draw()

class TheGui:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = (self.width, self.height)
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (self.display[0]/self.display[1]), 0.3, 50.0)
        glTranslatef(0.0, 0.0, -10.0)
                
    def navigationEvents(self):
        keys = pygame.key.get_pressed()
        bump = .01
        if keys[pygame.K_UP]:
            if keys[pygame.K_LEFT]:
                glTranslatef(bump, bump, 0.0)
            elif keys[pygame.K_RIGHT]:
                glTranslatef(-bump, bump, 0.0)
            elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                glTranslatef(0.0, 0.0, -bump)
            else:
                glTranslatef(0.0, bump,0.0)
        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                glTranslatef(bump, -bump, 0.0)
            elif keys[pygame.K_RIGHT]:
                glTranslatef(-bump, -bump, 0.0)
            elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                glTranslatef(0.0, 0.0, bump)
            else:
                glTranslatef(0.0, -bump, 0.0)
        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                glTranslatef(bump, bump, 0.0)
            elif keys[pygame.K_DOWN]:
                glTranslatef(bump, -bump, 0.0)
            elif keys[pygame.K_LCTRL]:
                glTranslatef(0.0, 0.0, 0.0)
            else:
                glTranslatef(bump, 0.0, 0.0)
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                glTranslatef(-bump, bump, 0.0)
            elif keys[pygame.K_DOWN]:
                glTranslatef(-bump, -bump)
            else:
                glTranslatef(-bump, 0.0, 0.0)
                
        
    def handleEvents(self):
        self.navigationEvents()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
   
    def start(self, scene):
        while True:
                self.handleEvents()
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                scene.render()
                pygame.display.flip()
                pygame.time.wait(10)
              
gui = TheGui(800, 800)
scene = Scene()
cube = CubeObject()
grid = GridObject(gui.width, gui.height)
scene.addObject(cube, "cube")
scene.addObject(grid, "grid")
gui.start(scene)

