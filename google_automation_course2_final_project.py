#!/usr/bin/env python3
import re
import sys
import os
import operator

from unittest import result

logfile = sys.argv[1]

def get_results(logfile):
    error = {}
    per_user = {}
    Pattern =  r"(.*)(ERROR|INFO): ([a-zA-Z ]*)(.*)\(([\w.]+)\)"
    with open(logfile) as file:
        for line in file:
                result = re.search(Pattern, line)
                if(result[2] == "ERROR"):
                    if (result[3]) not in error:
                        error[result[3]] = 1
                    else:
                        error[result[3]] += 1
                    if (result[5]) not in per_user:
                        per_user[result[5]] = {}
                    if (result[2]) not in per_user[result[5]]:
                        per_user[result[5]][result[2]] = 1
                    else:
                        per_user[result[5]][result[2]] += 1   
                elif (result[2] == "INFO"):
                    if (result[5] not in per_user):
                        per_user[result[5]] = {}
                    if (result[2]) not in per_user[result[5]]:
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