from netmiko import ConnectHandler

router = [
    {"device_type": "cisco_ios", "host": "192.168.138.130", "username": "admin", "password": "cisco123"}, 
    {"device_type": "cisco_ios", "host": "192.168.138.135", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios", "host": "192.168.138.136", "username": "admin", "password": "cisco123"},
]


def main_menu():
    for ip in router:
        try:
            connection = ConnectHandler(**ip)
            print(f"The connection to the {ip['host']} is connected sucessfully")
            connection.disconnect()
        except Exception as e:
            print(f"There is a error in {ip}:{e}")

main_menu ()