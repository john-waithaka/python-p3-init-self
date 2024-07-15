#!/usr/bin/env python3

# class Dog:
#     pass

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

nara = Dog("Nara" , "German Shepherd")
print(f"{nara.name} is a {nara.breed}.")        


# fido = Dog("Fido", "Golden Retriever")
# print(f"{fido.name} is a {fido.breed}.")
