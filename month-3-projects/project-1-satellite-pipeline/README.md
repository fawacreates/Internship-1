# Project 1: Satellite Image Analysis Pipeline

## Target Companies
Pixxel, SatSure

## Project Overview
Build an end-to-end satellite imagery analysis system using free public data.

### Key Features
- Sentinel-2 satellite data ingestion
- Land cover classification using CNN/U-Net
- Crop health monitoring via NDVI
- Interactive Streamlit dashboard
- RESTful API for inference

### Tech Stack
- Python, PyTorch/TensorFlow
- GDAL, Rasterio (geospatial)
- Google Earth Engine API
- Streamlit (UI), Flask (API)
- PostgreSQL (optional, for data)

### Data Sources
- [Google Earth Engine](https://earthengine.google.com/)
- [Copernicus Hub](https://scihub.copernicus.eu/)
- [Kaggle Satellite Datasets](https://www.kaggle.com/datasets?search=satellite)

## Directory Structure
```
project-1-satellite-pipeline/
├── src/
│   ├── data_processing.py
│   ├── model.py
│   ├── inference.py
│   └── utils.py
├── models/
│   └── trained_model.pth
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── streamlit_app.py
├── api_server.py
├── requirements.txt
└── README.md
```

## Deliverables
1. Trained model (89%+ accuracy)
2. Processing pipeline (Jupyter notebook)
3. Streamlit dashboard (live demo)
4. GitHub repo with documentation
5. Demo video (2-3 minutes)
