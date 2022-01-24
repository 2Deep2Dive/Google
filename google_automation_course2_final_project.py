#!/usr/bin/env python3
import re
import sys
import os
import operator

from unittest import result

logfile = sys.argv[1]

def get_errors(logfile):
    error = {}
    per_user = {}
    errorPattern =  r"(.*)(ERROR): ([a-zA-Z ]*)(.*)\(([\w.]+)\)"   #r"ticky: ERROR: ([\w ]*)"
    infoPattern = r"(.*)(INFO): ([a-zA-Z ]*)(.*)\(([\w.]+)\)"
    with open(logfile) as file:
        for line in file:
            if "ticky: ERROR:" in line :
                errorResult = re.search(errorPattern, line)
                if (errorResult[3]) not in error:
                    error[errorResult[3]] = 0
                else:
                    error[errorResult[3]] += 1    
            elif "ticky: INFO:" in line:
                infoResult = re.search(infoPattern, line)
                if (infoResult[5]) not in per_user:
                    per_user[infoResult[5]] = 0
                else:    
                    per_user[infoResult[5]] += 1
            else:
                continue
        file.close()
        sortedError = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
        sortedPerUser = sorted(per_user.items())
    return print(sortedError), print(sortedPerUser)

def get_results(logfile):
    error = {}
    per_user = {}
    Pattern =  r"(.*)(ERROR|INFO): ([a-zA-Z ]*)(.*)\(([\w.]+)\)"
    with open(logfile) as file:
        for line in file:
                result = re.search(Pattern, line)
                if(result[2] == "ERROR"):
                    print(result[2])
                    if (result[3]) not in error:
                        error[result[3]] = 1
                    else:
                        error[result[3]] += 1
                    if (result[5]) not in per_user:
                        per_user[result[5]] = {}
                        per_user[result[5]][result[2]] = 1 
                    else:
                        per_user[result[5]][result[2]] += 1    
                elif (result[2] == "INFO"):
                    print(result[2])
                    if (result[5] not in per_user):
                        per_user[result[5]] = {}
                        per_user[result[5]][result[2]] = 1
                    else:
                        per_user[result[5]][result[2]] += 1
                else:
                    continue
        file.close()
        sortedError = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
        sortedPerUser = sorted(per_user.items())
    return print(sortedError), print(sortedPerUser)

get_results(logfile)
