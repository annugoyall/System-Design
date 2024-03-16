from enum import Enum

class States(Enum):
    Idle = 0
    AcceptingMoney = 1
    SelectingProduct = 2
    DispensingProduct = 3
    ReturningChange = 4

class Items:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.quantity = 0
    
    def add(self, quantity):
        self.quantity += quantity
    
    def decrease(self, quantity):
        self.quantity -= quantity

class VendingMachineManager:
    _instance = None

    def getinstance():
        if VendingMachineManager._instance is None:
            VendingMachineManager._instance = VendingMachineManager()
        return VendingMachineManager._instance
    
    def __init__(self) -> None:
        self.items = {}
        _instance = self
    
    def update_item(self, shelfNumber, item):
        self.items[shelfNumber] = item

class VendingMachineState:
    def __init__(self, vendingMachine) -> None:
        self.vendingMachine = vendingMachine
    
    def insert_money(self, amount):
        pass
    
    def select_product(self, shelfNumber):
        pass
    
    def dispense_product(self):
        pass
    
    def return_change(self):
        pass

class AcceptingMoneyState(VendingMachineState):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def insert_money(self, amount):
        print("Money inserted")
        self.vendingMachine.state = SelectingProductState(self.vendingMachine)
    
    def select_product(self, shelfNumber):
        pass
    
    def dispense_product(self):
        pass
    
    def return_change(self):
        pass

class SelectingProductState(VendingMachineState):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def insert_money(self, amount):
        pass
    
    def select_product(self, shelfNumber):
        print("Product selected", self.vendingMachine.vmManager.items[shelfNumber].name)
        self.vendingMachine.state = DispensingProductState(self.vendingMachine)
    
    def dispense_product(self):
        pass
    
    def return_change(self):
        pass

class DispensingProductState(VendingMachineState):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def insert_money(self, amount):
        pass
    
    def select_product(self, shelfNumber):
        pass
    
    def dispense_product(self):
        print("Product dispensed")
        self.vendingMachine.state = ReturningChangeState(self.vendingMachine)
    
    def return_change(self):
        pass

class ReturningChangeState(VendingMachineState):
    def __init__(self, vendingMachine) -> None:
        super().__init__(vendingMachine)
    
    def insert_money(self, amount):
        pass
    
    def select_product(self, shelfNumber):
        pass
    
    def dispense_product(self):
        pass
    
    def return_change(self):
        print("Change returned")
        self.vendingMachine.state = AcceptingMoneyState(self.vendingMachine)

class VendingMachine:
    def __init__(self) -> None:
        self.vmManager = VendingMachineManager.getinstance()
        self.state = AcceptingMoneyState(self)  # Set initial state to Idle

    def update_item(self, shelfNumber, item):
        self.vmManager.update_item(shelfNumber, item)

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

    def insert_money(self, amount):
        self.state.insert_money(amount)

    def select_product(self, shelfNumber):
        self.state.select_product(shelfNumber)

    def dispense_product(self):
        self.state.dispense_product()

    def return_change(self):
        self.state.return_change()

vm = VendingMachine()
item1 = Items("Coke", 1.5)
item2 = Items("Pepsi", 1.5)
vm.update_item(1, item1)
vm.update_item(2, item2)
item1.add(10)
item2.add(10)
vm.insert_money(2)
vm.select_product(1)
vm.dispense_product()
vm.return_change()