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
