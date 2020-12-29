import pandas as pd
import numpy as np
import os, json

SOURCE_FILE = os.path.join(".", "hierarchy_case_20May2020.csv")
DESCINATION_FILE = os.path.join(".", "output.json")

CEO_BOSS = "none"


class Person:
    def __init__(self, EMPLOYEE_ID, DESIGNATION, DEPARTMENT, NAME, MANAGER_EMPLOYEE_ID):
        self.EMPLOYEE_ID = EMPLOYEE_ID
        self.DESIGNATION = DESIGNATION
        self.DEPARTMENT = DEPARTMENT
        self.NAME = NAME
        self.MANAGER_EMPLOYEE_ID = MANAGER_EMPLOYEE_ID
        self.reportees = []
    
    def generateTree(self):
        respTree = dict()
        respTree['EMPLOYEE_ID'] = self.EMPLOYEE_ID
        respTree['NAME'] = self.NAME
        respTree['reportees'] = self.reportees

        for index in range(len(respTree['reportees'])):
            respTree['reportees'][index] = respTree['reportees'][index].generateTree()

        return respTree


if __name__ == "__main__":
    readFile = pd.read_csv(SOURCE_FILE)
    readFile["MANAGER_EMPLOYEE_ID"].fillna(CEO_BOSS, inplace=True)
    count = len(readFile)

    readData = list()

    for i in range(count):
        readData.append(
            Person(
                readFile["EMPLOYEE_ID"][i],
                readFile["DESIGNATION"][i],
                readFile["DEPARTMENT"][i],
                readFile["NAME"][i],
                readFile["MANAGER_EMPLOYEE_ID"][i],
            )
        )

    # ==== dict to store the hirarchy ====
    hirarchy = list()

    tempIds = []

    for item in readData:
        if item.MANAGER_EMPLOYEE_ID == CEO_BOSS:
            tempIds.append([item])
    count -= 1
    
    hasChanged = True

    while count > 0 and hasChanged:
        hasChanged = False
        templ = list()
        for item in tempIds[-1]:
            for i in readData:
                if i.MANAGER_EMPLOYEE_ID == item.EMPLOYEE_ID:
                    item.reportees.append(i)
                    templ.append(i)
                    count -= 1
                    hasChanged = True
        if (templ!=[]):
            tempIds.append(templ)
    
    bossObj = tempIds[0][0]
    empTree = bossObj.generateTree()
        
    # ===== dump data in json file =====
    fileObj = open(DESCINATION_FILE, "w")
    json.dump(empTree, fileObj)
    fileObj.close()
