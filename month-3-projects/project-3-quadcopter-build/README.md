# Project 3: Build & Fly a Custom Quadcopter

**Target:** ideaForge, Asteria (hardware experience valued)

## Objective
Assemble, configure, and fly a real quadcopter with GPS waypoint missions and telemetry logging.

## Bill of Materials (₹15,000-25,000)

### Frame & Motors
- [ ] 450-500mm quadcopter frame kit: ₹2,500-4,000
- [ ] 4x Brushless motors (900-1100 KV): ₹2,000-3,000
- [ ] 4x ESCs (40-50A): ₹1,500-2,000
- [ ] Propellers (10", 11") + extras: ₹500-1,000

### Flight Controller & Sensors
- [ ] Pixhawk 4 or ArduPilot Mega + 2.8: ₹4,000-6,000
- [ ] GPS Module (NEO-6M/F9P): ₹800-2,000
- [ ] Power Distribution Board (PDB): ₹500-800
- [ ] Telemetry Radio (SiK/915MHz): ₹1,500-2,500

### Power
- [ ] 4S LiPo Battery (3000-5000 mAh): ₹2,000-3,000
- [ ] Battery Charger (balance charger): ₹800-1,200
- [ ] Voltage Regulator (BEC): ₹200-400

### Optional
- [ ] Servo for camera gimbal
- [ ] HD camera (GoPro, Runcam)
- [ ] FPV goggles (if doing FPV flights)

## Assembly Steps

### Phase 1: Frame & Mechanics
- [ ] Assemble frame
- [ ] Mount motors to arms
- [ ] Attach ESCs
- [ ] Wire power distribution

### Phase 2: Electronics Integration
- [ ] Mount Pixhawk/flight controller
- [ ] Connect sensors (GPS, compass, barometer)
- [ ] Wire telemetry radio
- [ ] Connect battery connector

### Phase 3: Configuration & Calibration
- [ ] Flash latest ArduPilot firmware
- [ ] Calibrate compass
- [ ] Calibrate accelerometer
- [ ] Calibrate ESCs
- [ ] Calibrate radio receiver
- [ ] Set up failsafes

### Phase 4: Ground Testing
- [ ] Bench test (props off): throttle response
- [ ] Verify all sensors read correctly
- [ ] Check GPS lock
- [ ] Test telemetry link
- [ ] Validate compass heading

### Phase 5: First Flight
- [ ] Clear flight area (open field, 50m+ radius)
- [ ] Start with stabilize mode
- [ ] Manual control to ~1-2m altitude
- [ ] Switch to altitude hold
- [ ] Return to manual, land

### Phase 6: Advanced Flights
- [ ] Test loiter mode (GPS hold)
- [ ] Fly simple waypoint mission (3-4 points)
- [ ] Monitor telemetry during flight
- [ ] Log flight data
- [ ] Analyze and debug

## Deliverables
- [ ] Photos of assembled quad
- [ ] Setup checklist (for repeatability)
- [ ] Flight logs (bin files)
- [ ] Video of flight (manual + autonomous)
- [ ] GitHub repo with:
  - Parameter configuration file
  - Calibration notes
  - Troubleshooting guide
  - Flight log analysis

## Tips
- **Cost sharing:** Partner with college drone/robotics club
- **Safety first:** Always fly in open areas, away from people/property
- **Incremental:** Start with manual flights before autonomous missions
- **Logging:** Always enable dataflash logging for post-flight analysis
- **Documentation:** Photo/video each assembly step for your portfolio

## Safety Checklist Pre-Flight
- [ ] Propellers secure and balanced
- [ ] Battery fully charged
- [ ] Failsafe configured
- [ ] GPS locked (if using GPS)
- [ ] Radio calibrated
- [ ] Compass validated
- [ ] ESC calibration done
- [ ] No loose wires
- [ ] Clear airspace
