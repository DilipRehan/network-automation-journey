from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
}

connection = ConnectHandler(**router)
connection.enable()

output = connection.send_command("show ip interface brief", use_textfsm=True)

for route in output:
    print(f" {route['interface']} {route['ip_address']}")

connection.disconnect()