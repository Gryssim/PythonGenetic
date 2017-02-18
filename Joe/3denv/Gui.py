import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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
                glTranslatef(-bump, bump, 0.0)
            elif keys[pygame.K_RIGHT]:
                glTranslatef(bump, bump, 0.0)
            elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                glTranslatef(0.0, 0.0, -bump)
            else:
                glTranslatef(0.0, bump,0.0)
        elif keys[pygame.K_DOWN]:
            if keys[pygame.K_LEFT]:
                glTranslatef(-bump, -bump, 0.0)
            elif keys[pygame.K_RIGHT]:
                glTranslatef(bump, -bump, 0.0)
            elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                glTranslatef(0.0, 0.0, bump)
            else:
                glTranslatef(0.0, -bump, 0.0)
        elif keys[pygame.K_LEFT]:
            glTranslatef(-bump, 0.0, 0.0)
        elif keys[pygame.K_RIGHT]:
            glTranslatef(bump, 0.0, 0.0)
                
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
