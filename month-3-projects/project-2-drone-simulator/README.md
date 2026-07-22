# Project 2: Autonomous Drone Mission Simulator

## Target Companies
ideaForge, Asteria, Sarla

## Project Overview
Simulate a fully autonomous drone completing survey missions with obstacle avoidance.

### Key Features
- PX4 SITL simulation in Gazebo
- Waypoint mission planning and execution
- Real-time obstacle avoidance (RRT-based)
- Kalman filter state estimation
- Python ground control station with telemetry
- Flight logs and analytics dashboard

### Tech Stack
- ROS2, Gazebo, PX4 SITL
- Python, pymavlink
- MAVLink protocol
- Flask/Streamlit (visualization)
- Docker (for reproducibility)

## Directory Structure
```
project-2-drone-simulator/
├── src/
│   ├── gcs.py (Ground Control Station)
│   ├── planner.py (Path planning)
│   ├── estimator.py (Kalman filter)
│   └── telemetry.py
├── simulation/
│   ├── models/
│   ├── worlds/
│   └── launch/
├── ros2-nodes/
│   ├── offboard_control/
│   ├── obstacle_detector/
│   └── telemetry_logger/
├── notebooks/
│   └── analysis.ipynb
├── Dockerfile
├── requirements.txt
└── README.md
```

## Deliverables
1. Simulated drone completing 10+ waypoint mission
2. Real-time telemetry dashboard
3. Obstacle avoidance demonstration
4. ROS2 nodes (reusable for real hardware)
5. GitHub repo with Docker setup
6. Demo video (5 minutes)
