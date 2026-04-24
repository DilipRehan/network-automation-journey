from napalm import get_network_driver

driver = get_network_driver("ios")


device = driver(
    hostname = "192.168.138.130",
    username = "admin",
    password = "cisco123",
    optional_args={"secret":"cisco123"}
)


try:
    device.open()
    interfaces = device.get_interfaces()

    print("=" * 45)
    print("INTERFACE STATUS")
    print("="* 45)
    
    for name,details,in interfaces.items():
        status = "UP" if details["is_up"] else "DOWN !"
        print(f"{name:20} {status}")
       
    device.close()


except Exception as e:
    print(f"Something went wrong!")
