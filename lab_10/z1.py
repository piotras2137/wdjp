import os 
def mkdirs(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

paths = ["folder", "aaaa", "xd"]

mkdirs(paths)