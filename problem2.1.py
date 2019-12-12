import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd

def trim(s):
    s = s[1:-2]
    tup = ()
    s=s.split(",")
    return (float(s[0]),float(s[1]),str(s[2][3:-1]),str(s[3][3:-1]),str(s[4][3:-1]),int(s[5][3:-1]))

def toCsv(num = 100):
    arr = [[],[],[],[],[],[]] # lat ,lon, date ,manufacturer, model, deviceId
    data = readFile(num)
    for l in data:
        for i in range(6):
            arr[i].append(l[i])
    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'lat': arr[0], 'long': arr[1], 'date': arr[2], 'manufacturer': arr[3], 'model': arr[4], 'deviceId': arr[5]})

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv("test1000.csv", index=False, sep=',')

def readFile(num):
    file = open("part-00000", 'r')
    data = []
    i=0;
    l = file.readline();
    if num > 0:
        while l and i < num:
            i += 1
            data.append(trim(l))
            print(trim(l))
            l = file.readline()
    else:
        while l:
            i += 1
            data.append(trim(l))
            print(trim(l))
            l = file.readline()
    file.close()

    return data


toCsv(1000)
