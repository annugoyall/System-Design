class ParkingSpot:
    def __init__(self, type, isEmpty, price) -> None:
        self.type = type
        self.isEmpty = isEmpty
        self.price = price
        self.vehicle = None

    def park(self, vehicle):
        self.vehicle = vehicle
        self.isEmpty = False
    
    def unpark(self):
        self.vehicle = None
        self.isEmpty = True

    def getVehicle(self):
        return self.vehicle
    

class ParkingLot:
    _instance = None

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def __init__(self) -> None:
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        self.parkingSpots = []

    def addParkingSpot(self, parkingSpot):
        self.parkingSpots.append(parkingSpot)

    def removeParkingSpot(self, parkingSpot):
        self.parkingSpots.remove(parkingSpot)

class TwoWheelerParkingLot(ParkingLot):
    _instance = None

    @staticmethod
    def get_instance():
        if TwoWheelerParkingLot._instance is None:
            TwoWheelerParkingLot._instance = TwoWheelerParkingLot()
        return TwoWheelerParkingLot._instance

    def __init__(self) -> None:
        if TwoWheelerParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        super().__init__()

class ThreeWheelerParkingLot(ParkingLot):
    _instance = None

    @staticmethod
    def get_instance():
        if ThreeWheelerParkingLot._instance is None:
            ThreeWheelerParkingLot._instance = ThreeWheelerParkingLot()
        return ThreeWheelerParkingLot._instance

    def __init__(self) -> None:
        if ThreeWheelerParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        super().__init__()

class FourWheelerParkingLot(ParkingLot):
    _instance = None

    @staticmethod
    def get_instance():
        if FourWheelerParkingLot._instance is None:
            FourWheelerParkingLot._instance = FourWheelerParkingLot()
        return FourWheelerParkingLot._instance

    def __init__(self) -> None:
        if FourWheelerParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        super().__init__()

class ParkingLotFactory:
    @staticmethod
    def getParkingLot(vehicleType):
        if vehicleType == "TwoWheeler":
            return TwoWheelerParkingLot.get_instance()
        elif vehicleType == "ThreeWheeler":
            return ThreeWheelerParkingLot.get_instance()
        elif vehicleType == "FourWheeler":
            return FourWheelerParkingLot.get_instance()
        else:
            return None
