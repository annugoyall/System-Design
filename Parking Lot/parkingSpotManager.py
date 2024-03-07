from parkingLot import ParkingLotFactory
from vehicle import VehicleFactory
from parkingStrategy import NearestParkingSpot, RandomParkingSpot
import time

class Ticket:
    def __init__(self, vehicleId, parking_spot_id, entryTime) -> None:
        self.vehicleId = vehicleId
        self.parking_spot = parking_spot_id
        self.entryTime = entryTime

class ParkingSpotManager:
    _instance = None

    @staticmethod
    def get_instance(parkingStrategy):
        if ParkingSpotManager._instance is None:
            ParkingSpotManager._instance = ParkingSpotManager(parkingStrategy)
        return ParkingSpotManager._instance

    def __init__(self, parkingStrategy) -> None:
        if ParkingSpotManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            if parkingStrategy == "Nearest":
                self.parkingStrategy = NearestParkingSpot()
            else:
                self.parkingStrategy = RandomParkingSpot()
        self.parkingLotFactory = ParkingLotFactory()

    def parkVehicle(self, vehicleType, vehicleNumber):
        parkingSpot = self.parkingStrategy.getParkingSpot(vehicleType=vehicleType)
        if parkingSpot:
            vehicleFactory = VehicleFactory()
            vehicle = vehicleFactory.createVehicle(vehicleNumber, vehicleType)
            parkingSpot.park(vehicle)
            return parkingSpot, vehicle
        return None, None

    def unparkVehicle(self, parkingSpot):
        parkingSpot.unpark()
        return parkingSpot.getVehicle()
    
    def addParkingSpot(self, parkingSpot, vehicleType):
        parkingLot = self.parkingLotFactory.getParkingLot(vehicleType=vehicleType)
        parkingLot.addParkingSpot(parkingSpot)

    def removeParkingSpot(self, parkingSpot, vehicleType):
        parkingLot = self.parkingLotFactory.getParkingLot(vehicleType=vehicleType)
        parkingLot.removeParkingSpot(parkingSpot)