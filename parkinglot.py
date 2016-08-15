
class ParkingLot(object):
    def __init__(self, spaces=5, parked=0, carlist=[]):
        if spaces < 0 or parked < 0:
            raise ValueError
        if len(carlist) > spaces:
            raise ValueError
        self.spaces = spaces
        self.parked = parked
        self.carlist = carlist
        self.capacity = self.spaces - self.parked
        # number of parking spaces set when instantiated
        # default parking spaces = 5

    def park(self,car):
        if self.capacity == 0:
            return 'No parking spaces available'
        else:
            self.parked += 1 # Update parked count
            self.capacity = self.spaces - self.parked # Update capacity
            self.carlist.append(car)
            return car +' has been parked'
            
    def return_car(self,car):
        if car in self.carlist:
            self.carlist.remove(car)
            self.parked -= 1
            self.capacity = self.spaces - self.parked
            return car + ' has exited the lot'
        else:
            return car + ' not parked in this lot'










