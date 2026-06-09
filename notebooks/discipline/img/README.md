# Imaging Node Notebooks

Notebooks demonstrating PDS API access for imaging data, with interactive map visualizations using leafmap and ipyleaflet.

## Installation

```bash
pip install --requirement requirements-img.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

## Notebooks

### MESSENGER Leafmap Visualization
**File:** `leafmap_mess.ipynb`

Queries MESSENGER imaging products from the PDS API and displays their spatial footprints on an interactive leafmap. Demonstrates geospatial filtering, GeoDataFrame construction from PDS metadata, and overlaying image footprints on a base map.
