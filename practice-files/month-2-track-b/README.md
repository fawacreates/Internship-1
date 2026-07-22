# Month 2 Track B: Drone Autonomy & Flight Software

Practice files for autonomous flight and embedded systems specialization.

## Directory Structure

```
month-2-track-b/
├── 01_flight_controller/
│   ├── px4_setup.md
│   ├── pixhawk_parameters.txt
│   └── custom_firmware.cpp
├── 02_simulation/
│   ├── gazebo_world.launch
│   ├── px4_sitl_start.sh
│   └── drone_model.sdf
├── 03_path_planning/
│   ├── a_star.py
│   ├── rrt.py
│   └── potential_fields.py
├── 04_state_estimation/
│   ├── kalman_filter.py
│   ├── extended_kalman_filter.py
│   └── sensor_fusion.py
└── 05_ros2_nodes/
    ├── flight_controller_node.py
    ├── telemetry_publisher.py
    └── command_subscriber.py
```

## Resources

- ArduPilot: https://ardupilot.org/
- PX4: https://px4.io/
- Gazebo: http://gazebosim.org/
- ROS2: https://docs.ros.org/
- Python Robotics: https://github.com/AtsushiSakai/PythonRobotics

## Getting Started

### Install Tools
```bash
# Install ROS2 Humble
sudo apt update && sudo apt install ros-humble-desktop

# Install Gazebo
sudo apt install gazebo

# Install PX4
git clone https://github.com/PX4/PX4-Autopilot.git
cd PX4-Autopilot
bash ./Tools/setup/ubuntu.sh

# Install Python packages
pip install numpy scipy matplotlib
pip install pymavlink
```

### Run Simulations
```bash
# Start PX4 SITL with Gazebo
cd PX4-Autopilot
make px4_sitl gazebo

# In another terminal, run control script
python3 control_drone.py
```

## Practice Path

1. **Week 5:** Flight Controller Basics
   - [ ] Understand ArduPilot/PX4 architecture
   - [ ] Review flight modes (Manual, Stabilize, Altitude Hold, Loiter)
   - [ ] Study autopilot state machine
   - [ ] Configure basic parameters

2. **Week 5-6:** Simulation Setup
   - [ ] Install Gazebo and ROS2
   - [ ] Get PX4 SITL running
   - [ ] Spawn drone in virtual world
   - [ ] Test arm/disarm/takeoff commands

3. **Week 6:** Path Planning
   - [ ] Implement A* algorithm
   - [ ] Implement RRT
   - [ ] Test on 2D grid
   - [ ] Extend to 3D space

4. **Week 7:** State Estimation
   - [ ] Study Kalman Filter theory
   - [ ] Implement basic KF
   - [ ] Extend to EKF
   - [ ] Fuse IMU + GPS sensors

5. **Week 8:** Ground Station & Integration
   - [ ] Set up QGroundControl
   - [ ] Parse MAVLink telemetry
   - [ ] Build custom dashboard
   - [ ] Execute autonomous missions
