from netmiko import ConnectHandler

router = {
    "device_type":"cisco_ios",
    "host":"192.168.138.130",
    "username":"admin",
    "password":"cisco123",
    "secret": "cisco123",
}

connection = ConnectHandler(**router)
connection.enable()

output = connection.send_config_set(["hostname R1-Updated"])

print(output)
connection.disconnect()
