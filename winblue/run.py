from __future__ import absolute_import

from sys import argv
from Registry import Registry
from pprint import pprint
from .constants import *


def descend(key, maxdepth=None):
    if maxdepth == 0:
        return Ellipsis
    elif maxdepth:
        maxdepth -= 1
    out = {key.name(): {}}
    for value in key.values():
        out[key.name()][value.name()] = value.value()
    for subkey in key.subkeys():
        out[key.name()][subkey.name()] = descend(subkey, maxdepth)
    return out

def main():
    regfile=argv[1]
    hive = Registry.Registry(regfile)

    le = hive.open(PATHS['btle'])
    pprint(descend(le, MAXDEPTH), indent=2)
