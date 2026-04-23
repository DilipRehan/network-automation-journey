from netmiko import ConnectHandler

router = {
    "device_type":"cisco_ios",
    "host":"192.168.138.130",
    "username":"admin",
    "password":"cisco123",
    "secret":"cisco123",
}

connection = ConnectHandler(**router)
connection.enable()

commands = [
    "hostname R1",
    "ip domain-name lab.local",
    "ntp server 8.8.8.8",
]

output = connection.send_config_set(commands)
print(output)

connection.disconnect()