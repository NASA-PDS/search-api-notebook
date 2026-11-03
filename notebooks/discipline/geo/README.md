# Geosciences Node Notebooks

Notebooks demonstrating PDS API access for geosciences data, including radio science, digital elevation models, and planetary flyby visualizations.

## Installation

```bash
pip install --requirement requirements-geo.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

## Notebooks

### BepiColombo Flyby Visualization
**File:** `BepiColombo_FlybyVisualization.ipynb`

Visualizes the BepiColombo spacecraft's flyby trajectory using SPICE-derived geometry and PDS API metadata. Demonstrates how to query position/attitude data and plot 3D flyby geometry with matplotlib.

### DEM Map Visualization
**File:** `DEM_MapVisualization.ipynb`

Reads a lunar Digital Elevation Model (DEM) product from PDS and renders it inline with matplotlib. Shows PDS4 label parsing with `pds4-tools`, resolving products by logical identifier, and GDAL `DEMProcessing` hillshade, colour relief and slope. Runs headless, no GUI required.

The GDAL bindings are optional. Without them the notebook falls back to a NumPy hillshade. To install them, match your system GDAL:

```bash
pip install gdal=="$(gdal-config --version)"
```

### MESSENGER Radio Science with PDR
**File:** `messenger-radio-science-with-pdr.ipynb`

Accesses MESSENGER radio science data via the PDS API and reads it using the Planetary Data Reader (`pdr`). Demonstrates locating calibrated data products and plotting time-series results.
