from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def press_button(self, aisle_number):
        pass

class NoCoinInsertedState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, amount):
        # self.vending_machine.set_amount()
        print("Coin inserted", amount)
        self.vending_machine.set_state(self.vending_machine.coin_inserted_state)

    def press_button(self, aisle_number):
        raise MachineException("No coin inserted")

    def dispense(self):
        raise MachineException("No coin inserted")

class CoinInsertedState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        raise MachineException("Coin already inserted")

    def press_button(self, aisle_number):
        print("Button pressed", aisle_number)
        self.vending_machine.set_state(self.vending_machine.dispensing_state)

    def dispense(self):
        raise MachineException("Button yet to press")

class DispensingState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        raise MachineException("Please wait while product is dispensing")

    def press_button(self, aisle_number):
        raise MachineException("Please wait while product is dispensing")

    def dispense(self, aisle_number):
        # print(self.vending_machine.inventory.aisle_product_map)
        print(self.vending_machine.inventory.aisle_product_map[aisle_number].name, "dispensed")
        # self.vending_machine.get_product_at(aisle_number)
        self.vending_machine.set_state(self.vending_machine.no_coin_inserted_state)

class Product:
    def __init__(self, name, product_id, price):
        self.name = name
        self.product_id = product_id
        self.price = price

    def __str__(self):
        return self.name
    
class Inventory:
    def __init__(self):
        self.product_count_map = {}
        self.aisle_product_map = {}
        self.available_aisle = list(range(11))

    def add_product(self, product):
        if product in self.product_count_map:
            self.product_count_map[product] += 1
        else:
            if self.available_aisle:
                aisle_number = self.available_aisle.pop()
            else:
                raise MachineException("No aisle to add new product")

            self.aisle_product_map[aisle_number] = product
            self.product_count_map[product] = 1

class VendingMachine:
    def __init__(self):
        self.no_coin_inserted_state = NoCoinInsertedState(self)
        self.coin_inserted_state = CoinInsertedState(self)
        self.dispensing_state = DispensingState(self)
        self.machine_state = self.no_coin_inserted_state
        self.loaded_amount = 0
        self.inventory = Inventory()

    def show_inventory(self):
        print(self.inventory.aisle_product_map)

    def insert_coin(self, amount):
        self.machine_state.insert_coin(amount)

    def press_button(self, aisle_number):
        self.machine_state.press_button(aisle_number)
        self.machine_state.dispense(aisle_number)

    def set_state(self, state):
        self.machine_state = state

    def set_amount(self):
        # Implementation of setting amount
        pass

    def check_if_product_available(self, aisle_number):
        # Implementation of checking product availability
        pass

    def get_product_at(self, aisle_number):
        # Implementation of getting product at aisle number
        pass

class MachineException(Exception):
    pass

# Path: main.py


# Create a vending machine instance
vending_machine = VendingMachine()

# Define some sample products
product1 = Product("Coke", 1, 1.5)
product2 = Product("Pepsi", 2, 1.5)

# Add products to the inventory
vending_machine.inventory.add_product(product1)
vending_machine.inventory.add_product(product2)

vending_machine.show_inventory()
# Insert a coin into the vending machine
vending_machine.insert_coin(1)

# Press a button to select a product
try:
    vending_machine.press_button(9)
except MachineException as e:
    print(e)

# Press a button to dispense the product
try:
    vending_machine.press_button(9)
except MachineException as e:
    print(e)