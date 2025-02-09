# 🤖 Remote Robotic Arm Control via Azure IoT Hub

This project enables remote control of a robotic arm using **Azure IoT Hub** and a **Flask Web Interface**. The system listens for commands from the cloud and sends them to the robotic arm via **serial communication**. Users can control the arm through a web interface, allowing movements like **up, down, open, close, and rotation**.

## 🚀 Features
- 🔗 **Azure IoT Hub Integration**: Secure cloud-based command transmission.
- 🌐 **Flask Web Interface**: Easy-to-use web dashboard for sending commands.
- 🖥️ **Serial Communication**: Direct control over the robotic arm.
- 📡 **Real-time Status Monitoring**: Request and view the arm’s current position.
- 🔄 **Rotation Support**: Specify angles for precise movements.

## 🛠️ Setup & Installation
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/robotic-arm-control.git
cd robotic-arm-control
```

### 2️⃣ **Set Up Environment Variables**
Since the IoT Hub connection string is sensitive, store it securely as an environment variable instead of hardcoding it.

#### 🔹 **On Windows (Command Prompt)**
```cmd
set IOTHUB_CONNECTION_STRING="your-iot-hub-connection-string"
```

#### 🔹 **On macOS/Linux (Terminal)**
```bash
export IOTHUB_CONNECTION_STRING="your-iot-hub-connection-string"
```
For github you can add it as repo Secrets

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App**
```bash
python app.py
```

### 5️⃣ **Start the Device Listener** (On the Robot's Device)
```bash
python device_side_listen.py
```

## 📡 How It Works
1. **Web Interface:** Users interact with a Flask-based web dashboard.
2. **Azure IoT Hub:** The Flask app sends commands to Azure IoT Hub.
3. **Device Listener:** The robotic arm listens for commands and executes movements.
4. **Serial Communication:** The arm receives commands via serial port (USB/COM).
5. **Real-time Feedback:** The robot arm can send status updates back to Azure.

## 🌍 Web API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | `GET` | Loads the web interface |
| `/toggle` | `POST` | Moves arm: `AU` (Up), `AD` (Down), `AC` (Close), `AO` (Open) |
| `/rotate` | `POST` | Rotates the arm (`R{angle}`) |
| `/get_status` | `GET` | Requests current status of the arm |

## 🛠️ Supported Commands
| Command | Description |
|---------|------------|
| `AU` | Move arm UP |
| `AD` | Move arm DOWN |
| `AC` | Close gripper |
| `AO` | Open gripper |
| `R{angle}` | Rotate by specified angle |
| `G` | Get current status |

## 🔗 Resources
- [Azure IoT Hub Documentation](https://docs.microsoft.com/en-us/azure/iot-hub/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)

## ⚠️ Security Considerations
- **DO NOT** hardcode your IoT Hub credentials in the code.
- Use **GitHub Secrets** or **Environment Variables** for sensitive data.

## ✨ Contribution
Feel free to fork this repo and submit a pull request if you have improvements!

## 📜 License
This project is licensed under the GPL V3 License.

---
💡 **Now you can remotely control your robotic arm with Azure IoT and a web interface!** 🤖🎮

