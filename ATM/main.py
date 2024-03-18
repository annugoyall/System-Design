class Card:
    def __init__(self, card_number, pin, balance):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return "Withdrawal successful"
    
    def change_pin(self, new_pin):
        self.pin = new_pin
        return "Pin change successful"

class Cards:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        return "Card added successfully"

    def card_exists(self, card_number):
        for card in self.cards:
            if card.card_number == card_number:
                return True
        return False

    def get_card(self, card_number):
        for card in self.cards:
            if card.card_number == card_number:
                return card
        return None
    
class ATMState:
    def __init__(self, atm):
        self.atm = atm
        
    def insert_card(self, card_number):
        pass

    def enter_pin(self, pin):
        pass
    
    def check_balance(self):
        pass
    
    def withdraw(self, amount):
        pass
    
    def change_pin(self, new_pin):
        pass
    
    def cancel(self):
        pass

class IdleState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def start_operation(self):
        self.atm.state = CardInsertedState(self.atm)
        return "Please insert your card"
    
    def insert_card(self, card_number):
        return "Operation not allowed"

    def enter_pin(self, pin):
        return "Operation not allowed"

    def check_balance(self):
        return "Operation not allowed"

    def withdraw(self, amount):
        return "Operation not allowed"

    def change_pin(self, new_pin):
        return "Operation not allowed"

    def cancel(self):
        return "No operation to cancel"

class CardInsertedState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card_number):
        print("Card inserted")
        for card in self.atm.cards.cards:
            if card.card_number == card_number:
                self.atm.card_number = card_number
                self.atm.state = PinState(self.atm)
                return "Please enter your pin"
        self.atm.state = IdleState(self.atm)
        print("Card not found")

    def enter_pin(self, pin):
        return "Operation not allowed"
    
    def check_balance(self):
        return "Operation not allowed"
    
    def withdraw(self, amount):
        return "Operation not allowed"
    
    def change_pin(self, new_pin):
        return "Operation not allowed"
    
    def cancel(self):
        self.atm.state = IdleState(self.atm)
        return "Transaction cancelled"

class PinState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card_number):
        return "Operation not allowed"

    def enter_pin(self, pin):
        if self.atm.cards.get_card(self.atm.card_number).pin == pin:
            self.atm.state = TransactionState(self.atm)
            return "Pin accepted"
        else:
            self.atm.state = IdleState(self.atm)
            print("Invalid pin")
    
    def check_balance(self):
        return "Operation not allowed"
    
    def withdraw(self, amount):
        return "Operation not allowed"
    
    def change_pin(self, new_pin):
        return "Operation not allowed"
    
    def cancel(self):
        self.atm.state = IdleState(self.atm)
        return "Transaction cancelled"

class TransactionState(ATMState):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, card_number):
        return "Operation not allowed"

    def enter_pin(self, pin):
        return "Operation not allowed"

    def check_balance(self):
        balance = self.atm.cards.get_card(self.atm.card_number).check_balance()
        self.atm.state = IdleState(self.atm)
        return f"Your balance is {balance}"

    def withdraw(self, amount):
        msg = self.atm.cards.get_card(self.atm.card_number).withdraw(amount)
        self.atm.state = IdleState(self.atm)
        return msg

    def change_pin(self, new_pin):
        msg = self.atm.cards.get_card(self.atm.card_number).change_pin(new_pin)
        self.atm.state = IdleState(self.atm)
        return msg
    
    def cancel(self):
        self.atm.state = IdleState(self.atm)
        return "Transaction cancelled"
    
class ATM:
    _instance = None
    
    @staticmethod
    def get_instance():
        if not ATM._instance:
            ATM._instance = ATM()
        return ATM._instance
    
    def __init__(self):
        self.cards = Cards()
        _instance = self
        self.state = IdleState(self)
    
    def insert_card(self, card_number):
        self.state.start_operation()
        return self.state.insert_card(card_number)
    
    def enter_pin(self, pin):
        return self.state.enter_pin(pin)
    
    def check_balance(self):
        return self.state.check_balance()
    
    def withdraw(self, amount):
        return self.state.withdraw(amount)
    
    def change_pin(self, new_pin):
        return self.state.change_pin(new_pin)
    
    def cancel(self):
        return self.state.cancel()
    
atm = ATM.get_instance()
card = Card("1234", "1234", 1000)
atm.cards.add_card(card)
print(atm.insert_card("1234"))
print(atm.enter_pin("134"))
print(atm.check_balance())
print(atm.withdraw(500))
print(atm.cancel())
