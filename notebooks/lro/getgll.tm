KPL/MK

   This meta-kernel is used for a test case for pyWWT.
   Galileo ephemeris information as well as magnetometer data is
   utilized to visualize the spacecrafts orbit about jupiter 
   using pyWWT.

   The names and contents of the kernels referenced by this
   meta-kernel are as follows:

   File name                   Contents
   --------------------------  -----------------------------
   naif0008.tls                Generic LSK
   981005_PLTEPH-DE405S.bsp    Solar System Ephemeris
   gll_951120_021126_raj2021.bsp   Galileo Spacecraft SPK


   \begindata
   KERNELS_TO_LOAD = ( 'kernels/lsk/naif0008.tls',
                       'kernels/spk/981005_PLTEPH-DE405S.bsp',
                       'kernels/spk/gll_951120_021126_raj2021.bsp' )
   \begintext