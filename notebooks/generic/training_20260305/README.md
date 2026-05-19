# PDS API Training Notebooks (March 2026)

Introductory notebooks from the March 2026 PDS API training session. Designed for new users learning to access PDS data programmatically.

## Installation

```bash
pip install -r requirements-training.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

## Notebooks

Work through these in order for a guided introduction to the PDS API.

### 01 — Getting Started with Peppi
**File:** `01_peppi_start.ipynb`

Introduction to `pds.peppi`: connecting to the PDS registry, running your first search, and converting results to a pandas DataFrame.

### 02 — Direct API Access
**File:** `02_direct_api_access.ipynb`

Shows how to query the PDS Search API directly with HTTP requests (no client library). Useful for understanding the underlying REST interface and for environments where the Python client is unavailable.

### 03 — Finding Data by DOI
**File:** `03_data_with_doi.ipynb`

Demonstrates resolving a dataset DOI to its PDS collection and retrieving associated products via the REST API.

### 04 — Peppi with DOI
**File:** `04_peppi_with_doi.ipynb`

Combines DOI resolution with `pds.peppi` for a cleaner end-to-end workflow: resolve a DOI, load the collection, and query products with the Peppi client.
