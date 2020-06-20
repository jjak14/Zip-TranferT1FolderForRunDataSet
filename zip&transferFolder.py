# This program or script zip the T1 folder and save the zip file in houfile5
# The program then copy the content of the MRK folder to the resource folder in Houfile5

# Import all the necessary libraries
import zlib
import shutil
import os
import os.path
import zipfile
from pathlib import Path  

# Ask user to enter the project number
# Test that the project number is 5 digits ask user to correct if not
while True:
    print('Enter Project Number: ')
    projectnum = input()
    try:
        projectnum = int(projectnum)
    except:
        print('Please use numeric digits.')
        continue
    if len(str(projectnum)) < 5 or len(str(projectnum)) > 6:
        print('The project number should be 5 digits !')
        continue
    break

# Ask user to enter line name
# Test that linename is 8 characters long and first 2 characters are numbers
while True:
    print('Enter Line Name: ')
    linename = input()
    try:
        initlinename = int(linename[0] + linename[1])
    except:
        print('The project number should be 8 characters the first two being digits !')
        continue
    if len(str(linename)) < 8 or len(str(linename)) > 8:
        print('The project number should be 8 characters the first two being digits !')
        continue
    break

# Ask user to enter technology
while True:
    print('Enter Tool technology: ')
    TechName = input()
    try:
        TechName = int(TechName)
    except:
        try:
            TechName = str(TechName)
            TechName = TechName.upper()
        except:
            continue
        if TechName == 'CBG' or TechName == 'BMD' or TechName == 'CDG' or TechName == 'BMG' or TechName == 'CDP':
            break
        else:
            print('Technology should be 3 letters. i.e: CBG, BMD, CDP, ...')
            continue
    print('Invalid technology entered.')

# store T1 path
t1source = 'C:/Proj0/' + str(projectnum) + '/' + linename + '/CBG/T1'
print('folder to be zipped is here')
print(Path(t1source))
print('\n')

# Build destination directory for T1.zip
t1dest = 'C:/Houfile5/Execution/' + linename + '/DryTest/'
print('zipped folder to be moved here')
print(Path(t1dest))
print('\n')

# Compress T1 foldeer in zip file
print('creating archive\n')

os.chdir(os.path.dirname(t1source))
with zipfile.ZipFile(t1source + '.zip',
                     "w",
                     zipfile.ZIP_DEFLATED,
                     allowZip64=True) as zf:
    for root, _, filenames in os.walk(os.path.basename(t1source)):
        for name in filenames:
            name = os.path.join(root, name)
            name = os.path.normpath(name)
            zf.write(name, name)

# Create the destination folder for T1.zip
print('Creating Drytest Folder to destination\n')
os.makedirs(t1dest)

# Move T1.zip to Houfile5
print('Moving T1.zip from source to destination\n')
shutil.move(t1source + '.zip', t1dest)
