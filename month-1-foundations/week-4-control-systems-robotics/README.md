# Week 4: Control Systems + Intro to Robotics Software

## Topics

### 1. Control Systems Basics
**Resource:** [Brian Douglas - Control System Lectures (YouTube)](https://www.youtube.com/c/BrianBDouglas)
**Tools:** MATLAB/Octave, Python

**Learning Goals:**
- PID (Proportional-Integral-Derivative) controllers
- Feedback loops
- System stability
- Tuning parameters (Kp, Ki, Kd)

### 2. ROS2 Introduction
**Resource:** [ROS2 Official Tutorials](https://docs.ros.org/en/humble/Tutorials.html)
**Tools:** Ubuntu + ROS2 Humble

**Learning Goals:**
- ROS2 architecture (nodes, topics, services)
- Publishers and subscribers
- Launch files
- Why: Used across drones, rovers, and robotics systems

### 3. MAVLink Protocol
**Resource:** [MAVLink Docs](https://mavlink.io/en/)
**Tools:** pymavlink (Python)

**Learning Goals:**
- MAVLink message format
- Drone-to-ground station communication
- Telemetry and command protocols
- Directly relevant to: ideaForge, Asteria flight software

## Deliverables

### 1. PID Simulation in Python
- [ ] Virtual pendulum balancing controller
- [ ] OR Drone altitude hold simulator
- [ ] Tune Kp, Ki, Kd parameters
- [ ] Plot response curves

### 2. ROS2 Publisher/Subscriber Node
- [ ] Create a simple publisher (e.g., sensor data)
- [ ] Create a subscriber (e.g., logs data)
- [ ] Test communication between nodes
- [ ] Launch from launch file

## Practice Files Location
See `../../practice-files/week-4/` for PID controller implementations and ROS2 boilerplate.
