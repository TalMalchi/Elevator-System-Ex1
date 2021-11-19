import Building
from Elevator import Elevator
import csv

class Calls:

    def __init__(self, csv): #call constructor
        #self.text = csv[0]
        self.time = float(csv[1])
        self.source = int(csv[2])
        self.destination = int(csv[3])
        self.state= int(csv[4])
        self.allocated_elevator = -1

    #function that check time between two floors
    def calculate_time_two_floors(self, firstfloor, secondfloor,elevator: Elevator):
        time_two_floors = 0
        time_two_floors = elevator.openTime + elevator.closeTime + elevator.startTime + elevator.stopTime + elevator.speed + (
                    (abs(firstfloor - secondfloor)) / elevator.speed)
        return time_two_floors

    def check_time(self,elevator: Elevator): #check the total time for each elevator
        finaltimeUP = 0
        for i in range(len(elevator.listCalls) - 1):
            curr_call = elevator.listCalls[i]
            next_call = elevator.listCalls[i + 1]

            finaltimeUP = self.calculate_time_two_floors(curr_call, next_call, elevator) +\
                          finaltimeUP
        return finaltimeUP

    # function go all over the elevator in the building and check the fast elevator
    def allocateTo(self, building: Building):
            minElv=0 #default min elevator
            time_before= self.check_time(building.elevators[0])
            building.elevators[0].tempCall_list_before()
            building.elevators[0].listCalls.append(self.source)
            building.elevators[0].listCalls.append(self.destination)
            building.elevators[0].listCalls.sort()
            time_after = self.check_time(building.elevators[0])
            building.elevators[0].tempCall_list_after()
            building.elevators[0].location= self.destination
            min_time=time_after-time_before
            i = 0
            for elevator in building.elevators:
                time_before_temp = self.check_time(elevator)
                elevator.tempCall_list_before()
                elevator.listCalls.append(self.source)
                elevator.listCalls.append(self.destination)
                elevator.listCalls.sort()
                time_after_temp = self.check_time(elevator)
                elevator.tempCall_list_after()
                temp_time=time_after_temp
                if temp_time < min_time:

                    min_time = temp_time
                    minElv = i
                i += 1
            self.allocated_elevator=minElv
            return self.allocated_elevator
