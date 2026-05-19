# Planetary Plasma Interactions Node Notebooks

Notebooks demonstrating PDS API access for plasma and magnetometer data, including Galileo magnetometer time-series analysis and WorldWide Telescope integration.

## Installation

```bash
pip install -r requirements-ppi.txt
```

Run from the repository root. Then start JupyterLab:

```bash
jupyter-lab
```

> **Note:** The `GLL_MagPlot` notebook uses pyWWT for 3D visualization. After installing, you may need to enable the JupyterLab extension:
> ```bash
> jupyter labextension install @wwtelescope/jupyterlab
> jupyter lab build
> ```
> Open a separate tab with the AAS WorldWide Telescope icon to interact with the WWT window.

## Notebooks

### Galileo Magnetometer Plot
**File:** `GLL_MagPlot.ipynb`

Queries Galileo magnetometer (MAG) data from the PDS API, reads PDS4-labeled binary data, and produces time-series plots of the magnetic field components. Also demonstrates projecting data into the AAS WorldWide Telescope for 3D spatial context.

### Pandas Data Read
**File:** `pandas_data_read.ipynb`

A lightweight example showing how to retrieve PDS API results directly into a pandas DataFrame. Useful as a starting point for tabular data workflows.
