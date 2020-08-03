#!/usr/bin/env python

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__age

    def getAge(self):
        return self.__name


s = Student('tom', 18)

print(s.getName(), s.getAge())
