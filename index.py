import os
rootdir = "./images"

for subdir, dirs, files in os.walk(rootdir):
  for file in files:
    print (os.path.join(subdir, file))