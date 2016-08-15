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

    def park(self, car):
        if self.capacity == 0:
            return 'No parking spaces available'
        else:
            self.parked += 1 # Update parked count
            self.capacity = self.spaces - self.parked # Update capacity
            self.carlist.append(car)
            return str(car) +' has been parked'
            
    def retrieve(self, car):
        if car in self.carlist:
            self.carlist.remove(car)
            self.parked -= 1
            self.capacity = self.spaces - self.parked
            return str(car) + ' has exited the lot'
        else:
            return str(car) + ' not parked in this lot'


class Car(object):
    def __init__(self, brand, model, year):
        if type(year) != int:
            raise ValueError
        self.brand = brand
        self.model = model
        self.year = year
        
    def __str__(self):
        return '{} {} {}'.format(self.year,self.brand,self.model)
    
    def __repr__(self):
        return '{} {} {}'.format(self.year,self.brand,self.model)
        