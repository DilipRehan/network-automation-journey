from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname= "192.168.138.130",
    username= "admin",
    password= "cisco123",
    optional_args={"secret":"cisco123"}
)

try:
    device.open()

    
    routes = device.get_route_to("10.10.10.0/24")
    print(routes)
    
    
    device.close()
except Exception as e:
    print(f"Something went wrong!")
    