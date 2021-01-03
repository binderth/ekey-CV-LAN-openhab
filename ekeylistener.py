#!/usr/bin/python
/*
 * Version 0.1.0
 * By Thomas Binder
 * openHAB Community: https://community.openhab.org/u/binderth
*/

import datetime, sys, socket, json, os, re        # standard packages

# CONFIGURATION
# openHAB REST
OH_HOST = '192.168.178.10'   # the IP-address of your openHAB server
OH_PORT = '8080'            # the port of your openHAB server (default is 8080)
OH_EKEYITEM = 'ekey_JSON'   # the item in openHAB, you send the JSON to

# UDP
UDP_PORT = 51000            # the UDP port you configured in the configuration program of CV LAN (default is 51000)
PAYLOAD_DELIMITER = "_"     # the delimiter you configured in the configuration program of CV LAN (default is '_')
EKEY_ATTRIBUTES = ["packettype", "userid", "username", "userstatus", "fingerid", "keyid", "serialfs", "namefs", "action", "inputid", "timestamp"]

print "listening on port: " + str(UDP_PORT)

# creating UDP-Socket
sock = socket.socket(	socket.AF_INET, # Internet
			socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

# wait for socket data
while True:
    # receiving MULTI coded Ekey payload
    EKEY_MULTI, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    EKEY_MULTI = re.sub('[^\u0000-\u007f]', '',  EKEY_MULTI)

    # current timestamp
    TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # split payload into a list and add the current timestamp
    EKEY_VALUES = EKEY_MULTI.split("_")
    EKEY_VALUES.append(str(TIMESTAMP))
    EKEY_LIST = dict(zip(EKEY_ATTRIBUTES, EKEY_VALUES))

    # convert list into JSON (and remove all non-ASCII characters)
    EKEY_JSON = json.dumps(EKEY_LIST)
    print "JSON: ", EKEY_JSON

    # Take JSON and update item with openHAB REST
    UPDATE_URL = 'http://' + OH_HOST + ':' + OH_PORT + '/rest/items/' + OH_EKEYITEM
    CURL_STR = "curl -X POST --header 'Content-Type: text/plain' --header 'Accept: application/json' -d '" + EKEY_JSON + "' '" + UPDATE_URL + "'"
    os.system(CURL_STR)