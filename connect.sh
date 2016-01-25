#!/bin/sh
INTERFACE="wlan0"
wpa_cli -i $INTERFACE scan
wpa_cli -i $INTERFACE add_network
wpa_cli -i $INTERFACE set_network 0 ssid "LEDnet5F5CA6"
wpa_cli -i $INTERFACE set_network 0 key_mgmt NONE
wpa_cli -i $INTERFACE enable_network 0
