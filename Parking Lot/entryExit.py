from parkingSpotManager import ParkingSpotManager, Ticket
import time

class Entrance:
    def __init__(self, strategy):
        self.parkingSpotManager = ParkingSpotManager.get_instance(strategy)

    def parkVehicle(self, vehicleType, vehicleNumber):
        parking_spot, vehicle = self.parkingSpotManager.parkVehicle(vehicleType, vehicleNumber)
        print("Parked vehicle with number " + vehicleNumber + " successfully!")
        ticket = Ticket(vehicle, parking_spot, time.time())
        return ticket

class Exit:
    def __init__(self, strategy) -> None:
        self.parkingSpotManager = ParkingSpotManager.get_instance(strategy)

    def unparkVehicle(self, parkingSpot):
        vehicle = self.parkingSpotManager.unparkVehicle(parkingSpot)
        return vehicle
    
    def getAmount(self, ticket):
        entryTime = ticket.entryTime
        exitTime = time.time()
        return (exitTime - entryTime) * ticket.parking_spot.price
    
    def pay(self, amount):
        print("Payment of " + str(amount) + " successful. Thank you!")
