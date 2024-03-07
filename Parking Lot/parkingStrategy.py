import random
from abc import ABC, abstractmethod
from parkingLot import ParkingLotFactory

class ParkingStrategy(ABC):
    def __init__(self) -> None:
        self.parkingLotFactory = ParkingLotFactory()

    @abstractmethod
    def getParkingSpot(self, vehicleType):
        pass
        

class NearestParkingSpot(ParkingStrategy):
    def __init__(self) -> None:
        super().__init__()

    def getParkingSpot(self, vehicleType):
        parkingLot = self.parkingLotFactory.getParkingLot(vehicleType=vehicleType)
        for spot in parkingLot.parkingSpots:
            if spot.isEmpty:
                return spot
        

class RandomParkingSpot(ParkingStrategy):
    def __init__(self) -> None:
        super().__init__()

    def getParkingSpot(self, vehicleType):
        parkingLot = self.parkingLotFactory.getParkingLot(vehicleType=vehicleType)
        availableSpots = []
        for spot in parkingLot.parkingSpots:
            if spot.isEmpty:
                availableSpots.append(spot)

        if len(availableSpots) > 0:
            randomIndex = random.randint(0, len(availableSpots) - 1)
            return availableSpots[randomIndex]
        return None
    