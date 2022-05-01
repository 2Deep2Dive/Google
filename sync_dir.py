
  #!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os



def run(list):
 dest = "/home/student-00-02a34070697f/data/prod_backup/"
 subprocess.call(["rsync", "-arqb", list, dest])

if __name__ == "__main__":
 src = "/home/student-00-02a34070697f/data/prod"
 list = []
 for root, dirs, files in os.walk(src):
     for name in dirs:
         list.append(os.path.join(root, name))
 p = Pool(len(list))
 p.map(run, list)