#!/usr/bin/env python
import time
import socket

"""
s_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# TODO: Is the UDP thing necessary?
s_send.sendto("HF-A11ASSISTHREAD", ('10.10.123.3', 51820))

s_listen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_listen.bind(('0.0.0.0', 48899))
while True:
    print 'sending packet'
    s_send.sendto("HF-A11ASSISTHREAD", ('10.10.123.3', 51820))
    print s_listen.recvfrom(2048)
"""

connect_msg = '1014100118002c1c07000fab818a8b96'.decode('hex')
light_off = '3100000000f00f30'.decode('hex')
light_on = '31000000ff0f0f4e'.decode('hex')

# Commands are fixed-length 8 bytes.
# The first 2 bytes specify a command maybe
# The subsequent 5 bytes are parameters
# Last byte is a simple checksum of the previous 7
blue_levels = [
    '3100000c00f00f3c'.decode('hex'),
    '3100012600f00f57'.decode('hex'),
    '3100034c00f00f7f'.decode('hex'),
    '3100057d00f00fb2'.decode('hex'),
    '3100069900f00fcf'.decode('hex'),
    '310007b500f00fec'.decode('hex'),
    '310009d700f00f10'.decode('hex'),
]

blue_levels = ['3100000000f00f30'.decode('hex')]

# Brightness can be 0 to 255
def get_set_color_command(brightness):
    base = list('3100000000f00f30'.decode('hex'))
    base[3] = chr(ord(base[3]) + brightness)
    base[7] = chr(ord(base[7]) + brightness)
    return ''.join(base)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( ('10.10.123.3', 5577) )

while True:
    for brightness in range(30):
        s.send(get_set_color_command(brightness))
        time.sleep(.05)
    time.sleep(3)
    for brightness in range(29, -1, -1):
        s.send(get_set_color_command(brightness))
        time.sleep(.05)
    time.sleep(10)
