class Building:
    total = 0
    def __init__(self, floor):
        Building.total += 1
        self.floor = floor
        print("Number_of_floor {}".format(self.floor))
building_floors = {}
for i in range(1, 41):
    floor_in_for = i
    building_floors[floor_in_for] = building_floors.get(floor_in_for, Building(floor = floor_in_for))
print('Total', Building.total)