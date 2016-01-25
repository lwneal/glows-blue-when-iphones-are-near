#!/usr/bin/env python
import time
import socket

connect_msg = '1014100118002c1c07000fab818a8b96'.decode('hex')
light_off = '3100000000f00f30'.decode('hex')
light_on = '31000000ff0f0f4e'.decode('hex')

# Commands are fixed-length 8 bytes.
# The first 2 bytes specify a command maybe
# The subsequent 5 bytes are parameters
# Last byte is a simple checksum of the previous 7
# Brightness can be 0 to 206
def get_set_color_command(brightness):
    brightness = min(brightness, 206)
    base = list('3100000000f00f30'.decode('hex'))
    base[3] = chr(ord(base[3]) + brightness)
    base[7] = chr(ord(base[7]) + brightness)
    return ''.join(base)


def glow_blue(brightness):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( ('10.10.123.3', 5577) )
    s.send(get_set_color_command(brightness))
