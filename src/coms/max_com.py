
import MaxPlus


def generate_mesh_in_3dsmax(meshatom):
    """
    @param mesh: atom mesh
    """

    meshcls = MaxPlus.ClassIds.TriMeshGeometry
    geom = MaxPlus.Factory.CreateGeomObject(meshcls)
    tri = MaxPlus.TriObject._CastFrom(geom)

    verts = meshatom.verts
    faces = meshatom.faces

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
