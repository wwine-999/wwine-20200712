#!/usr/bin/env python3

class Person:

    def say(self):
        print('我会说话')


class Chinese(Person):

    def say(self):
        print('我是中国人,我说普通话')


class Japanese(Person):

    def say(self):
        print('我是日本人,我说日语')


class American(Person):

    def say(self):
        print('我是美国人,我说美语')


def speak(s):
    s.say()


speak(Chinese())
speak(Japanese())
American().say()
