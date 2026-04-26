from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname = "192.168.138.130",
    username = "admin",
    password = "cisco123",
    optional_args={"secret":"cisco123"}
)


device.open()

bgp = device.get_bgp_neighbors()
print(bgp)

device.close()