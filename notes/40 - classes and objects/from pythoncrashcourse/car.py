"""A class that can be used to represent a car. class可以用来表示一辆汽车。"""
'''Example From: Python Crash Course 2nd Edition chapter 9
https://github.com/ehmatthes/pcc/blob/master/chapter_09/car.py'''

class Car():
    """A simple attempt to represent a NEW car."""

    def __init__(self, manufacturerIn, modelIn, yearIn):
        """Initialize attributes to describe a car.初始化(init)属性以描述一辆汽车。"""
        self.manufacturer = manufacturerIn#制造商
        self.model = modelIn
        self.year = yearIn
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name.返回一个格式整齐的描述性名称。"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage.打印一份显示汽车里程数的报表。"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.将里程表读数设置为给定值。
        Reject the change if it attempts to roll the odometer back.如果它试图将里程表向后滚动，则拒绝该变化。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.在里程表读数上加上给定的金额。"""
        self.odometer_reading += miles
