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

Follow the instructions line by line in appveyor.yml, this will give you
on linux the output of condat --list:

distribute                0.6.45                   py27_1  
freetype                  2.5.5                         1  
future                    0.15.2                    <pip>
jbig                      2.1                           0  
jpeg                      8d                            2  
libpng                    1.6.22                        0  
libtiff                   4.0.6                         2  
mkl                       11.3.3                        0  
numpy                     1.11.2                   py27_0  
openssl                   1.0.2j                        0  
pefile                    2016.3.28                 <pip>
pillow                    3.4.2                    py27_0  
pip                       8.1.2                    py27_0  
PyInstaller               3.2                       <pip>
pyqt                      4.10.4                   py27_0  
pyqtgraph                 0.9.10                   py27_1  
pyserial                  2.7                      py27_0  
pyside                    1.2.1                    py27_1  
python                    2.7.12                        1  
qt                        4.8.5                         0  
readline                  6.2                           2  
setuptools                27.2.0                   py27_0  
shiboken                  1.2.1                    py27_0  
sip                       4.15.5                   py27_0  
six                       1.10.0                   py27_0  
sqlite                    3.13.0                        0  
tk                        8.5.18                        0  
wheel                     0.29.0                   py27_0  
xz                        5.2.2                         0  
zlib                      1.2.8                         3  



Then run python setup.py develop to pull in py.test, etc.


Fedora Core 24 setup:

    sudo dnf -y libjpeg-devel libX11-devel
