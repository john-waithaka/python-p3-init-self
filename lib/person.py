#!/usr/bin/env python3

# class Person:
#     pass


class Person:
    def __init__(self, name):
        self.name = name

john = Person("John")
print(f"{john.name} is programming")


#just gives the name and takes the default breed given in the class
# buddy = Dog("Buddy")
# print(f"{buddy.name} is a {buddy.breed}.")