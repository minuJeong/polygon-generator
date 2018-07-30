
"""
This module provides some convenient macros to generate basic atoms

author: minu jeong
"""

import sys
import atom

if sys.version[0] == '2':
    reload(atom)


def box(width=10.0, height=10.0, length=10.0):
    """
    generate list of vertices and faces from given width, height, length

    @param width: expand for x axis
    @param height: expand for z axis
    @param length: expand for y axis
    """
    vs = [
        atom.Vertex(-width, -length, -height, 0),
        atom.Vertex(-width, +length, -height, 1),
        atom.Vertex(-width, +length, +height, 2),
        atom.Vertex(-width, -length, +height, 3),
        atom.Vertex(+width, -length, -height, 4),
        atom.Vertex(+width, +length, -height, 5),
        atom.Vertex(+width, +length, +height, 6),
        atom.Vertex(+width, -length, +height, 7)
    ]

    fs = []
    fs += atom.Quad([vs[0], vs[1], vs[2], vs[3]]).indices()
    fs += atom.Quad([vs[4], vs[0], vs[3], vs[7]]).indices()
    fs += atom.Quad([vs[5], vs[4], vs[7], vs[6]]).indices()
    fs += atom.Quad([vs[6], vs[7], vs[3], vs[2]]).indices()
    fs += atom.Quad([vs[1], vs[5], vs[6], vs[2]]).indices()
    fs += atom.Quad([vs[4], vs[5], vs[1], vs[0]]).indices()

    return atom.Mesh(vs, fs)
