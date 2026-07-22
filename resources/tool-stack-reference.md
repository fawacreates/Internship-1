# Tool Stack Reference

Complete list of software tools needed for the internship preparation.

## Development Environment

### Core Tools
- **Python 3.11+** - Primary programming language
- **VS Code** - IDE/Text editor
- **Git** - Version control
- **GitHub** - Remote repository
- **Anaconda/Miniconda** - Python environment management

### Installation
```bash
# Python & VS Code
# Download from official websites

# Anaconda (recommended for scientific computing)
conda create -n internship python=3.11
conda activate internship

# Essential packages
pip install numpy pandas matplotlib scipy scikit-learn
```

## Programming Languages

### Python 3.11+
**Key Libraries:**
- NumPy - Numerical computing
- Pandas - Data manipulation
- Matplotlib/Seaborn - Visualization
- Scikit-learn - Machine learning
- PyTorch/TensorFlow - Deep learning
- OpenCV - Computer vision
- Rasterio/GDAL - Geospatial processing

### C/C++
- **GCC/Clang** - Compilers
- **CMake** - Build system
- **Arduino IDE** - Microcontroller programming

## Simulation & Robotics

### Flight Simulation
- **PX4 SITL** - Software-in-the-loop drone simulator
- **Gazebo** - Physics simulator
- **ArduPilot SITL** - ArduPilot simulator
- **QGroundControl** - Ground control station

### ROS2 (Robotics OS)
```bash
# Ubuntu 22.04 installation
sudo apt install ros-humble-desktop

# Key ROS2 packages
ros-humble-gazebo-ros
ros-humble-mavros
ros-humble-geometry-msgs
```

## Computer Vision & ML

### Libraries
- **OpenCV 4.x** - Image processing
- **PyTorch 2.0+** - Deep learning (recommended)
- **TensorFlow/Keras** - Alternative deep learning
- **scikit-image** - Advanced image processing

### Installation
```bash
pip install opencv-python torch torchvision torchaudio
pip install tensorflow
pip install scikit-image pillow
```

## Geospatial Tools

### Python Libraries
- **Rasterio** - GeoTIFF and raster data
- **GDAL** - Geospatial data abstraction
- **Fiona** - Vector data (GIS)
- **Shapely** - Geometric operations
- **Folium** - Map visualization

### Standalone Software
- **QGIS 3.x** - GIS desktop application
- **Google Earth Engine** - Cloud-based analysis

### Installation
```bash
pip install rasterio fiona shapely folium
pip install geopandas pyproj
```

## Electronics & Embedded

### Hardware
- **Arduino Uno/Nano** - Microcontroller boards
- **ESP32** - Advanced microcontroller
- **Pixhawk** - Flight controller
- **Sensors** - IMU, GPS, barometer, etc.

### Software
- **Arduino IDE** - Official IDE
- **PlatformIO** - Advanced IDE
- **KiCad** - PCB design (optional)

### Installation
```bash
# Arduino IDE
# Download from arduino.cc

# PlatformIO (VS Code extension)
# Install from VS Code marketplace
```

## Data Visualization & Dashboard

### Web Frameworks
- **Flask** - Lightweight Python web framework
- **Streamlit** - Rapid data app development
- **Plotly/Dash** - Interactive dashboards

### Installation
```bash
pip install flask streamlit plotly dash
```

## Databases (Optional)

- **PostgreSQL** - Relational database
- **SQLite** - Lightweight embedded database
- **MongoDB** - NoSQL document database

## Documentation & Notebooks

- **Jupyter Notebook** - Interactive Python notebooks
- **Jupyter Lab** - Enhanced notebook environment
- **Sphinx** - Documentation generator

### Installation
```bash
pip install jupyter jupyterlab sphinx
```

## Version Control & Collaboration

- **Git** - Version control system
- **GitHub** - Remote repository hosting
- **GitHub Desktop** - GUI for Git (optional)

## Complete Setup Script

```bash
#!/bin/bash
# Setup script for internship environment

# Create conda environment
conda create -n internship python=3.11 -y
conda activate internship

# Install Python packages
pip install --upgrade pip
pip install numpy pandas matplotlib scipy scikit-learn
pip install pytorch torchvision torchaudio
pip install opencv-python
pip install rasterio fiona shapely folium geopandas
pip install flask streamlit plotly jupyter
pip install pymavlink

echo "Setup complete! Environment: internship"
echo "Activate with: conda activate internship"
```

## Hardware Setup (For Projects 3 & 4)

### Project 3: Quadcopter
- Frame kit (DJI F450 or similar)
- Flight controller (Pixhawk 4)
- Motors (920KV)
- ESCs (30A)
- LiPo battery (3S, 5000mAh)
- Mission Planner/QGroundControl

### Project 4: Sensor Payload
- ESP32 development board
- BMP280 barometer
- MPU6050 IMU
- NEO-6M GPS
- RFM95 LoRa module
- Breadboard, jumper wires
- 3.7V LiPo battery

## Resource Links

- Python: https://www.python.org/
- VS Code: https://code.visualstudio.com/
- Anaconda: https://www.anaconda.com/
- PyTorch: https://pytorch.org/
- ROS2: https://docs.ros.org/
- PX4: https://px4.io/
- Gazebo: https://gazebosim.org/
- QGIS: https://www.qgis.org/
