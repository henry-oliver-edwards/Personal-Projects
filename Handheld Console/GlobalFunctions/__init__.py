#Globally important functions called by many other scripts
import os

def Find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)