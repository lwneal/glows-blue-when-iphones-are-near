#!/usr/bin/env python
import sys
import time
import fileinput
import subprocess
import blue

WINDOW_LEN_SEC = 8

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


def parse_line(line):
    words = line.split()
    org_unique_id = words[0][:8].lower()
    device_name = unique_device_name(line[9:17])
    manufacturer = oui_map.get(org_unique_id) or 'Unknown'
    rssi = int(words[1].split(',')[0])
    return manufacturer, rssi


pings = []
def process_pings():
    global pings
    limit = time.time() - WINDOW_LEN_SEC
    pings = [(t, rssi) for (t, rssi) in pings if limit < t]


def clamp(value, minimum, maximum):
    return min(maximum, max(value, minimum))


def calculate_blue_level(pings):
    MIN_RSSI = -100  # Start glowing
    MAX_RSSI = -70  # Glow brightly to alert the fellowship of danger!
    if not pings:
        return 0
    max_rssi = max(rssi for (timestamp, rssi) in pings)
    closest = clamp(max_rssi, MIN_RSSI, MAX_RSSI)
    return 1 + (closest + 100) * 6


if __name__ == '__main__':
    oui_map = parse_oui_db()
    blue.glow_blue(1)
    last_set_time = 0
    while True:
        line = sys.stdin.readline()
        try:
            mfr, rssi = parse_line(line)
        except:
            continue
        if mfr.lower().startswith('apple'):
            sys.stdout.write('{} {}\n'.format(mfr, rssi))
            pings.append( (time.time(), rssi) )
            print '{} {} {}'.format(line, mfr, rssi)
        if time.time() - last_set_time > 1.0:
            process_pings()
            brightness = calculate_blue_level(pings)
            print('Blue level is {}'.format(brightness))
            blue.glow_blue(brightness)
            last_set_time = time.time()
