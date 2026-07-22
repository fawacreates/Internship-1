# Month 2 Track A: Computer Vision & Satellite Data

Practice files for computer vision and remote sensing specialization.

## Directory Structure

```
month-2-track-a/
├── 01_opencv_basics/
│   ├── image_loading.py
│   ├── filtering.py
│   ├── edge_detection.py
│   └── feature_matching.py
├── 02_deep_learning/
│   ├── mnist_classifier.py
│   ├── transfer_learning.py
│   └── simple_cnn.py
├── 03_satellite_imagery/
│   ├── earth_engine_api.py
│   ├── ndvi_calculation.py
│   └── image_classification.py
└── notebooks/
    ├── sentinel2_exploration.ipynb
    └── land_cover_classification.ipynb
```

## Resources

- OpenCV: https://docs.opencv.org/4.x/
- PyTorch: https://pytorch.org/
- Fast.ai: https://course.fast.ai/
- Google Earth Engine: https://developers.google.com/earth-engine

## Getting Started

### Install Dependencies
```bash
pip install opencv-python numpy scipy matplotlib
pip install torch torchvision
pip install tensorflow
pip install google-earth-engine
pip install rasterio gdal
```

### Run Examples
```bash
python3 01_opencv_basics/image_loading.py
python3 02_deep_learning/mnist_classifier.py
python3 03_satellite_imagery/ndvi_calculation.py
```

## Practice Path

1. **Week 5:** Master OpenCV fundamentals
   - [ ] Image I/O and display
   - [ ] Filtering and blurring
   - [ ] Edge detection (Canny, Sobel)
   - [ ] Feature detection and matching

2. **Week 5-6:** Deep Learning for Vision
   - [ ] MNIST classification (warm-up)
   - [ ] Transfer learning with ResNet
   - [ ] CNN from scratch
   - [ ] Semantic segmentation

3. **Week 6:** Satellite Imagery Basics
   - [ ] Access Sentinel-2 data via Earth Engine
   - [ ] Understand band combinations
   - [ ] Calculate vegetation indices (NDVI)
   - [ ] Explore QGIS

4. **Week 7:** Geospatial Processing
   - [ ] Read/write GeoTIFF files
   - [ ] Raster math with Rasterio
   - [ ] Reproject and resample imagery
   - [ ] Create NDVI heatmaps

5. **Week 7-8:** Applied Projects
   - [ ] Multi-class land cover classification
   - [ ] Crop stress detection
   - [ ] Change detection pipeline
