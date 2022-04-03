#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os

def run(dirs):
 dest = "/Users/macadmin/Education/Test_Backup"
 subprocess.call(["rsync", "-arq", dirs, dest])

if __name__ == "__main__":
 src = "/Users/macadmin/Education/Test/"
 for root, dirs, files in os.walk(src):
     print(dirs)
     #p = Pool(len(dirs))
     #p.map(run, dirs)