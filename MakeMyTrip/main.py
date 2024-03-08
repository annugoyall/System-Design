class Seat:
    def __init__(self, row, col, type) -> None:
        self.row = row
        self.col = col
        self.type = type
        self.price = None
        self.customer = None
    
    def bookSeat(self, customer):
        self.customer = customer

    def cancelSeat(self):
        self.customer = None

    def getSeatPrice(self):
        return self.price
    
    def setSeatPrice(self, price):
        self.price = price

    def isFree(self):
        return self.customer == None
    
    def __str__(self) -> str:
        return f"Seat {self.row}-{self.col} of type {self.type}"

class Flight:

    def __init__(self, source, destination, date, start_time, end_time) -> None:
        self.source = source
        self.destination = destination
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.seats = []

    def __str__(self) -> str:
        return f"Flight from {self.source} to {self.destination} on {self.date} from {self.start_time} to {self.end_time}"

    def cancelFlight(self, customer):
        for seat in self.seats:
            if seat.customer == customer:
                seat.customer = None

    def bookSeat(self, customer, seat):
        if seat.isFree():
            seat.bookSeat(customer)
            return True
        return False
    
    def addSeat(self, seat):
        self.seats.append(seat)
    
    def getFreeSeats(self):
        free_seats = []
        for seat in self.seats:
            if seat.isFree():
                free_seats.append(seat)
        return free_seats
    
    def getBookedSeats(self):
        booked_seats = []
        for seat in self.seats:
            if not seat.isFree():
                booked_seats.append(seat)
        return booked_seats
    
class System:
    _instance = None
    
    def __init__(self) -> None:
        if System._instance != None:
            raise Exception("This class is a singleton!")
        else:
            System._instance = self
        self.flights = []

    def getInstance():
        if System._instance == None:
            System()
        return System._instance

    def fetchFlights(self, source, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights
    
    def addFlight(self, flight):
        self.flights.append(flight)

    def cancelFlight(self, flight):
        booked_seats = flight.getBookedSeats()

        for seat in booked_seats:
            self.cancelFlightForCustomer(seat.customer, flight, seat)
            seat.cancelSeat()
        
        self.flights.remove(flight) 
        print(f"Flight {flight} has been cancelled and all the bookings have been refunded")

    def initiateRefund(self, customer, flight):
        print(f"Refund has been initiated for {customer} for the flight {flight}")

    def cancelFlightForCustomer(self, customer, flight, seat = None):
        self.initiateRefund(customer , flight)

        if seat == None:
            for seat in flight.seats:
                if seat.customer == customer:
                    break

        seat.cancelSeat()

        print(f"Booking has been cancelled for {customer.name} for the flight {flight}")

class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.bookingManager = System.getInstance()

    def __str__(self) -> str:
        return self.name

class Customer(User):
    
    def __init__(self, name, email) -> None:
        super().__init__(name, email)
        self.bookings = []

    def bookFlight(self, flight, seat):
        if flight.bookSeat(self, seat):
            self.bookings.append(flight)
            print(f"Booking has been done for {self} for the flight {flight}")
            return True
        return False
    
    def cancelBooking(self, flight):
        self.bookings.remove(flight)
        self.bookingManager.cancelFlightForCustomer(self, flight)

class Admin(User):
    def __init__(self, name, email) -> None:
        super().__init__(name, email)
    
    def addFlight(self, flight):
        self.bookingManager.addFlight(flight)
    
    def cancelFlight(self, flight):
        self.bookingManager.cancelFlight(flight)

# Usage
        
# Create a system
bookingManager = System()
Customer1 = Customer("Annu", "annu@gmail.com")
Customer2 = Customer("Mayank", "mayank@gmail.com")
admin = Admin("Admin", "admin@gmail.com")
flight1 = Flight("Delhi", "Mumbai", "2022-10-10", "10:00", "12:00")
flight2 = Flight("Delhi", "Mumbai", "2022-10-10", "14:00", "16:00")
admin.addFlight(flight1)
admin.addFlight(flight2)
seat1 = Seat(1, 1, "Business")
seat1.setSeatPrice(10000)
seat2 = Seat(1, 2, "Economy")
seat2.setSeatPrice(5000)
flight1.addSeat(seat1)
flight1.addSeat(seat2)

# Fetch flights
flights = bookingManager.fetchFlights("Delhi", "Mumbai", "2022-10-10")
print(flights)
seats = flights[0].getFreeSeats()
print(seats)

# Book a seat
Customer1.bookFlight(flights[0], seats[0])

# Cancel a booking
Customer1.cancelBooking(flights[0])