
"""
Polygon Generator
===



This is entry pointof polygon generator.
Make sure this script is compatible with Python 2.7

author: minu jeong
"""

import os
import sys

from src import macros
from src.coms import max_com
from src.coms import maya_com

if sys.version[0] == "2":
    # Need to use this to avoid restarting 3ds max for update
    # Not required for release
    reload(macros)
    reload(max_com)
    reload(maya_com)

CONFIG = {}

def read_config():
    """ require to have '.config' file """
    def parse_conf(line):
        if line == "" or line.startswith("#") or line.startswith("//"):
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
        context = fp.read().lower()

    list(map(lambda x: parse_conf(x), context.split("\n")))


def send_to_dcc(mesh):
    """
    @param mesh: atom mesh
    """
    if CONFIG["mode"] == "max":
        max_com.generate_mesh_in_3dsmax(mesh)
    elif CONFIG["mode"] == "maya":
        maya_com.generate_mesh_in_maya(mesh)
    else:
        print("Mode is not defined: " + CONFIG["mode"])


def main():
    """ Hello world! """
    read_config()

    mesh = macros.box(15, 21, 12)
    send_to_dcc(mesh)


if __name__ == "__main__":
    main()
