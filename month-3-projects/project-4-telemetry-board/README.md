# Project 4: Sensor Payload / Telemetry Board

**Target:** Bellatrix (propulsion telemetry), Ignis Aerospace, small-sat companies

## Objective
Design, build, and test a telemetry payload that logs and transmits sensor data in real-time (mimics CubeSat/rocket telemetry).

## Components

### Microcontroller
- [ ] ESP32-DevKit (WiFi + Bluetooth + LoRa): ₹400-600
  OR
- [ ] Arduino Mega + LoRa shield: ₹500-800

### Sensors
- [ ] BMP280 (barometer/thermometer): ₹200-300
- [ ] MPU6050 (6-axis IMU): ₹150-250
- [ ] NEO-6M GPS module: ₹300-400
- [ ] Wiring + breakout boards: ₹200-300

### Communication
- [ ] RFM95W LoRa module (900MHz): ₹400-600
- [ ] SX1278 LoRa breakout: ₹300-500
- [ ] Antenna (470-510MHz dipole): ₹100-200

### Enclosure & Mechanical
- [ ] 3D-printed enclosure: ₹500-1,000 (or simple plastic box)
- [ ] Standoffs, screws, connectors: ₹200-300

### Power
- [ ] 3.7V LiPo battery: ₹200-300
- [ ] Battery charging module: ₹100-150

**Total:** ₹3,500-5,500

## Design & Architecture

### Hardware Block Diagram
```
┌──────────────┐
│   ESP32      │
│              │
├──────┬───────┤
│      │       │
│   I2C Bus    │
│      │       │
├──────┼─────┬─┤
│ BMP280  │MPU  │
alt/temp│ IMU │
│      │       │
└──────────────┘
      │   │
      └───┼─────┬─────────────┐
          │     │             │
       UART   SPI (LoRa)   UART (GPS)
          │     │             │
     [Future] [RFM95W]     [NEO-6M]
        Display   LoRa         GPS
```

### Firmware Architecture
```
main loop:
  - Read sensors (I2C: BMP280, MPU6050)
  - Read GPS (UART: NEO-6M)
  - Apply sensor fusion (Kalman filter for altitude)
  - Transmit via LoRa (SPI)
  - Log to SPIFFS (onboard storage)
  - Sleep to conserve power
```

## Build Phases

### Phase 1: Sensor Integration
- [ ] Wire BMP280 (I2C)
  - SDA → GPIO 21
  - SCL → GPIO 22
  - VCC → 3.3V, GND → GND
- [ ] Wire MPU6050 (I2C, same bus)
- [ ] Wire NEO-6M GPS (UART)
  - RX → GPIO 16
  - TX → GPIO 17
- [ ] Write individual sensor drivers
- [ ] Test each sensor independently

### Phase 2: LoRa Module Integration
- [ ] Wire RFM95W (SPI)
  - NSS → GPIO 5
  - MOSI → GPIO 23
  - MISO → GPIO 19
  - SCK → GPIO 18
  - RST → GPIO 14
  - DIO0 → GPIO 26
- [ ] Install LoRa library (RadioHead or LMIC)
- [ ] Transmit test packets
- [ ] Verify range (start indoors, move outdoors)

### Phase 3: Firmware Development
- [ ] Initialize all sensors
- [ ] Create data struct for telemetry packet
- [ ] Implement main sensor reading loop (100 Hz IMU, 1 Hz GPS/Baro)
- [ ] Apply Kalman filter for altitude estimation
- [ ] Encode packet + transmit via LoRa
- [ ] Add SD card logging (optional, on future SD shield)
- [ ] Implement low-power sleep modes

### Phase 4: Ground Receiver
- [ ] Build simple LoRa receiver (Arduino + RFM95W or SDR)
- [ ] Decode incoming packets
- [ ] Display on serial monitor
- [ ] Log to CSV file
- [ ] (Optional) Real-time Python dashboard

### Phase 5: Enclosure & Testing
- [ ] Design 3D-printable box (or use plastic enclosure)
- [ ] Mount all components inside
- [ ] Add antenna connector
- [ ] Seal waterproofing (optional, for balloon/drop test)
- [ ] Field test: balloon, drone, or drop test
- [ ] Validate data transmission and logging

## Deliverables
- [ ] Assembled and tested telemetry board
- [ ] Firmware source code (GitHub)
- [ ] Ground station receiver code
- [ ] Schematic (hand-drawn or KiCad)
- [ ] PCB gerber files (bonus: if using custom PCB)
- [ ] Field test video/photos
- [ ] Flight data logs and analysis
- [ ] README with:
  - Build instructions
  - Pinout diagram
  - Calibration procedure
  - Test results
  - Future improvements

## Advanced: Custom PCB
(Optional, for extra points at companies)
- Use KiCad to design PCB
- Order from JLCPCB (cheap, fast)
- Solder components
- Test and iterate

## Why This Matters
- **Real hardware:** Not just simulation
- **End-to-end:** Sensor → transmission → ground station
- **Scaled version:** Mimics CubeSat/rocket payloads
- **Portfolio proof:** Shows electrical + firmware + systems skills
