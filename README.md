# Internship Learning Journey 

My daily efforts to land an internship by learning everything from scratch!

## About This Repository

This repository documents my **3-month structured learning plan** to break into aerospace companies as a **BCA student**. The focus is on **software** — computer vision, satellite data processing, drone autonomy, embedded systems, and GNC (Guidance-Navigation-Control) — areas where I can compete effectively against Mechanical/Aerospace graduates.

**Target Companies:** Bellatrix Aerospace, Pixxel, Asteria Aerospace, ideaForge, SatSure, Sarla Aviation, Ignis Aerospace.

---

## The Strategy

As a BCA student, my competitive edge is **software engineering**, not structures or propulsion math. This plan builds:
- **Computer vision & satellite data pipelines** (Pixxel, SatSure, ideaForge, Asteria)
- **Drone autonomy & embedded flight software** (ideaForge, Asteria, Sarla, Bellatrix)
- **Real hardware & software projects** for portfolio
- **Practical hands-on experience** that interns from competing backgrounds don't have

---

## 3-Month Roadmap Overview

```
MONTH 1: Foundations (4 weeks)
├── Week 1: Programming Core + Math Refresh
├── Week 2: Linux, Command Line & Aerospace Fundamentals
├── Week 3: Electronics + Embedded Systems Intro
└── Week 4: Control Systems + Intro to Robotics Software

MONTH 2: Deep Specialization (4 weeks)
├── TRACK A: Computer Vision & Satellite Data
│   └── Deep learning, remote sensing, geospatial processing
└── TRACK B: Drone Autonomy & Embedded Flight Software
    └── Flight controllers, simulation, path planning, state estimation

MONTH 3: High-Value Projects + Portfolio (4 weeks)
├── Software Project 1: Satellite Image Analysis Pipeline
├── Software Project 2: Autonomous Drone Mission Simulator
├── Hardware Project 1: Build & Fly a Custom Quadcopter
├── Hardware Project 2: Sensor Payload / Telemetry Board
└── Portfolio + Cold Outreach to Companies
```

**Daily Commitment:** 3–4 hours/day across all 12 weeks

---

## Repository Structure

```
Internship-1/
│
├── README.md (this file)
│
├── month-1-foundations/
│   ├── week-1-programming-math/
│   │   ├── python-basics/
│   │   ├── cpp-fundamentals/
│   │   ├── linear-algebra/
│   │   └── learning-notes.md
│   ├── week-2-linux-aerospace/
│   │   ├── bash-scripts/
│   │   ├── aerospace-fundamentals/
│   │   └── coordinate-frames.md
│   ├── week-3-electronics-embedded/
│   │   ├── arduino-projects/
│   │   ├── sensor-datasheets/
│   │   └── serial-communication/
│   └── week-4-control-systems/
│       ├── pid-simulation.py
│       ├── ros2-basics/
│       └── mavlink-protocol/
│
├── month-2-specialization/
│   ├── track-a-computer-vision/
│   │   ├── opencv-tutorials/
│   │   ├── deep-learning-models/
│   │   ├── satellite-imagery/
│   │   └── projects/
│   └── track-b-drone-autonomy/
│       ├── flight-controller-firmware/
│       ├── gazebo-simulation/
│       ├── path-planning/
│       └── kalman-filter/
│
├── month-3-projects/
│   ├── project-1-satellite-pipeline/
│   │   ├── src/
│   │   ├── models/
│   │   ├── data/
│   │   ├── streamlit_app.py
│   │   └── README.md
│   ├── project-2-drone-simulator/
│   │   ├── src/
│   │   ├── simulation/
│   │   ├── ros2-nodes/
│   │   └── README.md
│   ├── project-3-quadcopter/
│   │   ├── assembly-guide/
│   │   ├── firmware-config/
│   │   ├── flight-logs/
│   │   └── README.md
│   └── project-4-sensor-payload/
│       ├── hardware-design/
│       ├── firmware/
│       ├── ground-station/
│       └── README.md
│
├── learning-log/
│   ├── week-1.md
│   ├── week-2.md
│   └── ... (weekly progress notes)
│
├── resources/
│   ├── reading-list.md
│   ├── tool-stack-reference.md
│   ├── companies-research.md
│   └── interview-prep.md
│
└── portfolio/
    ├── resume.md
    ├── project-videos/
    └── github-showcases/
```

