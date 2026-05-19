# Simple Notebooks

Lightweight utility notebooks demonstrating basic PDS API access patterns and data conversion.

## Installation

```bash
pip install -r requirements-simple.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

## Notebooks

### Tab to CSV
**File:** `tab-to-csv.ipynb`

Locates a PDS4 fixed-width table product via the PDS API, reads it with the Planetary Data Reader (`pdr`), and exports it to CSV. A useful template for extracting legacy PDS table formats into modern data workflows.
