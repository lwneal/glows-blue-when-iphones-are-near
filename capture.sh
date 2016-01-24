#!/bin/bash
trap "exit" INT

gstdbuf -i0 -o0 -e0 tshark -I -i en0 -Tfields -e wlan.sa 2>/dev/null | python parse.py
