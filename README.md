# Planetary Data System API Notebook

This repository contains example [JupyterLab notebooks](https://jupyter.org) for the [application programmer's interface (API)](https://nasa-pds.github.io/pds-api/) of the [Planetary Data System](https://pds.nasa.gov/). You can incorporate these into your existing JupiyterLab notebooks for the plotting and exhibition of planetary and other scientific data, and use them as springboards for new notebooks. You can also run these notebooks directly on any Python-capable computer with a web browser.


## 🖥 Prerequisites

To run these notebooks locally, you'll need [Python 3.7](https://python.org/) or later as well as a web browser.


## 🏃‍♀️ Getting Started

Run the following commands from a terminal and your default web browser should launch:

```console
$ # Create a virtual Python environment to isolate Jupyter and PDS dependencies
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade --quiet pip
$ # Install the dependencies
$ pip install --requirement requirements.txt
$ # Start it up
$ jupyter-lab
```
    
At this point you'll have a locally running JupyterLab server and your browser opened to it. (If not, point your browser to http://localhost:8888/lab).

From here, you can try out the PDS API notebooks in the `/notebooks/` folder in the file tree on the left side:

-   `ovirs` contains demonstration notebooks for the [OSIRIS-REx Visible and InfraRed Spectrometer, OVIRS](https://www.asteroidmission.org). Within this folder are two sub-folders with the actual demonstration notebooks:
    -   `part1` has the notebook `explore-a-collection.ipynb` that shows how to get a get and explore a data collection with the API.
    -   `part2` has a notebook `find-data-standalone.ipynb` that extracts a specific data collection subset. A [demo video](https://www.youtube.com/watch?v=jTclsXR713Y) of this notebook is available.
-   `wwt` exhibits using PDS data in [WWT](https://pywwt.readthedocs.io/) via the PDS API; note, however, that this is currently incomplete and is a work in progress.


## 👥 Contributing

Within the NASA Planetary Data System, we value the health of our community as much as the code. Towards that end, we ask that you read and practice what's described in these documents:

-   Our [contributor's guide](https://github.com/NASA-PDS/.github/blob/main/CONTRIBUTING.md) delineates the kinds of contributions we accept.
-   Our [code of conduct](https://github.com/NASA-PDS/.github/blob/main/CODE_OF_CONDUCT.md) outlines the standards of behavior we practice and expect by everyone who participates with our software.


## 📃 License

The project is licensed under the [Apache version 2](LICENSE.md) license.
