# Month 2 Track B: Drone Autonomy & Embedded Flight Software

## Target Companies
ideaForge, Asteria, Sarla, Bellatrix

## Learning Path (Weeks 5-8)

### Week 5: Flight Controller Firmware
- ArduPilot or PX4 architecture
- Firmware customization basics
- Flight modes and stabilization
- **Resources:** [ArduPilot dev docs](https://ardupilot.org/dev/) or [PX4 docs](https://docs.px4.io/)

### Weeks 5-6: Simulation (Gazebo + ROS2)
- PX4 SITL setup
- Drone simulation in Gazebo
- ROS2 integration
- **Resources:** [PX4 Gazebo SITL](https://docs.px4.io/main/en/simulation/gazebo.html)

### Week 6: Path Planning & Obstacle Avoidance
- Waypoint navigation
- RRT and A* algorithms
- Collision avoidance
- **Resources:** [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics)

### Week 7: State Estimation
- Kalman Filter fundamentals
- Extended Kalman Filter (EKF)
- Sensor fusion
- **Resources:** [Kalman Filter for Beginners](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT)

### Week 8: Ground Control Station & Telemetry
- QGroundControl usage
- MAVLink protocol mastery
- Telemetry dashboard development
- **Tools:** QGroundControl, pymavlink, Python

## Deliverable
Simulated drone completing waypoint mission with obstacle avoidance and live telemetry

## Directory Structure
```
track-b-drone-autonomy/
├── flight-controller-firmware/
├── gazebo-simulation/
├── path-planning/
│   ├── rrt/
│   ├── astar/
│   └── obstacle-avoidance/
├── kalman-filter/
└── ground-station/
```
