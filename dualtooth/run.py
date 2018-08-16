from __future__ import absolute_import

from sys import argv
from Registry import Registry
from pprint import pprint
from .constants import *


def descend(key, maxdepth=None):
    if maxdepth < 1:
        return Ellipsis
    elif maxdepth:
        maxdepth -= 1
    out = {}
    for value in key.values():
        out[value.name()] = value.value()
    for subkey in key.subkeys():
        out[subkey.name()] = descend(subkey, maxdepth)
    return out



def get_attrs(dev_id, dev_dict):
    out = {}
    for thing in ['Name', 'VIDType', 'VID', 'PID', 'Version']:
        out[thing] = dev_dict.get(thing) #.rstrip('\x00')
    
    for s4 in [dev_dict[key] for key in dev_dict.keys() if key.startswith('ServicesFor')]:
        for thing in ['LEFlags', 'LEAddressType', 'LEAppearance']:
            out[thing] = s4.get(thing)
        break

    return out


def main():
    regfile=argv[1]
    hive = Registry.Registry(regfile)

    le = hive.open(PATHS['btle'])
    devices = descend(le, MAXDEPTH)

    pprint(devices, indent=2)

    devices = [get_attrs(*dev) for dev in devices['Devices'].items()]
    pprint(devices)
