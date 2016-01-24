#!/usr/bin/env python
import sys
import fileinput
import subprocess

def parse_oui_db():
    data = {}
    lines = open('oui.txt').read().splitlines()
    for line in lines:
        words = line.split()
        oui = words[0][:8].lower()
        name = words[1]
        data[oui] = name
    return data


def unique_device_name(mac_bytes):
    return mac_bytes


def get_mfr(line):
    org_unique_id = line[:8].lower()
    device_name = unique_device_name(line[9:17])
    manufacturer = oui_map.get(org_unique_id)
    if manufacturer is not None:
        return '{} {}'.format(manufacturer, device_name)
    else:
        return 'Unknown {} {}'.format(org_unique_id, device_name)


oui_map = parse_oui_db()
while True:
    line = sys.stdin.readline()
    if len(line) > 8:
        sys.stdout.write(get_mfr(line) + '\n')
