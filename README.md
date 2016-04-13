# AutoFallOff
Spectrometer fall off data acquisition automation

[![Travis Build Status](https://travis-ci.org/WasatchPhotonics/AutoFallOff.svg?branch=master)](https://travis-ci.org/WasatchPhotonics/AutoFallOff?branch=master)
[![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/1e1be5jy0m3qchq9?svg=true)](https://ci.appveyor.com/project/NathanHarrington/autofalloff)
[![Coverage Status](https://coveralls.io/repos/github/WasatchPhotonics/AutoFallOff/badge.svg?branch=master)](https://coveralls.io/github/WasatchPhotonics/AutoFallOff?branch=master)

Communicate with zaber stage and custom shutter controller. Acquire,
display and store data from Wasatch Photonics Cobra series of
spectrometers. Provide visual feedback for stage position, processing
progress and fall off curve collection procedures.


Environment setup instructions

    On Windows 7, install Miniconda-latest-Windows-x86_64
    (Using windows command prompt, as there appears to still be issues
    using conda in bash as part of the git for windows install)
    conda update conda
    conda --version (4.0.5 for these instructions)
    conda create --name autofalloff_conda pyside numpy pytest
    activate autofalloff_conda
    python setup.py develop

    
