# PDS federated API demo, Osiris-Rex OVIRS data visualization
# PART 2: FIND DATA YOU ARE INTERESTED IN

The purpose of this notebook is to demostrate how the PDS web API can be used to access the PDS data for a scientific use case.

The documention of the PDS web API is available on https://nasa-pds.github.io/pds-api/

This notebook is available on https://github.com/NASA-PDS/pds-api-notebook

<b>It is the 2nd part of 2 Use cases:</b>
 - <u>Part1</u>: explore the collection
 - <u>Part2</u>: find specific the data you are interested in
 
 <br/>
 
 WARNING: This notebook is a demo and not a real scientific use case. It might contain mistake in the way the data is used or displayed.


```python
from __future__ import print_function
from pprint import pprint
import time
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from astropy.io import fits
```

The PDS API is accessed using a python client library documented on https://nasa-pds.github.io/pds-api-client/


```python
import pds.api_client as pds_api
```

## Use the PDS demo web API server 

Connect to the demo server. See User Interface of the web API: http://pds-gamma.jpl.nasa.gov/api/swagger-ui.html

<b>Note: </b> this piece of code will be wrapped into a helper function so that 1 line will be enough to connect to the API using a default host


```python
configuration = pds_api.Configuration()

# demo server
configuration.host = 'http://pds-gamma.jpl.nasa.gov/api/'

api_client = pds_api.ApiClient(configuration)

```

## Get observations around specific spot (lat=12, lon=24) closer than 4 km

Get the result found in part1 by directly posting the search criteria to the API

The query syntax is described in the PDS API specification. It uses the following operators:
- comparison: lt, le, ...
- boolean: and, or, not
- groups: (, )


```python
start_time = time.time() 

products_api = pds_api.ProductsApi(api_client)

criteria = "((orex:spatial.orex:target_range lt 4.0)"
criteria += " and (orex:spatial.orex:latitude ge 9.0) and (orex:spatial.orex:latitude le 15.0)"
criteria += " and (orex:spatial.orex:longitude ge 21.0) and (orex:spatial.orex:longitude le 27.0))"

properties_of_interest = ['orex:spatial.orex:latitude', 'orex:spatial.orex:longitude', 'orex:spatial.orex:target_range', 'ops:Data_File_Info.ops:file_ref']

closer_products = products_api.products(q=criteria, fields=properties_of_interest)

elapsed = time.time() - start_time
print(f'retrieved {len(closer_products.data)} products in {elapsed} seconds')

```

    retrieved 4 products in 0.6159060001373291 seconds



```python
lidvids = [product.id for product in closer_products.data]
print(f'The lidvids of the selected products are {lidvids}')
```

    The lidvids of the selected products are ['urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204129s468_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204130s368_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204131s368_ovr_scil2.fits::1.0']


### Extract the links to the data files


```python
data_files = [product.properties['ops:Data_File_Info.ops:file_ref'] for product in closer_products.data]
print(f'product data file url: {data_files}')
```

    product data file url: ['https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204128S567_ovr_scil2.fits', 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204129S468_ovr_scil2.fits', 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204130S368_ovr_scil2.fits', 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204131S368_ovr_scil2.fits']


## Plot the data (FITS files)

Plot the spectra of the 4 observations on the same figure, one figure per dimension of the instrument.



```python
hduls = [fits.open(data_file) for data_file in data_files]

for i in range(20): # for each dimension of the instrument
    fig, ax = plt.subplots()
    ax.set_title(f'detector {i}')
    for hdul in hduls: # for each observation
        ax.plot(hdul[2].data[0, i, :], hdul[0].data[0, i, :])
    ax.set_xlabel('wavelength (micrometers)')
    ax.set_ylabel('radiance')
```


    
![png](images/output_13_0.png)
    



    
![png](images/output_13_1.png)
    



    
![png](images/output_13_2.png)
    



    
![png](images/output_13_3.png)
    



    
![png](images/output_13_4.png)
    



    
![png](images/output_13_5.png)
    



    
![png](images/output_13_6.png)
    



    
![png](images/output_13_7.png)
    



    
![png](images/output_13_8.png)
    



    
![png](images/output_13_9.png)
    



    
![png](images/output_13_10.png)
    



    
![png](images/output_13_11.png)
    



    
![png](images/output_13_12.png)
    



    
![png](images/output_13_13.png)
    



    
![png](images/output_13_14.png)
    



    
![png](images/output_13_15.png)
    



    
![png](images/output_13_16.png)
    



    
![png](images/output_13_17.png)
    



    
![png](images/output_13_18.png)
    



    
![png](images/output_13_19.png)
    



```python

```
