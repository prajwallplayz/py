import os
import shutil


path="c:/python/class 3"

print("before copy")
print(os.listdir(path))
source='c:/python/class 3/abc/abc.txt'
destination='c:/python/class 3/abc.txt'
dest=shutil.copy(source,destination)
print("after copy")
print(dest)
print(os.listdir(path))