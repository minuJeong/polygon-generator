
class Vertex(object):
    index = 0
    x, y, z = None, None, None

    def __init__(self, index, x, y, z):
        self.index = index
        self.x, self.y, self.z = x, y, z

    def pos(self):
        return self.x, self.y, self.z
