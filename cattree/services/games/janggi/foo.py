class Coordinate:
    coefficient = 1
    all = []

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        Coordinate.all.append(self)

    def __str__(self):
        return f"coordinate: ({self.x}, {self.y})"

    def transfer_by_coefficient(self):
        self.x = self.x * self.coefficient
        self.y = self.y * self.coefficient

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


coor1 = Coordinate(1, 3)
coor1.transfer_by_coefficient()
print(coor1.__dict__)
print(coor1.__str__())
coor1.coefficient = 3
coor1.transfer_by_coefficient()
print(coor1.__dict__)
print(coor1.__str__())
print(Coordinate.coefficient)
Coordinate.coefficient = 2
coor2 = Coordinate(1, 2)
coor2.transfer_by_coefficient()
print(coor2.__str__())
print(Coordinate.coefficient)
print(Coordinate.__dict__)
print(Coordinate.all)
