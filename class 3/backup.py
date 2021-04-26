import os
import shutil

source=input('enter the path')
destination=input('enter the path')
#source=source+
#destination=destination+
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)