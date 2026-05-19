# Geosciences Node Notebooks

Notebooks demonstrating PDS API access for geosciences data, including radio science, digital elevation models, and planetary flyby visualizations.

## Installation

```bash
pip install -r requirements-geo.txt
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

Reads a Digital Elevation Model (DEM) product from PDS and renders it as an interactive map. Shows PDS4 label parsing with `pds4-tools` and raster visualization.

### MESSENGER Radio Science with PDR
**File:** `messenger-radio-science-with-pdr.ipynb`

Accesses MESSENGER radio science data via the PDS API and reads it using the Planetary Data Reader (`pdr`). Demonstrates locating calibrated data products and plotting time-series results.
