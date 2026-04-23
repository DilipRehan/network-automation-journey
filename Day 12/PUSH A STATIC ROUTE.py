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

command = ["ip route 10.10.10.0 255.255.255.0 192.168.138.1"]

output = connection.send_config_set(command)
print(output)


output1 = connection.send_command("show ip route static")

print(output1)
connection.disconnect()
print("Statis route pushed !")
