import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd

def trim(s):

    s=s.split("\t")
    # return s
    return (float(s[0]),float(s[1]),int(s[2][0:-1]))

def toCsv(num = -1):
    arr = [[],[],[]] # lat ,lon, ID
    data = readFile(num)
    for l in data:
        for i in range(3):
            arr[i].append(l[i])
    dataframe = pd.DataFrame({'lat': arr[0], 'long': arr[1], 'ID': arr[2]})
    dataframe.to_csv("geo.csv", index=False, sep=',')

def readFile(num):
    file = open("sample_geo.txt", 'r')
    data = []
    i=0
    l = file.readline()
    if num > 0:
        while l and i < num:
            i += 1
            if len(l) == 1:
                continue
            data.append(trim(l))
            print(trim(l))
            l = file.readline()
    else:
        while l:
            i += 1
            if len(l) == 1:
                l = file.readline()
                continue
            data.append(trim(l))
            print(trim(l))
            l = file.readline()
    file.close()

    return data


toCsv()
# print(readFile(-1))