class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.small = small
        self.medium = medium

    def addCar(self, carType: int) -> bool:
        """
        bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
        carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
        A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
        """

        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False

        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False

        else:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False


# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]


parkingSystem = ParkingSystem(1, 1, 0)
print(
    parkingSystem.addCar(1)
)  #  return true because there is 1 available slot for a big car
print(
    parkingSystem.addCar(2)
)  #  return true because there is 1 available slot for a medium car
print(
    parkingSystem.addCar(3)
)  #  return false because there is no available slot for a small car
print(
    parkingSystem.addCar(1)
)  #  return false because there is no available slot for a big car. It is already occupied.


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
