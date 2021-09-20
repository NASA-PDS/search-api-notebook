# PDS federated API demo, Osiris-Rex OVIRS data visualization
# PART 1: EXPLORE A COLLECTION

The purpose of this notebook is to demostrate how the PDS web API can be used to access the PDS data for a scientific use case.

The documention of the PDS web API is available on https://nasa-pds.github.io/pds-api/

This notebook is available on https://github.com/NASA-PDS/pds-api-notebook

<b>2 Use cases:</b>
 - <u>Part1</u>: explore the collection
 - <u>Part2</u>: find/visualize specific the data you are interested in
 
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

Connect to the demo server. See User Interface of the web API: https://pds-gamma.jpl.nasa.gov/api/swagger-ui.html

<b>Note: </b> this piece of code will be wrapped into a helper function so that 1 line will be enough to connect to the API using a default host


```python
configuration = pds_api.Configuration()

# demo server
configuration.host = 'https://pds-gamma.jpl.nasa.gov/api/'

api_client = pds_api.ApiClient(configuration)

```

## Explore a collection

### Get the lidvid of your collection of interest

Search for a collection of interest on https://pds.nasa.gov/datasearch/keyword-search/ (or https://pds.nasa.gov > Data Search > Keyword Search):
- Search for "osiris rex ovirs collection" (https://pds.nasa.gov/datasearch/keyword-search/search.jsp?q=osiris+rex+ovirs+collection)
- Click on the first collection on the results
- Copy the lidvid


### Get the properties available for the observational products belonging to the selected collection

Get the properties available for the product belonging to the collection of interest using CollectionsProductsApi.products_of_a_collection (see https://nasa-pds.github.io/pds-api-client/api/api_client.api.html#api_client.api.collections_products_api.CollectionsProductsApi)


```python
lidvid = 'urn:nasa:pds:orex.ovirs:data_calibrated::10.0'

collection_products_api = pds_api.CollectionsProductsApi(api_client)
api_response = collection_products_api.products_of_a_collection(lidvid , start=0, limit=20, only_summary=True)
available_properties = api_response.to_dict()['summary']['properties']
print(f"The available properties for the selected products are {available_properties}")
```

    The available properties for the selected products are ['pds:Modification_Detail.pds:description', 'pds:Axis_Array.pds:axis_name', 'pds:Local_Internal_Reference.pds:local_reference_type', 'pds:File.pds:file_size', 'pds:Modification_Detail.pds:modification_date', 'orex:Spatial.orex:bennu_radec_target', 'orex:Spatial.orex:emission_angle', 'pds:Internal_Reference.pds:lidvid_reference', 'ops:Label_File_Info.ops:md5_checksum', 'vid', 'orex:Spatial.orex:bore_angle', 'orex:Mission_Information.orex:mission_phase_identifier', 'orex:Spatial.orex:phase_angle', 'pds:Array_2D_Spectrum.pds:axes', 'orex:Time.orex:mid_obs', 'pds:Observing_System_Component.pds:type', 'orex:Spatial.orex:declination', 'sp:Observation_Parameters.sp:resolution_limit_wavelength', 'sp:Observation_Parameters.sp:net_integration_time', 'orex:Time.orex:mid_obs_et', 'sp:Spectral_Characteristics.sp:spectral_bin_type', 'pds:Axis_Array.pds:sequence_number', 'ops:Data_File_Info.ops:md5_checksum', 'pds:Identification_Area.pds:title', 'sp:Observation_Parameters.sp:number_of_exposures', 'pds:Array_2D_Spectrum.pds:local_identifier', 'pds:Investigation_Area.pds:name', 'ops:Label_File_Info.ops:creation_date_time', 'orex:Time.orex:exposure', 'sp:Field_of_View.sp:description', 'orex:Spatial.orex:bennu_dec', 'geom:SPICE_Kernel_Identification.geom:kernel_type', 'ref_lid_product', 'orex:Mission_Information.orex:mission_phase_name', 'pds:Internal_Reference.pds:comment', 'orex:Spatial.orex:bennu_radec_quality', 'pds:File.pds:creation_date_time', 'ops:Data_File_Info.ops:creation_date_time', 'pds:Observing_System_Component.pds:description', 'pds:Internal_Reference.pds:reference_type', 'pds:Array_2D.pds:local_identifier', 'pds:Primary_Result_Summary.pds:purpose', 'pds:Identification_Area.pds:information_model_version', 'disp:Display_Direction.disp:horizontal_display_axis', 'orex:Spatial.orex:semiminor_axis', 'pds:Local_Internal_Reference.pds:local_identifier_reference', 'orex:Spatial.orex:right_ascension', 'orex:Spatial.orex:boresight_x', 'pds:Time_Coordinates.pds:start_date_time', 'orex:Spatial.orex:boresight_y', 'orex:Spatial.orex:boresight_z', 'sp:Spectral_Characteristics.sp:spectrum_format', 'pds:Observing_System.pds:name', 'pds:Header.pds:object_length', 'orex:Spatial.orex:fov_fill_factor', 'lidvid', 'pds:Modification_Detail.pds:version_id', 'ops:Label_File_Info.ops:file_size', 'pds:Array_2D.pds:description', 'ops:Data_File_Info.ops:file_name', 'orex:Spatial.orex:boresight_range', 'pds:Element_Array.pds:data_type', 'orex:Spatial.orex:fov_fill_flag', 'geom:Geometry_Orbiter.geom:geometry_reference_time_tdb', 'orex:Time.orex:utc', 'geom:Geometry_Orbiter.geom:geometry_reference_time_utc', 'lid', 'pds:Header.pds:parsing_standard_id', 'pds:Header.pds:offset', 'ref_lid_instrument', 'pds:File.pds:file_name', 'product_class', 'pds:Array_2D_Spectrum.pds:axis_index_order', 'orex:OVIRS_Instrument_Attributes.orex:fpa_moly_a_temp_x', 'pds:Time_Coordinates.pds:stop_date_time', 'ref_lidvid_product', 'pds:Primary_Result_Summary.pds:processing_level', 'orex:Spatial.orex:bennu_ra', 'ops:Label_File_Info.ops:file_ref', 'orex:Spatial.orex:semimajor_axis', 'pds:Element_Array.pds:unit', 'pds:Array_2D.pds:axis_index_order', 'ops:Data_File_Info.ops:mime_type', 'pds:Target_Identification.pds:name', 'sp:Bin_Description.sp:bin_profile_description', 'pds:Observing_System_Component.pds:name', 'orex:Spatial.orex:bore_flag', 'pds:Array_2D.pds:offset', 'geom:SPICE_Kernel_Identification.geom:spice_kernel_file_name', 'pds:Identification_Area.pds:product_class', 'pds:Array_2D_Spectrum.pds:description', 'ref_lid_instrument_host', 'title', 'ops:Data_File_Info.ops:file_ref', '_package_id', 'disp:Display_Direction.disp:vertical_display_direction', 'pds:Identification_Area.pds:version_id', 'orex:Spatial.orex:sun_range', 'disp:Display_Direction.disp:vertical_display_axis', 'pds:Internal_Reference.pds:lid_reference', 'sp:Circular_FOV.sp:diameter_angle', 'pds:Identification_Area.pds:logical_identifier', 'ops:Data_File_Info.ops:file_size', 'orex:Time.orex:expo_ms', 'pds:Axis_Array.pds:elements', 'geom:SPICE_Kernel_Identification.geom:kernel_provenance', 'pds:Array_2D_Spectrum.pds:offset', 'ref_lid_investigation', 'pds:Array_2D.pds:axes', 'ops:Label_File_Info.ops:blob', 'orex:Spatial.orex:longitude', 'orex:Spatial.orex:latitude', 'ops:Label_File_Info.ops:file_name', 'pds:Target_Identification.pds:type', 'orex:Spatial.orex:incidence_angle', 'orex:Time.orex:mid_obs_sclk', 'disp:Display_Direction.disp:horizontal_display_direction', 'orex:Spatial.orex:target_range', 'pds:Investigation_Area.pds:type']


### Request specific properties of all the observational products of the collection

Get the latitude, longitude and target_range of the observational products belonging to the collection

The API results are paginated, to get all the results we need to go through the pages.


```python
properties_of_interest = ['orex:spatial.orex:latitude', 'orex:spatial.orex:longitude', 'orex:spatial.orex:target_range']

start = 0
limit = 500
products = []
pbar = tqdm()

start_time = time.time()
while True:
    pbar.update(int(start/500))
    
    api_response = collection_products_api.products_of_a_collection(
        'urn:nasa:pds:orex.ovirs:data_calibrated::10.0' , 
        start=start, 
        limit=limit, 
        fields=properties_of_interest)

    if api_response.data:
        products.extend(api_response.data)
        start += limit
    else:
        break

elapsed = time.time() - start_time
print(f'retrieved {start} products in {elapsed/60.0} minutes')

pbar.close()


```


    0it [00:00, ?it/s]


    retrieved 279500 products in 12.354426515102386 minutes


### Filter out records with no valid values

Some records have fill values for the fields we are interested in (e.g. latitude == -9999, we want to remove them fro our results.



```python
def at_least_one_valid_value(p):
    return ((p['orex:spatial.orex:latitude'] !=  '-9999') \
           and (p['orex:spatial.orex:latitude'] != None))

def filter_out_invalid(products):
    properties = []
    for product in products:
        if at_least_one_valid_value(product.properties):
            p = product.properties
            p['id'] = product.id
            properties.append(p)
    return properties

properties = filter_out_invalid(products)
        
print(f"The values of the selected properties are")
pprint(properties[:3])
```

    The values of the selected properties are
    [{'id': 'urn:nasa:pds:orex.ovirs:data_calibrated:20181102t041236s859_ovr_scil2.fits::1.0',
      'orex:spatial.orex:latitude': '-22.546203099740598',
      'orex:spatial.orex:longitude': '29.6493567602281',
      'orex:spatial.orex:target_range': '197.757787474397'},
     {'id': 'urn:nasa:pds:orex.ovirs:data_calibrated:20181102t041237s759_ovr_scil2.fits::1.0',
      'orex:spatial.orex:latitude': '-18.1849081622853',
      'orex:spatial.orex:longitude': '16.445177388920598',
      'orex:spatial.orex:target_range': '197.757720053807'},
     {'id': 'urn:nasa:pds:orex.ovirs:data_calibrated:20181102t041238s659_ovr_scil2.fits::1.0',
      'orex:spatial.orex:latitude': '-14.845147832590499',
      'orex:spatial.orex:longitude': '7.29380975545429',
      'orex:spatial.orex:target_range': '197.757652690671'}]


### Transpose to extract lat,lon and target range as columns, ready to plot 


```python
def transpose(properties):
    lat = [float(p['orex:spatial.orex:latitude']) for p in properties]
    lon = [float(p['orex:spatial.orex:longitude']) for p in properties]
    target_range = [float(p['orex:spatial.orex:target_range']) for p in properties]
    return lat, lon, target_range

lat, lon, target_range = transpose(properties)
print(f'The target_range values for the selected products are {target_range[:3]}')
```

    The target_range values for the selected products are [197.757787474397, 197.757720053807, 197.757652690671]


### Plot the lat,lon of the observations, colored by target_range


```python
def observation_map(lat, lon, target_range, vmax=25):
    fig, ax = plt.subplots()

    ax.set_xlabel('longitude')
    ax.set_ylabel('latitude')
    ax.set_title('orex.ovirs products lat,lon')

    im = ax.scatter(lon, lat, c=target_range, vmin=0, vmax=vmax)

    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('target range (km)')
    
observation_map(lat,lon, target_range, vmax=25)

```


    
![png](images/output_19_0.png)
    


### Overview of the observation target_range with an histogram


```python
plt.hist(target_range, range=(0, 15))
```




    (array([    0.,     0., 32390., 18425.,     0.,     0.,     0.,     0.,
                0.,     0.]),
     array([ 0. ,  1.5,  3. ,  4.5,  6. ,  7.5,  9. , 10.5, 12. , 13.5, 15. ]),
     <BarContainer object of 10 artists>)




    
![png](images/output_21_1.png)
    


### Get observations around specific spot (lat=12, lon=24) closer than 4 km


```python
lidvids = [p['id'] for p in properties if float(p['orex:spatial.orex:target_range']) < 4.0 
          and abs(float(p['orex:spatial.orex:latitude']) - 12.0) < 3.0
          and abs(float(p['orex:spatial.orex:longitude']) - 24.0) < 3.0]
print(f'The lidvids of the selected products are {lidvids}')
```

    The lidvids of the selected products are ['urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204129s468_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204130s368_ovr_scil2.fits::1.0', 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204131s368_ovr_scil2.fits::1.0']


### Get the full product description


```python
products_api = pds_api.ProductsApi(api_client)
product = products_api.products_by_lidvid(lidvids[0])
print(product)
```

    {'description': None,
     'id': 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits::1.0',
     'investigations': [{'description': None,
                         'href': 'https://pds-gamma.jpl.nasa.gov/products/urn:nasa:pds:context:investigation:mission.orex',
                         'id': 'urn:nasa:pds:context:investigation:mission.orex',
                         'title': None,
                         'type': None}],
     'metadata': {'creation_date_time': '2019-10-23T19:05:39.752Z',
                  'label_url': 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204128S567_ovr_scil2.xml',
                  'update_date_time': None,
                  'version': '1.0'},
     'observing_system_components': [{'description': None,
                                      'href': 'https://pds-gamma.jpl.nasa.gov/products/urn:nasa:pds:context:instrument_host:spacecraft.orex',
                                      'id': 'urn:nasa:pds:context:instrument_host:spacecraft.orex',
                                      'title': None,
                                      'type': None},
                                     {'description': None,
                                      'href': 'https://pds-gamma.jpl.nasa.gov/products/urn:nasa:pds:context:instrument:ovirs.orex',
                                      'id': 'urn:nasa:pds:context:instrument:ovirs.orex',
                                      'title': None,
                                      'type': None}],
     'properties': {'_package_id': 'd8f102ae-f1b7-4009-8a94-240a687eebf0',
                    'disp:Display_Direction.disp:horizontal_display_axis': ['Sample',
                                                                            'Sample',
                                                                            'Sample',
                                                                            'Sample',
                                                                            'Sample',
                                                                            'Sample'],
                    'disp:Display_Direction.disp:horizontal_display_direction': ['Left '
                                                                                 'to '
                                                                                 'Right',
                                                                                 'Left '
                                                                                 'to '
                                                                                 'Right',
                                                                                 'Left '
                                                                                 'to '
                                                                                 'Right',
                                                                                 'Left '
                                                                                 'to '
                                                                                 'Right',
                                                                                 'Left '
                                                                                 'to '
                                                                                 'Right',
                                                                                 'Left '
                                                                                 'to '
                                                                                 'Right'],
                    'disp:Display_Direction.disp:vertical_display_axis': ['Line',
                                                                          'Line',
                                                                          'Line',
                                                                          'Line',
                                                                          'Line',
                                                                          'Line'],
                    'disp:Display_Direction.disp:vertical_display_direction': ['Bottom '
                                                                               'to '
                                                                               'Top',
                                                                               'Bottom '
                                                                               'to '
                                                                               'Top',
                                                                               'Bottom '
                                                                               'to '
                                                                               'Top',
                                                                               'Bottom '
                                                                               'to '
                                                                               'Top',
                                                                               'Bottom '
                                                                               'to '
                                                                               'Top',
                                                                               'Bottom '
                                                                               'to '
                                                                               'Top'],
                    'geom:Geometry_Orbiter.geom:geometry_reference_time_tdb': '606472957.753112',
                    'geom:Geometry_Orbiter.geom:geometry_reference_time_utc': '2019-03-21T20:41:28.567Z',
                    'geom:SPICE_Kernel_Identification.geom:kernel_provenance': 'Reconstructed',
                    'geom:SPICE_Kernel_Identification.geom:kernel_type': 'MK',
                    'geom:SPICE_Kernel_Identification.geom:spice_kernel_file_name': 'spoc-digest-2019-04-10T05_59_50.989Z.mk',
                    'lid': 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits',
                    'lidvid': 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits::1.0',
                    'ops:Data_File_Info.ops:creation_date_time': '2019-10-24T19:59:00Z',
                    'ops:Data_File_Info.ops:file_name': '20190321T204128S567_ovr_scil2.fits',
                    'ops:Data_File_Info.ops:file_ref': 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204128S567_ovr_scil2.fits',
                    'ops:Data_File_Info.ops:file_size': '472320',
                    'ops:Data_File_Info.ops:md5_checksum': '6be3bc0237b72133682bde38161b40ba',
                    'ops:Data_File_Info.ops:mime_type': 'application/fits',
                    'ops:Label_File_Info.ops:blob': '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',
                    'ops:Label_File_Info.ops:creation_date_time': '2019-10-24T20:00:40Z',
                    'ops:Label_File_Info.ops:file_name': '20190321T204128S567_ovr_scil2.xml',
                    'ops:Label_File_Info.ops:file_ref': 'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204128S567_ovr_scil2.xml',
                    'ops:Label_File_Info.ops:file_size': '23633',
                    'ops:Label_File_Info.ops:md5_checksum': '8a814eb0227539941bcc11a57ed497ae',
                    'orex:spatial.orex:bennu_dec': '-1.49385634794811',
                    'orex:spatial.orex:bennu_ra': '177.462413140157',
                    'orex:spatial.orex:bennu_radec_quality': 'BEST: SPK',
                    'orex:spatial.orex:bennu_radec_target': 'BENNU',
                    'orex:spatial.orex:bore_angle': '1.10819138947643',
                    'orex:spatial.orex:bore_flag': '1',
                    'orex:spatial.orex:boresight_range': '3471.93929617945',
                    'orex:spatial.orex:boresight_x': '229.04362184104698',
                    'orex:spatial.orex:boresight_y': '104.03157207133602',
                    'orex:spatial.orex:boresight_z': '65.6625393485129',
                    'orex:spatial.orex:declination': '-2.41967425443514',
                    'orex:spatial.orex:emission_angle': '32.993490239933',
                    'orex:spatial.orex:fov_fill_factor': '1',
                    'orex:spatial.orex:fov_fill_flag': '1',
                    'orex:spatial.orex:incidence_angle': '39.468563569488296',
                    'orex:spatial.orex:latitude': '14.6288946565699',
                    'orex:spatial.orex:longitude': '24.427540289882902',
                    'orex:spatial.orex:phase_angle': '30.2826816709929',
                    'orex:spatial.orex:right_ascension': '176.852994999857',
                    'orex:spatial.orex:semimajor_axis': '16.617098932094002',
                    'orex:spatial.orex:semiminor_axis': '13.937276309720298',
                    'orex:spatial.orex:sun_range': '155969432.408299',
                    'orex:spatial.orex:target_range': '3.72245951665015',
                    'orex:time.orex:expo_ms': '910.2',
                    'orex:time.orex:exposure': '0.9102',
                    'orex:time.orex:mid_obs': '2019-03-21T20:41:28.567Z',
                    'orex:time.orex:mid_obs_et': '606472957.753112',
                    'orex:time.orex:mid_obs_sclk': '3/0606472849.35710',
                    'orex:time.orex:utc': '2019-03-21T20:41:28.423Z',
                    'pds:Array_2D.pds:axes': ['2', '2', '2', '2', '2'],
                    'pds:Array_2D.pds:axis_index_order': ['Last Index Fastest',
                                                          'Last Index Fastest',
                                                          'Last Index Fastest',
                                                          'Last Index Fastest',
                                                          'Last Index Fastest'],
                    'pds:Array_2D.pds:description': ['Quality indicator of the '
                                                     'calibrated frame.',
                                                     'Wavelengths of the '
                                                     'calibrated spectra.',
                                                     'Channel widths (FWHM) of the '
                                                     'spectral wavelength bins.',
                                                     'Wavelength offset due to '
                                                     'temperature dependence. The '
                                                     'wavelength correction is '
                                                     'absolute wavelength shift '
                                                     'per K difference from 115 K. '
                                                     'The shift is subtracted from '
                                                     'the center_wavelength. This '
                                                     'value may be very close to '
                                                     'zero.',
                                                     'Dark values subtracted from '
                                                     'L0 science product before '
                                                     'conversion to radiance.'],
                    'pds:Array_2D.pds:local_identifier': ['Quality',
                                                          'Center Wavelength',
                                                          'Channel Width',
                                                          'Temperature Dependence',
                                                          'cal_dark'],
                    'pds:Array_2D.pds:offset': ['92160',
                                                '138240',
                                                '220160',
                                                '302080',
                                                '388800'],
                    'pds:Array_2D_Spectrum.pds:axes': '2',
                    'pds:Array_2D_Spectrum.pds:axis_index_order': 'Last Index '
                                                                  'Fastest',
                    'pds:Array_2D_Spectrum.pds:description': 'OVIRS calibrated '
                                                             'spectral data. These '
                                                             'data are an array of '
                                                             'radiance values for '
                                                             'each super pixel '
                                                             'line in the ROI for '
                                                             'a single frame '
                                                             '(instrument '
                                                             'integration).',
                    'pds:Array_2D_Spectrum.pds:local_identifier': 'Calibrated',
                    'pds:Array_2D_Spectrum.pds:offset': '5760',
                    'pds:Axis_Array.pds:axis_name': ['Line',
                                                     'Sample',
                                                     'Line',
                                                     'Sample',
                                                     'Line',
                                                     'Sample',
                                                     'Line',
                                                     'Sample',
                                                     'Line',
                                                     'Sample',
                                                     'Line',
                                                     'Sample'],
                    'pds:Axis_Array.pds:elements': ['20',
                                                    '512',
                                                    '20',
                                                    '512',
                                                    '20',
                                                    '512',
                                                    '20',
                                                    '512',
                                                    '20',
                                                    '512',
                                                    '20',
                                                    '512'],
                    'pds:Axis_Array.pds:sequence_number': ['1',
                                                           '2',
                                                           '1',
                                                           '2',
                                                           '1',
                                                           '2',
                                                           '1',
                                                           '2',
                                                           '1',
                                                           '2',
                                                           '1',
                                                           '2'],
                    'pds:Element_Array.pds:data_type': ['IEEE754MSBDouble',
                                                        'SignedMSB4',
                                                        'IEEE754MSBDouble',
                                                        'IEEE754MSBDouble',
                                                        'IEEE754MSBDouble',
                                                        'IEEE754MSBDouble'],
                    'pds:Element_Array.pds:unit': ['W/cm**2/sr/µm',
                                                   'micrometer',
                                                   'micrometer',
                                                   'micrometer'],
                    'pds:File.pds:creation_date_time': '2019-10-23T19:05:39.752Z',
                    'pds:File.pds:file_name': '20190321T204128S567_ovr_scil2.fits',
                    'pds:File.pds:file_size': '472320',
                    'pds:Header.pds:object_length': ['5760',
                                                     '2880',
                                                     '2880',
                                                     '2880'],
                    'pds:Header.pds:offset': ['0', '89280', '135360', '385920'],
                    'pds:Header.pds:parsing_standard_id': ['FITS 3.0',
                                                           'FITS 3.0',
                                                           'FITS 3.0',
                                                           'FITS 3.0'],
                    'pds:Identification_Area.pds:information_model_version': '1.7.0.0',
                    'pds:Identification_Area.pds:logical_identifier': 'urn:nasa:pds:orex.ovirs:data_calibrated:20190321t204128s567_ovr_scil2.fits',
                    'pds:Identification_Area.pds:product_class': 'Product_Observational',
                    'pds:Identification_Area.pds:title': 'OSIRIS-REx OVIRS '
                                                         'Calibrated Science Data '
                                                         'Product (L2) '
                                                         '2019-03-21T20:41:28.567Z',
                    'pds:Identification_Area.pds:version_id': '1.0',
                    'pds:Internal_Reference.pds:comment': ['Radiometric '
                                                           'calibration file used '
                                                           'in processing. The '
                                                           'file can be found in '
                                                           'the OVIRS calibration '
                                                           'collection.',
                                                           'Out of band '
                                                           'calibration file used '
                                                           'in processing. The '
                                                           'file can be found in '
                                                           'the OVIRS calibration '
                                                           'collection.',
                                                           'Bad pixel map '
                                                           'calibration file used '
                                                           'in processing. The '
                                                           'file can be found in '
                                                           'the OVIRS calibration '
                                                           'collection.'],
                    'pds:Internal_Reference.pds:lid_reference': ['urn:nasa:pds:context:investigation:mission.orex',
                                                                 'urn:nasa:pds:context:instrument_host:spacecraft.orex',
                                                                 'urn:nasa:pds:context:instrument:ovirs.orex',
                                                                 'urn:nasa:pds:context:target:asteroid.101955_bennu'],
                    'pds:Internal_Reference.pds:lidvid_reference': ['urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_rad_20010101t000000_20500101t000000_v001.fits::1.0',
                                                                    'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_oob_20010101t000000_20500101t000000_v002.fits::1.0',
                                                                    'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_bpm_20170808t000000_20500101t000000_v002.fits::1.0'],
                    'pds:Internal_Reference.pds:reference_type': ['data_to_investigation',
                                                                  'is_instrument_host',
                                                                  'is_instrument',
                                                                  'data_to_target',
                                                                  'data_to_calibration_product',
                                                                  'data_to_calibration_product',
                                                                  'data_to_calibration_product'],
                    'pds:Investigation_Area.pds:name': 'OSIRIS-REx',
                    'pds:Investigation_Area.pds:type': 'Mission',
                    'pds:Local_Internal_Reference.pds:local_identifier_reference': ['Calibrated',
                                                                                    'Quality',
                                                                                    'Center '
                                                                                    'Wavelength',
                                                                                    'Channel '
                                                                                    'Width',
                                                                                    'Temperature '
                                                                                    'Dependence',
                                                                                    'cal_dark',
                                                                                    'Calibrated',
                                                                                    'Center '
                                                                                    'Wavelength',
                                                                                    'Channel '
                                                                                    'Width'],
                    'pds:Local_Internal_Reference.pds:local_reference_type': ['display_settings_to_array',
                                                                              'display_settings_to_array',
                                                                              'display_settings_to_array',
                                                                              'display_settings_to_array',
                                                                              'display_settings_to_array',
                                                                              'display_settings_to_array',
                                                                              'spectral_characteristics_to_array_object',
                                                                              'spectral_characteristics_to_bin_center_values',
                                                                              'spectral_characteristics_to_bin_width_values'],
                    'pds:Modification_Detail.pds:description': 'Initial version.',
                    'pds:Modification_Detail.pds:modification_date': '2019-02-01T00:00:00Z',
                    'pds:Modification_Detail.pds:version_id': '1.0',
                    'pds:Observing_System.pds:name': 'OSIRIS-REx Visible and '
                                                     'InfraRed Spectrometer '
                                                     '(OVIRS)',
                    'pds:Observing_System_Component.pds:description': 'Origins, '
                                                                      'Spectral '
                                                                      'Interpretation, '
                                                                      'Resource '
                                                                      'Identification, '
                                                                      'Security - '
                                                                      'Regolith '
                                                                      'Explorer '
                                                                      'Spacecraft',
                    'pds:Observing_System_Component.pds:name': ['OSIRIS-REx',
                                                                'OVIRS'],
                    'pds:Observing_System_Component.pds:type': ['Spacecraft',
                                                                'Instrument'],
                    'pds:Primary_Result_Summary.pds:processing_level': 'Calibrated',
                    'pds:Primary_Result_Summary.pds:purpose': 'Science',
                    'pds:Target_Identification.pds:alternate_designation': '1999 '
                                                                           'RQ36',
                    'pds:Target_Identification.pds:name': '(101955) BENNU',
                    'pds:Target_Identification.pds:type': 'Asteroid',
                    'pds:Time_Coordinates.pds:start_date_time': '2019-03-21T20:41:28.567Z',
                    'pds:Time_Coordinates.pds:stop_date_time': '2019-03-21T20:41:28.567Z',
                    'product_class': 'Product_Observational',
                    'ref_lid_instrument': 'urn:nasa:pds:context:instrument:ovirs.orex',
                    'ref_lid_instrument_host': 'urn:nasa:pds:context:instrument_host:spacecraft.orex',
                    'ref_lid_investigation': 'urn:nasa:pds:context:investigation:mission.orex',
                    'ref_lid_product': ['urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_bpm_20170808t000000_20500101t000000_v002.fits',
                                        'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_oob_20010101t000000_20500101t000000_v002.fits',
                                        'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_rad_20010101t000000_20500101t000000_v001.fits'],
                    'ref_lid_target': 'urn:nasa:pds:context:target:asteroid.101955_bennu',
                    'ref_lidvid_product': ['urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_bpm_20170808t000000_20500101t000000_v002.fits::1.0',
                                           'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_oob_20010101t000000_20500101t000000_v002.fits::1.0',
                                           'urn:nasa:pds:orex.ovirs:calibration:ovirs_s1a_rad_20010101t000000_20500101t000000_v001.fits::1.0'],
                    'sp:Bin_Description.sp:bin_profile_description': 'The OVIRS '
                                                                     'calibrated '
                                                                     'spectrum '
                                                                     'wavelength '
                                                                     'binning is '
                                                                     'described by '
                                                                     'the three '
                                                                     '2d_Array '
                                                                     'structures '
                                                                     'labeled as '
                                                                     'Center_Wavelength, '
                                                                     'Channel_width '
                                                                     'and '
                                                                     'Temperature '
                                                                     'Dependance. '
                                                                     'Center_Wavelength '
                                                                     'is a 512 '
                                                                     'element '
                                                                     'array that '
                                                                     'give the '
                                                                     'channel '
                                                                     'center '
                                                                     'wavelength '
                                                                     'in units of '
                                                                     'micrometer, '
                                                                     'Channel_Width '
                                                                     'is also a '
                                                                     '512 element '
                                                                     'array that '
                                                                     'gives the '
                                                                     'width (FWHM) '
                                                                     'of each '
                                                                     'channel in '
                                                                     'micrometers. '
                                                                     'Temperature '
                                                                     'Dependence '
                                                                     'is a '
                                                                     'temperature '
                                                                     'dependent '
                                                                     'correction '
                                                                     'to the '
                                                                     'Center_Wavelength. '
                                                                     'It is '
                                                                     'applied as '
                                                                     'an absolute '
                                                                     'wavelength '
                                                                     'shift per K '
                                                                     'from 115 K. '
                                                                     'The shift is '
                                                                     'subtracted '
                                                                     'from the '
                                                                     'wavelength. '
                                                                     'Center_Wavelength '
                                                                     'element 1 '
                                                                     'corresponds '
                                                                     'to '
                                                                     'Channel_Width '
                                                                     'element 1 '
                                                                     'and '
                                                                     'Temperature '
                                                                     'Dependence '
                                                                     'element 1',
                    'sp:Circular_FOV.sp:diameter_angle': '4',
                    'sp:Field_of_View.sp:description': 'The OSIRIS-REx Visible and '
                                                       'IR Spectrometer (OVIRS) is '
                                                       'a point spectrometer with '
                                                       'a 4-mrad\xa0diameter '
                                                       'circular field of view '
                                                       '(FOV) that provides '
                                                       'spectra over the '
                                                       'wavelength range of '
                                                       '0.4–4.3 μm\xa0(25,000–2300 '
                                                       'cm–1).',
                    'sp:Observation_Parameters.sp:net_integration_time': '1.2',
                    'sp:Observation_Parameters.sp:number_of_exposures': '1',
                    'sp:Observation_Parameters.sp:resolution_limit_wavelength': '0.4',
                    'sp:Spectral_Characteristics.sp:spectral_bin_type': 'wavelength',
                    'sp:Spectral_Characteristics.sp:spectrum_format': '2D',
                    'title': 'OSIRIS-REx OVIRS Calibrated Science Data Product '
                             '(L2) 2019-03-21T20:41:28.567Z',
                    'vid': '1.0'},
     'start_date_time': '2019-03-21T20:41:28.567Z',
     'stop_date_time': '2019-03-21T20:41:28.567Z',
     'targets': [{'description': None,
                  'href': 'https://pds-gamma.jpl.nasa.gov/products/urn:nasa:pds:context:target:asteroid.101955_bennu',
                  'id': 'urn:nasa:pds:context:target:asteroid.101955_bennu',
                  'title': None,
                  'type': None}],
     'title': 'OSIRIS-REx OVIRS Calibrated Science Data Product (L2) '
              '2019-03-21T20:41:28.567Z',
     'type': 'Product_Observational'}


### Get the file path of the data


```python
product.properties['ops:Data_File_Info.ops:file_ref']
```




    'https://pds-gamma.jpl.nasa.gov/data/pds4/test-data/registry/orex.ovirs/data_calibrated/bennu_original_calibration/detailed_survey/20190321T204128S567_ovr_scil2.fits'


