


class BluetoothDevice:
    
    
    def __init__(self, name="Unknown Device", mac_address=None):
        self.name = name
        self.mac_address = mac_address
        self.is_paired = False
        self.is_connected = False
        self.battery_level = 100

    def pair(self, device_mac_address):
        if not self.is_paired:
            self.mac_address = device_mac_address
            self.is_paired = True
            return f"{self.name} paired with device {device_mac_address}."
        return f"{self.name} is already paired with {self.mac_address}."

    def unpair(self):
        if self.is_paired:
            result = f"{self.name} unpaired from device {self.mac_address}."
            self.is_paired = False
            self.mac_address = None
            self.is_connected = False
            return result
        return f"{self.name} is not paired with any device."

    def connect(self):
        if self.is_paired and not self.is_connected:
            self.is_connected = True
            return f"{self.name} connected to {self.mac_address}."
        if not self.is_paired:
            return f"{self.name} is not paired with any device."
        return f"{self.name} is already connected to {self.mac_address}."

    def disconnect(self):
        if self.is_connected:
            result = f"{self.name} disconnected from {self.mac_address}."
            self.is_connected = False
            return result
        return f"{self.name} is not connected to any device."

    def send_data(self, data):
        if self.is_connected:
            return f"Sending data to {self.mac_address}: {data}"
        return f"{self.name} is not connected. Cannot send data."

    def receive_data(self):
        if self.is_connected:
            data = "Sample received data"
            return f"Data received from {self.mac_address}: {data}"
        return f"{self.name} is not connected. Cannot receive data."

    def get_battery_level(self):
        return f"{self.name} battery level: {self.battery_level}%"

    def rename_device(self, new_name):
        old_name = self.name
        self.name = new_name
        return f"Device renamed from '{old_name}' to '{self.name}'"
