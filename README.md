# ekey-CV-LAN-openhab
UDP listener for Ekey CV LAN, which uses openHAB REST API to upload the fingerprint response to openHAB
# ekey-UDP-openhab
an alternative way to import Ekey fingerprint to openHAB (openHAB2, openHAB3)
# prerequisites
* Ekey fingerprint sensor
* Ekey CV LAN 
* openHAB3 recommended, REST-calls also available with openHAB2 (http://openhab.org)

first of all, you have to configure your Ekey CV LAN via ekey_home_converter_LAN_config.exe (find it at https://www.ekey.net/downloadcenter/) to use your IP-addresses and be sure to configure the UDP-Calls like this:
* configure the UDP-port
* configure the IP-address of the recipient (the server you're running ekeylistener.py on!)
* configure the delimiter
* configure MULTI as protocol type
# how to use
After that, configure the variables in ekeylistener.py:
openHAB variables:
* OH_HOST = '192.168.xx.yy' // The IP-adress of your openHAB server
* OH_PORT = '8080' // The Port of your openHAB Server (default is 8080)
* OH_EKEYITEM = 'ekey_JSON' // The name of an openHAB item, which you want the JSON to update
CV LAN variables:
* UDP_PORT = 51000 // the UDP-port you chose in the above configuration programm (default is 51000)
* PAYLOAD_DELIMITER = "_" // the delimiter you chose in the configuration programm (default is "_")

after that, you're good to go, with the JSON of the fingerprint sensor in your item.

# notes
* This is for the REST API without any restrictions as introduced in openHAB3, perhaps later on, I'll update to allow for a credentials restricted API access.
* this comes "as is", no warranties
