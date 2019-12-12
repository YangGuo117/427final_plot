import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd

def trim(s):

    s=s.split(" ")
    # return s
    return (float(s[0]),float(s[1]),str(s[2][0:-1]))

def toCsv(num = -1):
    arr = [[],[],[]] # lat ,lon, ID
    data = readFile(num)
    for l in data:
        if (l[0] >= 25 and l[0] <= 49) and (l[1] >= -130 and l[1] <= - 70) :
            for i in range(3):
                arr[i].append(l[i])
    dataframe = pd.DataFrame({'lat': arr[0], 'long': arr[1], 'URL': arr[2]})
    dataframe.to_csv("geoLarge.csv", index=False, sep=',')

def readFile(num):
    file = open("lat_longs", 'r')
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
# print(readFile(1000))