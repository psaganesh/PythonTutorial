#!/usr/bin/python

class Car(object):
    
    @staticmethod  
    def make_car_sound():
        print 'VRooooommmm!'

mustang = Car()
print mustang
mustang.make_car_sound()

