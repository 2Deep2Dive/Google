#!/usr/bin/env python3
import re
import os
import csv
import sys
import operator

from unittest import result

logfile = sys.argv[1]

def dict_to_list(dict):
    list_from_dict = []
    for k1,d in dict.items():
        key = k1
        for k2,v in d.items():
            subKey = k2
            value  = v
        list_from_dict.append(tuple((key,subKey,value)))
    return list_from_dict

def list_to_csv(fileName, list):
    with open(fileName, 'w',newline='') as csv_File:
        writer = csv.writer(csv_File)
        writer.writerows(list)
    csv_File.close()
    return

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
    sortedError   = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    sortedPerUser = sorted(dict_to_list(per_user))
    sortedError.insert(0, tuple(("Error", "Count")))
    sortedPerUser.insert(0,tuple(("Username", "INFO", "ERROR")))
    list_to_csv("error_message.csv",sortedError)
    list_to_csv("user_statistics.csv",sortedPerUser)
    return

get_results(logfile)