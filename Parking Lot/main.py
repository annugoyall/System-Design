from parkingLot import ParkingSpot
from entryExit import Entrance, Exit

def main():
    vehicle_type = "TwoWheeler"
    vehicle_number = "KA01HH1234"

    parking_lot = "Nearest"
    entrance = Entrance(parking_lot)
    parking_spot = ParkingSpot(vehicle_type, True, 1000)
    entrance.parkingSpotManager.addParkingSpot(parking_spot, vehicle_type)
    print("Parking vehicle")
    ticket = entrance.parkVehicle(vehicle_type, vehicle_number)

    print("Unparking vehicle")
    exit = Exit(parking_lot)
    amount = exit.getAmount(ticket)
    exit.pay(amount)
    print(exit.unparkVehicle(ticket.parking_spot))    

main()