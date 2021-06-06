import csv
import pandas as pd
import plotly.express as px
import math
import numpy as np

def getDataSource(dataPath):
    percentage=[]
    daysPresent=[]

    with open(dataPath,encoding='utf8') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        
        for row in csv_reader:
            percentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    
    return {"x":percentage,"y":daysPresent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between percentage and days present",correlation[0,1])

def setUp():
    dataPath="Project106/data.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setUp()