---

## 📖 Detailed Month-by-Month Plan

### **MONTH 1 — Foundations (Weeks 1–4)**

**Goal:** Build strong CS fundamentals + aerospace basics + embedded systems intro

#### **Week 1: Programming Core + Math Refresh**

| Topic | Resource | Tool | Status |
|-------|----------|------|--------|
| Python (data structures, OOP, NumPy) | [CS50P (Harvard)](https://cs50.harvard.edu/python/) | Python 3.11+, VS Code | 📍 Starting |
| C/C++ fundamentals | [Learn C the Hard Way](https://learncodethehardway.org/c/) | GCC, VS Code | ⏳ Queued |
| Linear Algebra | [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra) | — | ⏳ Queued |
| Git/GitHub basics | [Git Immersion](https://gitimmersion.com/) | Git, GitHub | ⏳ Queued |

**Deliverable:** 3–4 small Python scripts on GitHub (matrix calculator, file parser, etc.)

---

#### **Week 2: Linux, Command Line & Aerospace Fundamentals**

| Topic | Resource | Tool | Status |
|-------|----------|------|--------|
| Linux basics (bash, permissions) | [Linux Journey](https://linuxjourney.com/) | Ubuntu (VM or dual-boot) | ⏳ Queued |
| Flight dynamics & aerodynamics | *Introduction to Flight* — Anderson (Ch 1–5) | — | ⏳ Queued |
| Orbital mechanics basics | [NPTEL Rocket Propulsion](https://nptel.ac.in/) | — | ⏳ Queued |
| Coordinate systems & reference frames | YouTube tutorials | — | ⏳ Queued |

**Deliverable:** Notes on coordinate frames + write-up explaining lift, drag, thrust, weight

---

#### **Week 3: Electronics + Embedded Systems Intro**

| Topic | Resource | Tool | Status |
|-------|----------|------|--------|
| Basic electronics | [allaboutcircuits.com](https://www.allaboutcircuits.com/) | Multimeter, breadboard kit | ⏳ Queued |
| Arduino programming | [Arduino docs](https://docs.arduino.cc/) | Arduino Uno/Nano | ⏳ Queued |
| Aerospace sensors (IMU, GPS, barometer) | Datasheets (MPU6050, NEO-6M, BMP280) | Arduino IDE | ⏳ Queued |
| Serial protocols (UART, I2C, SPI) | [SparkFun tutorials](https://learn.sparkfun.com/) | Logic analyzer (optional) | ⏳ Queued |

**Deliverable:** Arduino project — read IMU + GPS data and log to serial monitor

---

#### **Week 4: Control Systems + Intro to Robotics Software**

| Topic | Resource | Tool | Status |
|-------|----------|------|--------|
| Control systems & PID | [Brian Douglas Lectures](https://www.youtube.com/c/BrianBDouglas) | MATLAB/Octave | ⏳ Queued |
| ROS2 introduction | [ROS2 official tutorials](https://docs.ros.org/en/humble/Tutorials.html) | Ubuntu + ROS2 Humble | ⏳ Queued |
| MAVLink protocol | [MAVLink docs](https://mavlink.io/en/) | pymavlink (Python) | ⏳ Queued |

**Deliverable:** Simple PID simulation in Python (virtual pendulum/drone altitude hold) + basic ROS2 pub/sub node

---

### **MONTH 2 — Deep Specialization (Weeks 5–8)**

**Choose ONE track** (recommendation: **Track A** for BCA profile coverage)

#### **TRACK A: Computer Vision & Satellite Data** → Pixxel, SatSure, ideaForge, Asteria

| Week | Topic | Resource | Tool |
|------|-------|----------|------|
| 5 | OpenCV fundamentals | [OpenCV tutorials](https://docs.opencv.org/4.x/) + [PyImageSearch](https://pyimagesearch.com/) | OpenCV, Python |
| 5–6 | Deep learning for vision (CNNs, transfer learning) | [fast.ai](https://course.fast.ai/) or [CS231n (YouTube)](https://www.youtube.com/playlist?list=PLoROMvodv4rOc-Z5UBs2sJf6EmL5cM_pu) | PyTorch/TensorFlow |
| 6 | Remote sensing & satellite imagery | [Google Earth Engine course](https://developers.google.com/earth-engine) | Google Earth Engine, QGIS |
| 7 | Geospatial data processing | [Rasterio docs](https://rasterio.readthedocs.io/) | Rasterio, GDAL, QGIS |
| 7–8 | Applied projects: classification, change detection | [Kaggle satellite datasets](https://www.kaggle.com/datasets?search=satellite) | Kaggle, Colab |

**Deliverable:** End-to-end trained model on satellite imagery (land cover classification or crop health mapping)

---

#### **TRACK B: Drone Autonomy & Embedded Flight Software** → ideaForge, Asteria, Sarla, Bellatrix

| Week | Topic | Resource | Tool |
|------|-------|----------|------|
| 5 | Flight controller firmware | [ArduPilot dev docs](https://ardupilot.org/dev/) or [PX4 docs](https://docs.px4.io/) | Pixhawk or SITL |
| 5–6 | Simulation (Gazebo + ROS2 + drone/rover) | [PX4 + Gazebo SITL](https://docs.px4.io/main/en/simulation/gazebo.html) | Gazebo, ROS2 |
| 6 | Path planning & obstacle avoidance | [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) | Python |
| 7 | State estimation (Kalman Filter / EKF) | [Kalman Filter for Beginners](https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT) | Python/MATLAB |
| 8 | Ground control station + telemetry | [QGroundControl](http://qgroundcontrol.com/) + pymavlink | QGroundControl, Python |

**Deliverable:** Simulated drone completing waypoint mission with obstacle avoidance + live telemetry dashboard

---

### **MONTH 3 — High-Value Projects + Portfolio (Weeks 9–12)**

#### **🖥️ Software Project 1: Satellite Image Analysis Pipeline**

**Target:** Pixxel, SatSure

- Pull free Sentinel-2 imagery (Google Earth Engine / Copernicus Hub)
- Build CNN/U-Net for land cover classification or crop stress detection (NDVI-based)
- Wrap in Flask/Streamlit dashboard
- **Stack:** Python, PyTorch/TensorFlow, GDAL, Streamlit, Google Earth Engine API
- **Why it matters:** This IS their core business — shows you understand their product

**Repo structure:** `month-3-projects/project-1-satellite-pipeline/`

---

#### **🖥️ Software Project 2: Autonomous Drone Mission Simulator**

**Target:** ideaForge, Asteria, Sarla

- Gazebo + PX4 SITL: drone waypoint survey + obstacle avoidance
- Kalman filter for state estimation
- Python ground station (pymavlink) with live telemetry
- **Stack:** ROS2, Gazebo, PX4, Python, pymavlink
- **Why it matters:** GNC + autonomy without needing to own a drone

**Repo structure:** `month-3-projects/project-2-drone-simulator/`

---

#### **🔧 Hardware Project 1: Build & Fly a Quadcopter** *(Optional based on budget)*

**Target:** ideaForge, Asteria, Sarla

- Assemble from frame kit + Pixhawk + ESCs + motors
- Flash ArduPilot, calibrate, tune PID, fly GPS waypoint mission
- Log telemetry data
- **Cost:** ₹15k–25k (consider robotics club collaboration)
- **Why it matters:** "Actually built and flew" > simulations only

**Repo structure:** `month-3-projects/project-3-quadcopter/`

---

#### **Hardware Project 2: Sensor Payload / Telemetry Board**

**Target:** Bellatrix, Ignis, SatSure

- Arduino/ESP32 + BMP280 (altitude) + MPU6050 (orientation) + GPS
- LoRa module for real-time telemetry transmission
- Field test (balloon drop or drone payload)
- **Stack:** ESP32/Arduino, KiCad (optional PCB design), LoRa (RFM95/SX1278)
- **Why it matters:** Scaled-down satellite/rocket telemetry — shows end-to-end pipeline

**Repo structure:** `month-3-projects/project-4-sensor-payload/`

---

#### **Week 12: Portfolio + Cold Outreach**

 **GitHub:**
- Crystal-clear READMEs for all projects
- Problem statement, architecture diagrams, quantified results
- Video demos (even 1 minute)

**Resume:**
- One page, project-first format
- Quantified results ("89% accuracy," "10m² survey in 3min")

*LinkedIn:**
- Post project demos, tag companies

**Cold Email Template:**
```
Hi [Founder/HR],

I'm a BCA student from [college] building aerospace software to learn your stack. 
I just finished [specific project] — it does [X].

GitHub: [link]
Video: [YouTube link]

Would you have 15 min to give feedback? Looking to apply for your internship.

Thanks,
[Your name]
```

---

## Full Tool Stack Reference

| Category | Tools |
|----------|-------|
| Programming | Python, C/C++ |
| Simulation | MATLAB/Octave, Gazebo, PX4 SITL |
| Robotics middleware | ROS2 |
| Computer Vision/ML | OpenCV, PyTorch/TensorFlow |
| Geospatial | QGIS, GDAL, Rasterio, Google Earth Engine |
| Embedded | Arduino IDE, ESP32, Pixhawk, ArduPilot |
| PCB/Hardware design | KiCad (optional, advanced) |
| CAD | FreeCAD or Fusion 360 (optional) |
| Ground control | QGroundControl, pymavlink |
| Version control | Git, GitHub |

---

## Core Reading List

- **Introduction to Flight** — John D. Anderson
- **Orbital Mechanics for Engineering Students** — Howard Curtis
- **Understanding Space: An Introduction to Astronautics** — Sellers
- **ArduPilot & PX4 Developer Documentation** (treat as textbooks)
- **NPTEL Courses** — Search for "rocket propulsion," "flight dynamics," "spacecraft dynamics"

---

## Weekly Time Budget

- **40%** Hands-on coding/building
- **30%** Structured learning (courses, videos, reading)
- **20%** Project work
- **10%** Documentation & writing up learnings

---

## Learning Log

Track your progress week-by-week:

- [Week 1 Progress](./learning-log/week-1.md) ⏳
- [Week 2 Progress](./learning-log/week-2.md) ⏳
- [Week 3 Progress](./learning-log/week-3.md) ⏳
- [Week 4 Progress](./learning-log/week-4.md) ⏳
- (Weeks 5–12 to follow...)

---

##  Key Insights for BCA Students Applying to Aerospace

### **Your Competitive Advantage:**
 You can ship **production-quality software** faster than most  
 You understand **systems architecture** and code organization  
 You can **glue together** hardware + software + cloud APIs  

### **What You Won't Compete On (And Don't Need To):**
 Propulsion physics  
Structural analysis  
 Aerodynamic CFD  

### **What Companies Actually Want From You:**
 **Real projects** (GitHub portfolio beats any certificate)  
 **Software that works** (flight controller firmware, GCS, image processing pipelines)  
 **Communication** (explain your choices, document decisions)  
 **Learning velocity** (this 3-month plan proves it)

---

##  How to Use This Repository

1. **Clone it** and make it your own — add your weekly progress
2. **Pick Month 2 track early** (don't wait to decide)
3. **Build in public** — commit code weekly, not just at project end
4. **Document everything** — future you (and recruiters) will thank you
5. **Ship before perfect** — shipping Month 3 projects in week 11 is way better than perfecting them by week 14

---

##  Target Companies & Their Focus

| Company | What They Do | Your Angle |
|---------|-------------|-----------|
| **Pixxel** | Hyperspectral satellite imaging | Computer vision + satellite data pipelines |
| **SatSure** | Satellite data analytics for agriculture | Remote sensing, crop monitoring, ML |
| **ideaForge** | UAVs + autopilots | Drone autonomy, GNC software |
| **Asteria Aerospace** | Drones + defense tech | Flight software, autonomy, embedded systems |
| **Bellatrix Aerospace** | Propulsion + rocket engines | Telemetry software, data pipelines |
| **Sarla Aviation** | eVTOL urban air mobility | Flight control software, autonomy |
| **Ignis Aerospace** | Rocket propulsion + design | Flight software, avionics, simulation |

---

##  Let's Build This!

This isn't just a learning plan — it's a **proof of work**. By week 12, you'll have:

 4 real projects on GitHub  
 Quantified results (model accuracy, flight autonomy metrics)  
 2+ videos of real outputs  
 Documented learning journey  
 A portfolio that stands out against 500 other applicants  

**Start Week 1 today.** The best time to plant a tree was 10 years ago. The second best time is now.

---

**Last Updated:** July 21, 2026  
**Status:** Just starting the journey!  
**Next Milestone:** Complete Week 1 + push first 3 Python projects by [DATE]

---

*Built by [@fawacreates](https://github.com/fawacreates) as a BCA student learning aerospace software engineering from scratch.*
