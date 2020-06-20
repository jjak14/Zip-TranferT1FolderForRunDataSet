# I'm trying here a totally different approach to the initial one

# This program or script zip the T1 folder and save the zip file in houfile5
# The program then copy the content of the MRK folder folder to the resource folder in Houfile5
# The script is run from a specific position and discover the path itself

# Import all the necessary libraries
import shutil
import os
import zipfile
from pathlib import Path

# Obtaining and storing the current directory, Project Number and LineName
currentdir = Path.cwd()
currentdir = str(currentdir)
projNum = currentdir[9:14]
LineName = currentdir[15:23]


# Build destination directory for T1.zip
t1zipdestination =  'C:/Houfile5/Execution/' + LineName + '/DryTest/'
# Current T1 location
t1loc = Path('C:/Proj0/' + projNum + '/' + LineName + '/CBG/T1')
# Create the destination folder for T1.zip
os.makedirs(t1zipdestination)

# Zip the T1 folder
zip_file = zipfile.ZipFile('T1.zip', 'w')
zip_file.write(t1loc, compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()

# Move T.zip to Houfile5
t1loc = 'C:/Proj0/' + projNum + '/' + LineName + '/CBG/T1'
sourceT = t1loc + '.zip'
DestT = t1zipdestination
shutil.move(sourceT, DestT)
