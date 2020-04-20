import ipaddress
import json


def validate_ip(ip):
    try:
        if ipaddress.ip_address(ip):
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    with open('JSONdata') as f:
        data = json.loads(f.read())

        for device in data:
            ip_address = device['lanIp']
            serial_number = device['serial']
            if validate_ip(ip_address):
                print(f"{ip_address} is a Valid IP Address for Serial #{serial_number}")
            else:
                print(f"{ip_address} is not a Valid IP Address for Serial #{serial_number}")
