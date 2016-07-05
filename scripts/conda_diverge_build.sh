# As of 20160701 appveyor conda and conda on a windows 7 machine 
# required different processes for application building.
#
# The appveyor.yml file contains the correct steps for appveyor.
# This file documents the steps needed for a conda build on a 
# windows 7 machine:
# Here is the conda list output of the result of build:
# appveyor-conda-build 6bcab781 on appveyor:
#
# packages in environment at C:\Miniconda\envs\autofalloff_conda:
#
#bzip2                     1.0.6                     vc9_3  [vc9]
#distribute                0.6.45                   py27_1  
#freetype                  2.5.5                     vc9_1  [vc9]
#future                    0.15.2                    <pip>
#jpeg                      8d                        vc9_0  [vc9]
#libpng                    1.6.22                    vc9_0  [vc9]
#libtiff                   4.0.6                     vc9_2  [vc9]
#mkl                       11.3.3                        1  
#numpy                     1.11.1                   py27_0  
#openssl                   1.0.2h                    vc9_0  [vc9]
#pefile                    2016.3.28                 <pip>
#pillow                    3.2.0                    py27_1  
#pip                       8.1.2                    py27_0  
#PyInstaller               3.2                       <pip>
#pyqt                      4.11.4                   py27_6  
#pyqtgraph                 0.9.10                   py27_1  
#pyserial                  2.7                      py27_0  
#pyside                    1.2.1                    py27_0  
#python                    2.7.12                        0  
#pywin32                   220                      py27_1  
#qt                        4.8.7                     vc9_8  [vc9]
#setuptools                23.0.0                   py27_0  
#sip                       4.16.9                   py27_2  
#six                       1.10.0                   py27_0  
#vs2008_runtime            9.00.30729.1                  2  
#wheel                     0.29.0                   py27_0  
#zlib                      1.2.8                     vc9_3  [vc9]



# Based heavily on:
# http://tjelvarolsson.com/blog/how-to-continuously-test-your-python-code-on-windows-using-appveyor/

"python --version"
"python -c \"import struct; print(struct.calcsize('P') * 8)\""

# If you run this on windows it will break your conda installation
#- conda update -q conda
conda info -a

conda config --set always_yes yes
conda create --name autofalloff_conda pyside
activate autofalloff_conda

conda remove setuptools
conda remove distribute

# Pre-requisite for pyinstaller
conda install pywin32

# No conda packages for these:
pip install pefile
pip install pyinstaller


conda install numpy
conda install pyside
conda install six
conda install distribute
conda install pillow
conda install pyqtgraph
conda install pyserial

# This will create the following from conda list:

#bzip2                     1.0.6                     vc9_3  [vc9]
#distribute                0.6.45                   py27_1
#freetype                  2.5.5                     vc9_1  [vc9]
#jpeg                      8d                        vc9_0  [vc9]
#libpng                    1.6.22                    vc9_0  [vc9]
#libtiff                   4.0.6                     vc9_2  [vc9]
#mkl                       11.3.3                        1
#numpy                     1.11.1                   py27_0
#openssl                   1.0.2h                    vc9_0  [vc9]
#pillow                    3.2.0                    py27_1
#pip                       1.4.1                    py27_1
#pyqt                      4.11.4                   py27_6
#pyqtgraph                 0.9.10                   py27_1
#pyserial                  2.7                      py27_0
#pyside                    1.2.1                    py27_0
#python                    2.7.12                        0
#pywin32                   220                      py27_1
#qt                        4.8.7                     vc9_8  [vc9]
#setuptools                23.0.0                   py27_0
#sip                       4.16.9                   py27_2
#six                       1.10.0                   py27_0
#vs2008_runtime            9.00.30729.1                  2
#wheel                     0.29.0                   py27_0
#zlib                      1.2.8                     vc9_3  [vc9]


# The acceptance test for any changes to this script is that the 
# pyinstaller command below will run, build the application, which is
# then pacakged by innosetup. Running the installation should install
# the program on a windows machine, then the user works with the
# application.

pyinstaller 
  --clean 
  --windowed 
  --distpath=scripts/built-dist
  --workpath=scripts/work-path
  --noconfirm 
  --specpath scripts scripts/AutoFallOff.py

#!/bin/bash
#
# Run supporting pyrcc files to generate resource files and future
# designer conversions into python code. Run this from the home project
# directory like:
# <project root> $ ./scripts/rebuild_resources.sh

CMD_NAME="pyside-rcc"
UIC_NAME="pyside-uic"


if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    echo "Windows detected"
    CMD_NAME="C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe"
    UIC_NAME="C:\Python27\Lib\site-packages\PySide\pyside-uic.exe"
    if [ ! -e $UIC_NAME ]
    then
        echo "git-bash pyside-uic.exe with no prefix instead"
        UIC_NAME="pyside-uic.exe"
    fi
fi

echo "Rebuilding resources file"

# Use the relative package name glob so the build is portable across
# other projects
#$CMD_NAME \
#    */assets/resources.qrc \
#    -o */assets/resources_rc.py

# Process all of the QRC Files
for QRC_FILE in */assets/*.qrc;
    do echo "QRC Processing $QRC_FILE";

    PREFIX=$(echo $QRC_FILE | cut -d '.' -f 1)
    DEST_RC=${PREFIX}_rc.py
    $CMD_NAME $QRC_FILE -o $DEST_RC

done

for UIC_FILE in */assets/*.ui;
    do echo "UIC Processing $UIC_FILE";

    PREFIX=$(echo $UIC_FILE | cut -d '.' -f 1)
    DEST_PY=${PREFIX}.py
    $UIC_NAME  $UIC_FILE  -o $DEST_PY

done

