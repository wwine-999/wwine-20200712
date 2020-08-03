#!/usr/bin/env python3

class Student:

    def __init__(self, score):
        self.__score = score

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def set_score(self, score):
        if score >= 0 and score <= 100:
            self.__score = score
        else:
            print('成绩范围0-100')


s = Student(-100)
s.set_score = 50
print(s.get_score)
