#!/usr/bin/env python3

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('h1')


class Student(Person):

    def say(self):
        print('aaa')


s = Student('tom', 100)

s.say()

print(s.name, s.age)
