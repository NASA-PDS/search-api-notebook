# Small Bodies Node Notebooks

Notebooks demonstrating PDS API access for small bodies data, including OSIRIS-REx OVIRS spectroscopy and CMOR meteor radar data.

## Installation

```bash
pip install --requirement requirements-sbn.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

## Notebooks

### CMOR Data as CSV
**File:** `cmor_data_as_csv_demo.ipynb`

Demonstrates locating CMOR (Canadian Meteor Orbit Radar) data products in the PDS registry and exporting them to CSV using the Planetary Data Reader (`pdr`).

### OVIRS Part 1 — Explore a Collection
**File:** `ovirs/part1/explore-a-collection.ipynb`

Explores the OSIRIS-REx OVIRS calibrated data collection using the legacy `pds.api_client`. Shows how to list products, inspect collection metadata, and page through large result sets.

### OVIRS Part 2 — Find Data (Standalone)
**File:** `ovirs/part2/find-data-standalone.ipynb`

Builds on Part 1 to filter OVIRS spectra by observation geometry and time window using `pds.peppi`. Demonstrates targeted queries and spectral data retrieval for downstream analysis.
