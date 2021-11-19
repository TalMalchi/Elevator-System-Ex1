
import sys
import csv
from Calls import Calls
from Building import Building
import json


def createBuilding(building_json): #create a building fron the json file
    return Building(building_json)


def ReadFromCSV(csv_calls): #read the csv file, create new calls and add then to a list
    with open(csv_calls, 'r') as f:
        calls_list = []
        reader = csv.reader(f)
        for call in reader:
            calls_list.append(Calls(call))
        f.close()
    building_objcet.calls = calls_list


def CreateNewCSV(csv_output): #create new csv file with allocate elevalor for each call
    with open(csv_output, "w", newline="") as f:
        writer = csv.writer(f)
        for i in building_objcet.calls:
            ans = building_objcet.calls_output(i)
            print(ans)
            writer.writerow(ans)


if __name__ == '__main__':
    list = sys.argv
    building = list[1]
    csv_calls = list[2]
    csv_output = list[3]

    # building= ("B1.json")
    # csv_calls= ("Calls_a.csv")
    # csv_output=("out.log")

    building_objcet = createBuilding(building)
    ReadFromCSV(csv_calls)
    CreateNewCSV(csv_output)








