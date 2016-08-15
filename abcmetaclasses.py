# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 18:15:28 2016

@author: Ken
"""

from abc import ABCMeta, abstractmethod

class Pet(object):
    __metaclass__ = ABCMeta
    
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def can_swim(self):
        pass
    @abstractmethod
    def speak(self):
        pass

class Dog(Pet):
    def can_swim(self):
        super(Dog, self).can_swim()
        return True
        
    def speak(self):
        super(Dog, self).speak()
        return self.name + ' says "Woof!"'
        
class Cat(Pet):
    def can_swim(self):
        super(Cat, self).can_swim()
        return False
        
    def speak(self):
        super(Cat, self).speak()
        return self.name + ' says "Meow!"'
        
class Fish(Pet):
    def can_swim(self):
        super(Fish, self).can_swim()
        return True
        
    def speak(self):
        super(Fish, self).speak()
        return self.name + " can't speak."

class Plant(Pet):
    def can_swim(self):
        super(Plant, self).can_swim()
        return False
        
    def speak(self):
        super(Plant, self).speak()
        return self.name + " can't speak."