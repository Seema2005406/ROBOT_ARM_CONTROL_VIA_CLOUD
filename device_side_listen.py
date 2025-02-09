import time
import serial
import os
from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.common.transport_exceptions import ConnectionDroppedError

# Serial Port Configuration
s = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

# Azure IoT Hub Connection String (Replace with your actual key)
CONNECTION_STRING = os.getenv("IOTHUB_STRING")

# Function to create an IoT Hub Client with auto-reconnect

# Function to handle received commands
def command_callback(message):
    try:
        command = message.data.decode("utf-8")
        print(f"📩 Received command: {command}")

        # Control the robotic arm based on the command
        if command == 'AU':  # Arm UP
            s.write(b'AU\n')
            print("⬆️ Moving arm up...")
        elif command == 'AD':  # Arm DOWN
            s.write(b'AD\n')
            print("⬇️ Moving arm down...")
        elif command == 'AC':  # Arm CLOSE
            s.write(b'AC\n')
            print("✊ Closing arm...")
        elif command == 'AO':  # Arm OPEN
            s.write(b'AO\n')
            print("🖐️ Opening arm...")
        elif command.startswith('R'):  # Rotate
            angle = command[1:]
            s.write(f'R{angle}\n'.encode())
            print(f"🔄 Rotating arm by {angle} degrees...")
        elif command == 'G':  # Get Status
            s.write(b'G\n')
            print("📡 Getting status...")
# Reading Data
            byte = s.read().decode()
            stri = ""
            while(byte != '\n'):
                stri = stri + byte
                byte = s.read().decode('ascii')

# Parsing the Recieved Data
            stri = stri.split()
            print(stri)

    except Exception as e:
        print(f"❌ Error processing command: {e}")

# Set the callback function to handle messages
def listen_for_commands():
    try:
        device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        device_client.on_message_received = command_callback
        print("Waiting for commands from Azure IoT Hub...")

        device_client.connect()
        while True:
            pass  # Keep listening for messages
    except KeyboardInterrupt:
        print("Stopping device client")
    finally:
        device_client.shutdown()

# Example Usage
listen_for_commands()
