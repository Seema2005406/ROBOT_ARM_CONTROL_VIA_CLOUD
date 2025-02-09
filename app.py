from flask import Flask, render_template, request, jsonify
from azure.iot.device import IoTHubDeviceClient
from azure.iot.hub import IoTHubRegistryManager
import time
import os

app = Flask(__name__)

# Azure IoT Hub Connection String
CONNECTION_STRING = os.getenv("IOTHUB_CONNECTION_STRING")
DEVICE_ID = "robotic-arm"
# Function to create an IoT Hub Clientztho
# Function to send command to Azure IoT Hub
def send_command_to_azure(command):
    global client
    try:
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)
        registry_manager.send_c2d_message(DEVICE_ID, command)
        print(f"Command sent to device {DEVICE_ID}: {command}")
    except Exception as e:
        print(f"Failed to send command: {str(e)}")

# Route to serve the HTML interface
@app.route('/')
def index():
    return render_template('index.html')

# Route to send commands (toggle)
@app.route('/toggle', methods=['POST'])
def toggle_arm():
    try:
        data = request.json
        action = data.get('action')

        if action not in ['AU', 'AD', 'AC', 'AO']:
            return jsonify({"status": "error", "message": "Invalid command"}), 400

        send_command_to_azure(action)
        return jsonify({"status": "success", "command": action})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to rotate the robotic arm
@app.route('/rotate', methods=['POST'])
def rotate_arm():
    try:
        data = request.json
        angle = data.get('angle')

        if not str(angle).isdigit():
            return jsonify({"status": "error", "message": "Invalid angle"}), 400

        send_command_to_azure(f"R{angle}")
        return jsonify({"status": "success", "command": f"R{angle}"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to get the status of the robotic arm
@app.route('/get_status', methods=['GET'])
def get_status():
    try:
        send_command_to_azure("G")
        return jsonify({"status": "success", "command": "G"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
