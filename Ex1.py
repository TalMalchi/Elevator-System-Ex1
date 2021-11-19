import sys
import csv
from Calls import Calls
from Building import Building
import json

def createBuilding(building): #create a building fron the json file
    return Building(building)

calls_list=[]
def ReadFromCSV(csv_calls): #read the csv file, create new calls and add then to a list
    with open(csv_calls, 'r') as f:
        reader = csv.reader(f)
        for call in reader:
            calls_list.append(Calls(call))
        f.close()
    Building.calls=calls_list



def CreateNewCSV(csv_output): #create new csv file with allocate elevalor for each call
    with open(csv_output, "w", newline="") as f:
        writer = csv.writer(f)
        for i in Building.calls:
            ans= Building.calls_output(i)
            writer.writerows(ans)


if __name__ == '__main__':
    #list = sys.argv
    # building = list[1]
    # csv_calls = list[2]
    # csv_output = list[3]

    building= ("B5.json")
    csv_calls= ("Calls_a.csv")
    file=("out.log")
    createBuilding(building)
    ReadFromCSV(csv_calls)
    CreateNewCSV(file)








