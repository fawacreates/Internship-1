# Week 3 Practice Files

This directory contains practice exercises for Week 3: Electronics + Embedded Systems

## Files

1. **arduino_led_blink.ino** - Hello World for Arduino
2. **imu_sensor_read.ino** - Read MPU6050 6-axis IMU
3. **gps_serial_read.ino** - Parse GPS NMEA data
4. **sensor_fusion_example.ino** - Combine multiple sensors
5. **i2c_scanner.ino** - Utility to find I2C devices

## Hardware Setup

### MPU6050 (6-axis IMU) Connections
```
MPU6050 → Arduino:
VCC    → 3.3V
GND    → GND
SDA    → A4 (SDA)
SCL    → A5 (SCL)
INT    → D2 (optional)
```

### NEO-6M GPS Module Connections
```
NEO-6M → Arduino:
VCC    → 5V
GND    → GND
TX     → RX (D0)
RX     → TX (D1) via level shifter
```

### BMP280 (Barometer) Connections
```
BMP280 → Arduino:
VCC    → 3.3V
GND    → GND
SDA    → A4 (SDA)
SCL    → A5 (SCL)
```

## Quick Start

1. Install Arduino IDE
2. Install required libraries:
   - MPU6050 library by InvenSense
   - TinyGPS++ library for GPS parsing
   - Adafruit BMP280 library
3. Upload sketches to Arduino board
4. Open Serial Monitor (9600 baud)

## Learning Progression

1. Start with `arduino_led_blink.ino` - verify upload works
2. Move to `i2c_scanner.ino` - verify sensor connections
3. Try individual sensor sketches
4. Combine into `sensor_fusion_example.ino`
