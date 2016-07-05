@echo off
python --version
python -c "import struct; print(struct.calcsize('P') * 8)"

call deactivate
conda remove --name autofalloff_conda --all

conda info -a

conda config --set always_yes yes
conda create --name autofalloff_conda pyside
call activate autofalloff_conda

conda remove setuptools

conda install numpy

conda install pywin32 

REM Pre-requisite for pyinstaller
conda install pywin32

REM This branching is based on:
REM http://stackoverflow.com/questions/1164049/batch-files-error-handling

REM Kludge to ignore pefile "being used by another process"
call pip install pefile && (
 	echo "THe pefile command has succeeded"
	(call )
) || (
	echo "failure in pe file command %ERRORLEVEL%"
	(call )
)

conda install pyside
conda install six
conda install distribute
conda install pillow
conda install pyqtgraph
conda install pyserial

REM attempting to install pyinstaller with distribute shows a version issue.
conda remove distribute

REM Kludge to ignore pyinstaller "being used by another process"
call pip install pyinstaller && (
	echo "The pyinstaller command has succeeded"
	(call )
) || (
	echo "Failure in pyinstaller pip command %ERRORLEVEL%"
)

REM Add distribute back in
conda install distribute

conda install future
conda list

python setup.py develop

pyinstaller^
  --clean^
  --windowed^
  --distpath=scripts/built-dist^
  --workpath=scripts/work-path^
  --noconfirm^
  --specpath scripts scripts/AutoFallOff.py
