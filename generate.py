
import MaxPlus


def generate_mesh_in_3dsmax(verts, faces):
    """
    @param verts: iterable of position
    @param verts: iterable of int
    """

    meshcls = MaxPlus.ClassIds.TriMeshGeometry
    geom = MaxPlus.Factory.CreateGeomObject(meshcls)
    tri = MaxPlus.TriObject._CastFrom(geom)

    mesh = tri.GetMesh()
    mesh.SetNumVerts(len(verts))
    mesh.SetNumFaces(len(faces) / 3)

    for idx, v in enumerate(verts):
        mesh.SetVert(idx, MaxPlus.Point3(*v.pos()))

    for idx in range(0, len(faces), 3):
        face = mesh.GetFace(idx / 3)
        face.SetVerts(
            faces[idx + 0], faces[idx + 1], faces[idx + 2]
        )

    mesh.InvalidateGeomCache()
    mesh.InvalidateTopologyCache()
    MaxPlus.Factory.CreateNode(tri)


def gen_quad(verts):
    """ @param verts: iterable of vertices, length should be 4 """
    return [
        verts[1].index, verts[0].index, verts[2].index,
        verts[2].index, verts[0].index, verts[3].index
    ]


class Vertex(object):
    index = 0
    x, y, z = None, None, None

    def __init__(self, index, x, y, z):
        self.index = index
        self.x, self.y, self.z = x, y, z

    def pos(self):
        return self.x, self.y, self.z

def main():
    v = 10.0
    vs = [
        Vertex(0, -v, -v, -v),
        Vertex(1, -v, +v, -v),
        Vertex(2, -v, +v, +v),
        Vertex(3, -v, -v, +v),
        Vertex(4, +v, -v, -v),
        Vertex(5, +v, +v, -v),
        Vertex(6, +v, +v, +v),
        Vertex(7, +v, -v, +v)
    ]

    fs = []
    fs += gen_quad([vs[0], vs[1], vs[2], vs[3]])
    fs += gen_quad([vs[4], vs[0], vs[3], vs[7]])
    fs += gen_quad([vs[5], vs[4], vs[7], vs[6]])
    fs += gen_quad([vs[6], vs[7], vs[3], vs[2]])
    fs += gen_quad([vs[1], vs[5], vs[6], vs[2]])
    fs += gen_quad([vs[4], vs[5], vs[1], vs[0]])

    generate_mesh_in_3dsmax(vs, fs)


if __name__ == "__main__":
    main()
