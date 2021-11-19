import json
import Calls
from Elevator import Elevator


class Building:

    def __init__(self, file_name): #building constructor
        #f=open(file_name)
        with open(file_name) as f:  # open the file as r (read)
            data= f.read()
        building= json.loads(data)
        self.minFloor=building['_minFloor']
        self.maxFloor=building['_maxFloor']
        self.calls = [] #create list calls for each building
        self.elevators=[] #create elevator list
        for i in building['_elevators']:
            self.elevators.append(Elevator(i["_id"], i["_speed"], i["_minFloor"], i["_maxFloor"],
                          i["_closeTime"], i["_openTime"],i["_startTime"], i["_stopTime"]))

    # function gets a call, allocate an elevator and add the call to new csv file
    def calls_output(self, new_call: Calls):
        temp_list=["Elevator call", new_call.time, new_call.source, new_call.destination, new_call.state]
        chosen_ele = new_call.allocateTo(self)
        temp_list.append(chosen_ele)
        temp_list.append("Done")
        return temp_list










