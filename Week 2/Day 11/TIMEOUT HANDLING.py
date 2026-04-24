from netmiko import ConnectHandler
from datetime import datetime
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException


def connect_device(ip, username, password, secret):
    try:
        router = {
            "device_type":"cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
            "secret": secret,
            "timeout": 5,
        }

        connection = ConnectHandler(**router)
        connection.enable()
        print(f"{ip} - Connected Sucessfully")
        connection.disconnect()

    except NetmikoTimeoutException:
        print(f"! {ip} - Device unreachable (timeout)")

    except NetmikoAuthenticationException:
        print(f"{ip} -  Wroing username or password")

    except Exception as e:
        print(f"! {ip} -  Failed : {e}")


connect_device("192.168.138.130", "admin","cisco123","cisco123")

connect_device("192.168.138.99", "admin","cisco123","cisco123")

connect_device("192.168.138.130", "admin","wrongpass","cisco123")