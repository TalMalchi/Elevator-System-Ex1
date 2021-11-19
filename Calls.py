import Building
from Elevator import Elevator
import csv

class Calls:

    def __init__(self, csv): #call constructor
        self.time = float(csv[1])
        self.source = int(csv[2])
        self.destination = int(csv[3])
        self.allocated_elevator = -1


    def calculate_time_two_floors(self, firstfloor, secondfloor):
        time_two_floors = 0
        time_two_floors = self.openTime + self.closeTime + self.startTime + self.stopTime + self.speed + (
                    (abs(firstfloor - secondfloor)) / self.speed)
        return time_two_floors

    def check_time(self,elevator: Elevator): #check the total time for each elevator
        #finaltimeUP= elevator.closeTime+elevator.startTime+elevator.stopTime+elevator.openTime+ \
                     #abs(self.source-self.destination)
        finaltimeUP = 0
        for i in elevator.listCalls:
            finaltimeUP = self.calculate_time_two_floors(i, i + 1) + finaltimeUP
        return finaltimeUP

    # function go all over the elevator in the building and check the fast elevator
    def allocateTo(self, building: Building):
            minElv=0 #default min elevator
            time_before= self.check_time(building.elevator[0])
            building.elevator[0].tempCall_list_before()
            building.elevator[0].listCalls.append(self)
            time_after = self.check_time(building.elevator[0])
            building.elevator[0].tempCall_list_after()
            min_time=time_before-time_after
            for i in building.elevator:
                time_before_temp = self.check_time(building.elevator[i])
                building.elevator[i].tempCall_list_before()
                building.elevator[i].listCalls.append(self)
                time_after_temp = self.check_time(building.elevator[i])
                building.elevator[i].tempCall_list_after()
                temp_time = time_before_temp - time_after_temp
                if temp_time<minValue:
                    minValue=temp_time
                    minElv=i
            #self.allocateTo = building.getElev(building.elevators[elevatorId])
            self.allocated_elevator=building.elevator[minElv]
            return self.allocated_elevator
