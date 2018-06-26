from miplant import MiPlant

for plant in MiPlant.discover():
        print("hi")
        print(plant.temperature)
