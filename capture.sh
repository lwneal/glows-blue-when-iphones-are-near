#!/bin/bash
trap "exit" INT
set -e

INTERFACE=wlan1
echo "Starting to capture on interface $INTERFACE"
stdbuf -i0 -o0 -e0 tshark -I -i $INTERFACE -Tfields -e wlan.sa -e radiotap.dbm_antsignal 2>/dev/null | python parse.py
