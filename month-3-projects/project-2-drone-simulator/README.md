# Project 2: Autonomous Drone Mission Simulator

**Target:** ideaForge, Asteria, Sarla Aviation

## Objective
Build a complete autonomous drone simulator with waypoint navigation, obstacle avoidance, state estimation, and ground station.

## Architecture

```
┌─────────────────────────────────────────┐
│  Gazebo Physics Engine + PX4 SITL       │
│  (Virtual Drone in 3D Environment)      │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────┴──────────┐
        ↓                     ↓
  ROS2 Nodes          State Estimator
  - Flight Ctrl      (Kalman Filter)
  - Sensor Sim       - Position
  - Telemetry        - Velocity
  - Comms            - Orientation
        │                     │
        └──────────┬──────────┘
                   ↓
         Ground Station (Python)
         - MAVLink Handler
         - Telemetry Dashboard
         - Mission Planner
         - Live Monitoring
```

## Tech Stack
- **Simulation:** Gazebo + PX4 SITL
- **Middleware:** ROS2 Humble
- **Flight Control:** PX4 Autopilot
- **Ground Station:** Python + PyMAVLink
- **State Estimation:** Kalman Filter (custom Python)
- **Dashboard:** Matplotlib/Plotly real-time plots
- **Version Control:** Git/GitHub

## Milestones

### Phase 1: Environment Setup
- [ ] Install Gazebo + PX4 SITL
- [ ] Install ROS2 Humble
- [ ] Verify simulation runs
- [ ] Test basic drone spawning

### Phase 2: ROS2 Integration
- [ ] Create ROS2 workspace
- [ ] Define message types (sensor data, commands)
- [ ] Build flight controller node
- [ ] Build telemetry publisher
- [ ] Implement sensor simulation (GPS, IMU, barometer)

### Phase 3: State Estimation
- [ ] Implement Extended Kalman Filter (EKF)
- [ ] Fuse IMU + GPS data
- [ ] Estimate position, velocity, orientation
- [ ] Publish state estimates via ROS2

### Phase 4: Autonomous Mission
- [ ] Implement waypoint navigation
- [ ] Add simple obstacle avoidance (LiDAR sim)
- [ ] PID controller for trajectory tracking
- [ ] Takeoff/land maneuvers

### Phase 5: Ground Station
- [ ] Implement MAVLink receiver
- [ ] Build telemetry parser
- [ ] Real-time plotting (altitude, position, speed)
- [ ] Mission upload/monitoring interface
- [ ] Emergency stop command

### Phase 6: Testing & Documentation
- [ ] Run complete mission scenario
- [ ] Log flight data
- [ ] Generate plots and videos
- [ ] Write comprehensive README
- [ ] Create setup instructions

## Expected Outcomes
- [ ] Drone autonomously flies waypoint mission
- [ ] Avoids simulated obstacles
- [ ] State estimation error < 0.5m
- [ ] Ground station displays live telemetry
- [ ] Full mission logged and visualized
- [ ] Clean GitHub repo with instructions

## Files in This Directory
- `ros2_ws/` - ROS2 workspace with all packages
- `src/` - Python flight control code
- `config/` - Gazebo world files, PX4 configs
- `missions/` - Mission definition files
- `logs/` - Flight data logs and results
- `scripts/` - Ground station and utilities
