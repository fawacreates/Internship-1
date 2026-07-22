# Week 4 Practice Files

This directory contains practice exercises for Week 4: Control Systems + Robotics

## Files

1. **pid_controller.py** - Implementation of PID controller
2. **pid_simulator.py** - Simulate PID on virtual pendulum/drone
3. **ros2_publisher.py** - ROS2 publisher node example
4. **ros2_subscriber.py** - ROS2 subscriber node example
5. **mavlink_example.py** - Basic MAVLink communication

## Understanding PID

### PID Equation
```
output = Kp*error + Ki*∫error*dt + Kd*d(error)/dt

Where:
- Kp (Proportional): Direct response to error
- Ki (Integral): Accumulated error correction
- Kd (Derivative): Rate of change dampening
```

### Tuning Guidelines
- Increase Kp: Faster response, but may oscillate
- Increase Ki: Removes steady-state error
- Increase Kd: Reduces overshoot

## Quick Start

### Run PID Simulation
```bash
python3 pid_simulator.py
```

### Set Up ROS2 Workspace
```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_ws
colcon build
```

### Run ROS2 Example
```bash
ros2 run my_package publisher_node
# In another terminal:
ros2 run my_package subscriber_node
```

## Learning Path

1. Study `pid_controller.py` - understand the algorithm
2. Run `pid_simulator.py` - see PID in action
3. Experiment with tuning parameters
4. Install ROS2 and run publisher/subscriber examples
5. Explore MAVLink for drone communication
