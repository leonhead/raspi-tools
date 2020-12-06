import bluetooth
import time
import threading
import requests

class BluetoothService:

    def __init__(self):
        self.found_devs = {'addr':'name'}

    def find_devs(self):
        print("starting discover devices")
        devices = bluetooth.discover_devices(lookup_names=True)
        print(devices)
        for (addr,name) in devices:
            if (addr,) not in self.found_devs:
                print("found new device: %s - %s" % (addr, name))
                self.found_devs.update({addr:name})
                #requests.post("http://", data = {'key':'value'})
                self.find_services(addr)

    def find_services(self, addr):
        print("start service discovery for addr: %s" % (addr))
        services = bluetooth.find_service(address=addr)
        print(services)