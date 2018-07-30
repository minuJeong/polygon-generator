
class Vertex(object):
    index = 0
    x, y, z = None, None, None

    def __init__(self, x, y, z, index=0):
        self.x, self.y, self.z = x, y, z
        self.index = index

    def pos(self):
        return self.x, self.y, self.z
