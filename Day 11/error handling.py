def connect_device(ip,username, password):
    try:
        if ip == "":
            raise ValueError("IP address cannot be empty")
        if username == "":
            raise ValueError("Username cannot be empty")
        
        print(f"Connecting to {ip}")
        print(f"Connected sucessfully")

    except ValueError as e:
        print(f"Invalid input: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")



connect_device ("192.168.1.1","admin","cisco123")


connect_device("","admin","cisco123")

connect_device("192.168.1.1","","cisco123")