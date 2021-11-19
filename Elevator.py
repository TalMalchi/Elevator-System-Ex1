
class Elevator:

    #elevator constructor
    def __init__(self, id: int = None, speed: int = None, minFloor: int = None, maxFloor: int = None,
                 closeTime: float = None, openTime: float = None, startTime: float = None, stopTime: float = None,
                 **kwargs):
        """
        :param id: return the id of this elevator
        :param speed: Returns the speed (in floor per second)
        :param minFloor: eturns the minimal floor number to which this Elevator can reach
        :param maxFloor: Returns the maximal floor number to which this Elevator can reach.
        :param closeTime: Returns the time (in seconds it takes the Elevator to close its doors)
        :param openTime: Returns the time (in seconds it takes the Elevator to open its doors)
        :param startTime: Return the time in seconds that it takes the elevator to start moving in full speed
        :param stopTime: Return the time in seconds that it takes the elevator to stop moving in full speed
        """
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.listCalls = []
        self.temp_listCalls = []
        self.location = []  # elevator[t]

    def tempCall_list_before(self): #create temp list call
        self.temp_listCalls = self.listCalls.copy()

    def tempCall_list_after(self): #return to the original list call
        self.listCalls = self.temp_listCalls.copy()