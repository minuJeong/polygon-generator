
class Mesh(object):
    def __init__(self, verts, faces):
        self.verts, self.faces = verts, faces


class Vertex(object):
    index = 0
    x, y, z = None, None, None

    def __init__(self, x, y, z, index=0):
        self.x, self.y, self.z = x, y, z
        self.index = index

    def pos(self):
        return self.x, self.y, self.z


class Quad(object):
    verts = []

    def __init__(self, verts):
        """ @param verts: iterable of vertices, length should be 4 """
        assert len(verts) == 4, "can initialize with 4 vertices"
        self.verts += [
            verts[1], verts[0], verts[2],
            verts[2], verts[0], verts[3]
        ]

    def indices(self):
        return list(map(lambda x: x.index, self.verts))
