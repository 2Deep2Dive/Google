#!/usr/bin/env python3
import re
import sys
import os
from unittest import result

logfile = sys.argv[1]

def get_error_messages(logfile):
    erros = {}
    per_user = {}
    errorPattern =  r"(.*)(ERROR): ([a-zA-Z ]*)(.*)\(([a-z]+)\)"   #r"ticky: ERROR: ([\w ]*)"
    infoPattern = r"(.*)(INFO): ([a-zA-Z ]*)(.*)\(([a-z]+)\)"
    try:
        with open(logfile) as file:
            for line in file:
                if "ticky: INFO: [\w ]*)" in line :
                    result = re.search(errorPattern, line)

                else:
                    continue
            file.close()
    except:
        print("Error")
get_error_messages(logfile)
