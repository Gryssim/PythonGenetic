class Scene:

    def __init__(self):
        self.objects = {}

    def addObject(self, newObject, objectName):
        self.objects[objectName] = newObject

    def render(self):
        for k, obj in self.objects.items():
            obj.draw()
