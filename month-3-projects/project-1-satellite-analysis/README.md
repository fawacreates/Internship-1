# Project 1: Satellite Image Analysis Pipeline

**Target:** Pixxel, SatSure

## Objective
Build an end-to-end pipeline to classify land cover and detect crop stress using satellite imagery.

## Architecture

```
Google Earth Engine / Copernicus Hub
         ↓
   Sentinel-2 Imagery
         ↓
   Preprocessing (GDAL/Rasterio)
         ↓
   CNN/U-Net Model (PyTorch)
         ↓
   Land Cover Classification
   + NDVI Calculation
         ↓
   Streamlit Dashboard
         ↓
   Interactive Results Visualization
```

## Tech Stack
- **Data Source:** Google Earth Engine API / Copernicus Hub
- **Processing:** GDAL, Rasterio, NumPy
- **ML Framework:** PyTorch / TensorFlow
- **Model:** U-Net for segmentation, ResNet50 for classification
- **Dashboard:** Streamlit
- **Version Control:** Git/GitHub

## Milestones

### Phase 1: Data Acquisition
- [ ] Set up Google Earth Engine account
- [ ] Pull Sentinel-2 tiles for target region
- [ ] Export as GeoTIFF files
- [ ] Document dataset statistics

### Phase 2: Data Processing
- [ ] Load and normalize imagery
- [ ] Create NDVI/spectral indices
- [ ] Train/validation/test split
- [ ] Data augmentation

### Phase 3: Model Development
- [ ] Implement U-Net or ResNet model
- [ ] Train on labeled satellite data
- [ ] Evaluate metrics (accuracy, F1, IoU)
- [ ] Hyperparameter tuning

### Phase 4: Dashboard Development
- [ ] Build Streamlit app
- [ ] Upload satellite image
- [ ] Display prediction overlay
- [ ] Show NDVI heatmap
- [ ] Export results

### Phase 5: Documentation & Deployment
- [ ] README with results
- [ ] Training curve plots
- [ ] Before/after images
- [ ] Usage instructions
- [ ] Deploy to Streamlit Cloud (optional)

## Expected Outcomes
- [ ] Trained model with >85% accuracy
- [ ] Working dashboard
- [ ] GitHub repo with clean code
- [ ] Sample predictions on Sentinel-2 data
- [ ] Time to predict per image

## Files in This Directory
- `data/` - Downloaded satellite tiles
- `notebooks/` - Jupyter notebooks for exploration
- `models/` - Trained model checkpoints
- `src/` - Production code (preprocessing, model, app)
- `results/` - Output predictions and visualizations
