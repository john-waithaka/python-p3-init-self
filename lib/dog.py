#!/usr/bin/env python3

# class Dog:
#     pass

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

nara = Dog("Nara" , "German Shepherd")
print(f"{nara.name} is a {nara.breed}.")        



#just gives the name and takes the default breed given in the class
# buddy = Dog("Buddy")
# print(f"{buddy.name} is a {buddy.breed}.")
