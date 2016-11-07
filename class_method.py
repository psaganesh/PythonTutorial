#!/usr/bin/python

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

class Vehicle(object):
  
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2

test = Vehicle('Car')

test.is_motorcycle()
