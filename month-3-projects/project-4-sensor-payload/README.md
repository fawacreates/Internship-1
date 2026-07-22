# Project 4: Sensor Payload & Telemetry Board

## Target Companies
Bellatrix, Ignis, SatSure

## Project Overview
Design and build a modular sensor payload with LoRa telemetry transmission.

### Components
- ESP32 microcontroller
- BMP280 (barometer/altitude)
- MPU6050 (IMU - accel/gyro)
- NEO-6M (GPS)
- LoRa module (RFM95 or SX1278)
- Lithium battery + charger
- KiCad PCB design (optional)

### Key Features
- Multi-sensor fusion
- Real-time LoRa transmission
- Low power mode for balloon/drone deployment
- Data logging to SD card (optional)
- Web dashboard for live tracking

## Tech Stack
- Arduino/PlatformIO firmware
- KiCad (PCB design)
- Python (telemetry receiver)
- Streamlit (dashboard)
- LoRa long-range communication

## Directory Structure
```
project-4-sensor-payload/
├── hardware-design/
│   ├── kicad-schematic/
│   ├── gerber-files/
│   ├── BOM.csv
│   └── assembly_guide.md
├── firmware/
│   ├── sensor_drivers/
│   ├── lora_comm/
│   ├── power_management/
│   └── main.ino
├── ground-station/
│   ├── receiver.py
│   ├── dashboard.py
│   ├── data_logger.py
│   └── requirements.txt
├── data/
│   └── flight_data/
└── README.md
```

## Deliverables
1. Functional sensor payload
2. PCB design and gerber files
3. Firmware with telemetry
4. Ground station receiver
5. Live dashboard
6. GitHub repo with full documentation
7. Payload deployment video
