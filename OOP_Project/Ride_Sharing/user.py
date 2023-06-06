from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return repr({
            'comapany_name': self.company_name,
            'riders': len(self.riders),
            'drivers': len(self.drivers),
            'rides': len(self.rides),
        })


class User(ABC):
    def __init__(self, name, email, password, nid) -> None:
        self.name = name
        self.email = email
        self.__password = password
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, password, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, password, nid)

    def display_profile(self):
        print(f'Rider with name: {self.name} and email: {self.email}') 

    def load_cas(self, amount):
        if(amount > 0):
            self.wallet += amount

    def update_locatin(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing,  destination):
        if(not self.current_ride):
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            self.current_ride = ride_matcher.find_rider(ride_request)

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, password, nid, currrent_location) -> None:
        self.current_location = currrent_location
        self.wallet = 0
        super().__init__(name, email, password, nid)

    def display_profile(self):
        print(f'Rider with name: {self.name} and email: {self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amoutn):
        self.end_time = datetime.now()
        self.rider.wallet -=  self.estimated_fare
        self.driver.wallet +=  self.estimated_fare

    def __repr__(self) -> str:
        return (f'Rdie details. Started: {self.start_location} to end: {self.end_location} ')

class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_Matching :
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_rider(self, ride_request):
        if(len(self.available_drivers) > 0):
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):
    speed = {'car': 50, 'bike': 60, 'cng': 40, 'bus': 65}
    def __init__(self, vehicle_type, license_plate, rate, ) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class CNG(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'


# check the class intregration

pathao = Ride_Sharing('Pathao Limited')
rifat = Rider('Rifat Ahmed', 'rifat12@gmail.com', 'd7sad6732f', '17832782347', 'Bogora', 1340)
pathao.add_rider(rifat)
arafat = Driver('Arafat Shuvo', 'arafat12@gmai.com', 'gh8237yg', 1832989328, 'zurain')
pathao.add_driver(arafat)

print(pathao)
rifat.request_ride(pathao, 'Wari',)
rifat.show_current_ride()