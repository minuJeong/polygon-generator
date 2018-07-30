
import os

from max_com import generate_mesh_in_3dsmax
from maya_com import generate_mesh_in_maya

from atom import Vertex

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

    MODE = CONFIG["MODE"]
    if MODE == "MAX":
        generate_mesh_in_3dsmax(vs, fs)
    elif MODE == "MAYA":
        generate_mesh_in_maya(vs, fs)
    else:
        print("Mode is not defined: " + MODE)


if __name__ == "__main__":
    main()
