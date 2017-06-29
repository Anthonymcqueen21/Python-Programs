# Car class

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a certain vehicle."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a nearly formatted descriputive name."""
        long_name = str(self.year) + ' ' + self.name + ' ' + self.model
        return long_name.title()
        
    my_new_car = Car('Ford', 'GT', 2017)
    print(my_new_car.get_descriptive_name())
    
    
