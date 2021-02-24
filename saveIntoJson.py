import json
import io,os
from datetime import datetime
import pandas


file_path = 'numberPlateStore/nbPltStore.json'
convToDic= {}

def writeToFile (path, data):
    with open(path, "a") as f:
        json.dump(data, f)
        


def parseData(dics):
    now = datetime.now()
    convToDic['date'] = now.strftime("%Y/%m/%d")
    convToDic['time'] = now.strftime("%H:%M:%S")
    convToDic['locale'] = dics['locale'][0]
    convToDic['nbplt'] = dics['description'][0]
    writeToFile(file_path, convToDic)