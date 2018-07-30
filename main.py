
import os

from src.coms.max_com import generate_mesh_in_3dsmax
from src.coms.maya_com import generate_mesh_in_maya

from src.atom import Vertex

CONFIG = {}

def read_config():
    """ require to have '.config' file """

    def parse_conf(line):
        if line == "":
            return

        if line.startswith("#") or line.startswith("//"):
            return
        d = line.split(' ')
        key = d[0].replace(":", "")
        CONFIG[key] = ' '.join(d[1:])

    dirpath = os.path.dirname(__file__)
    config_path = dirpath + "/.config"
    if not os.path.isfile(config_path):
        print("Can't find config file")
        return

    with open(config_path, 'r') as fp:
        context = fp.read()

    list(map(lambda x: parse_conf(x), context.split("\n")))

def gen_quad(verts):
    """ @param verts: iterable of vertices, length should be 4 """
    return [
        verts[1].index, verts[0].index, verts[2].index,
        verts[2].index, verts[0].index, verts[3].index
    ]

def main():
    """ Hello world! """

    read_config()

    v = 10.0
    vs = [
        Vertex(-v, -v, -v, 0),
        Vertex(-v, +v, -v, 1),
        Vertex(-v, +v, +v, 2),
        Vertex(-v, -v, +v, 3),
        Vertex(+v, -v, -v, 4),
        Vertex(+v, +v, -v, 5),
        Vertex(+v, +v, +v, 6),
        Vertex(+v, -v, +v, 7)
    ]

    fs = []
    fs += gen_quad([vs[0], vs[1], vs[2], vs[3]])
    fs += gen_quad([vs[4], vs[0], vs[3], vs[7]])
    fs += gen_quad([vs[5], vs[4], vs[7], vs[6]])
    fs += gen_quad([vs[6], vs[7], vs[3], vs[2]])
    fs += gen_quad([vs[1], vs[5], vs[6], vs[2]])
    fs += gen_quad([vs[4], vs[5], vs[1], vs[0]])

    if CONFIG["MODE"] == "MAX":
        generate_mesh_in_3dsmax(vs, fs)
    elif CONFIG["MODE"] == "MAYA":
        generate_mesh_in_maya(vs, fs)
    else:
        print("Mode is not defined: " + CONFIG["MODE"])


if __name__ == "__main__":
    main()
