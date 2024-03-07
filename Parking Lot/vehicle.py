class Vehicle:
    def __init__(self, vehicle_number) -> None:
        self.vehicle_number = vehicle_number

class TwoWheeler(Vehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number)

class ThreeWheeler(Vehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number)

class FourWheeler(Vehicle):
    def __init__(self, vehicle_number) -> None:
        super().__init__(vehicle_number)

class VehicleFactory:
    def createVehicle(self, vehicle_number, vehicle_type):
        if vehicle_type == "TwoWheeler":
            return TwoWheeler(vehicle_number)
        elif vehicle_type == "ThreeWheeler":
            return ThreeWheeler(vehicle_number)
        elif vehicle_type == "FourWheeler":
            return FourWheeler(vehicle_number)
        else:
            return None