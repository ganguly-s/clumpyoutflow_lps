## Description

Use [plotter.py](plotter.py) to plot line profile figures similar to those available in our paper: [On Synthetic Absorption Line Profiles of Thermally Driven Winds from Active Galactic Nuclei] (https://arxiv.org/abs/2103.06497).

Our Athena++ generated outflow models comprise of steady to thermally unstable wind solutions. We use photoionization models of XSTAR to compute synthetic absorption line profiles of such systems. We have analysed profiles for 25 ions, for steady wind models A21, B and C and clumpy cases of models B and C, namely models B-c and C-c. The [FITS files](lps_fits_files/), containing normalized flux with absorption profiles for each ion along with their Doppler-shifted velocities, wavelength, optical depth, etc. have been made available through this public repository, for direct comparison with observations. Future X-ray missions like ATHENA and XRISM, may hold the key to testing our models accurately.

## Usage

Similar to Figures. 8, 14 and 15 in our paper, one can plot the line profiles for our different models and our entire list of ions using [this code](plotter.py).
**Note:** The model selection determines the path to the FITS files, subject to some adjustment required in the path name.
