from typing import Any, SupportsIndex


class User:
    def __init__(self, name, email_id=""):
        self.name = name
        self.email_id = email_id

class UserService:
    _instance = None

    @staticmethod
    def get_instance():
        if not UserService._instance:
            UserService._instance = UserService()
        return UserService._instance
    
    def __init__(self):
        self.users = []
        self._instance = self

    def create_user(self, name, email_id):
        user = User(name, email_id)
        self.users.append(user)
        return user

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
    
class Group:
    def __init__(self, group_name) -> None:
        self.group_name = group_name
        self.users = []
        self.balance = Balance()

class GroupService: 
    _instance = None

    @staticmethod
    def get_instance():
        if not GroupService._instance:
            GroupService._instance = GroupService()
        return GroupService._instance
    
    def __init__(self):
        self.groups = []
        self.userService = UserService.get_instance()
        self._instance = self

    def create_group(self, group_name):
        group = Group(group_name)
        self.groups.append(group)
        return group

    def add_user_to_group(self, group_name, user_name):
        user = self.userService.get_user(user_name)
        if user:
            for group in self.groups:
                if group.group_name == group_name:
                    group.users.append(user)
                    print(f"User {user_name} added to group {group_name}")
                    group.balance.group_balance[user_name] = 0
                    return
        print("User or Group not found")

    def get_group(self, group_name):
        for group in self.groups:
            if group.group_name == group_name:
                return group
        return None

class Balance:
    def __init__(self) -> None:
        self.group_balance = {}

class ExpenseService:
    _instance = None

    @staticmethod
    def get_instance():
        if not ExpenseService._instance:
            ExpenseService._instance = ExpenseService()
        return ExpenseService._instance
    
    def __init__(self):
        self.groupService = GroupService.get_instance()
        self._instance = self

    def add_expense_to_group(self, group_name, user_paid, user_split_list, total_anount):
        group = self.groupService.get_group(group_name)
        if group:
            for user in user_split_list:
                group.balance.group_balance[user] -= total_anount/len(user_split_list)
            group.balance.group_balance[user_paid] += total_anount
            print(f"Expense added to group {group_name}")
        else:
            print("Group not found")

    def simplify_group_debts(self, group_name):
        group = self.groupService.get_group(group_name)
        balance_map = group.balance.group_balance
        balances = [[balance_map[user], user] for user in balance_map]

        balances.sort()
        l, r = 0, len(balances) - 1

        while l < r:
            debit, credit = balances[l][1], balances[r][1]
            amount = min(-balances[l][0], balances[r][0])
            balances[l][0] += amount
            balances[r][0] -= amount

            print(f"{debit} pays {amount} to {credit}")

            if balances[l][0] == 0:
                l += 1
            if balances[r][0] == 0:
                r -= 1

class System:
    _instance = None

    @staticmethod
    def get_instance():
        if not System._instance:
            System._instance = System()
        return System._instance
    
    def __init__(self) -> None:
        self.userService = UserService.get_instance()
        self.groupService = GroupService.get_instance()
        self.expenseService = ExpenseService.get_instance()
        self._instance = self

    def create_user(self, name, email_id):
        self.userService.create_user(name, email_id)

    def create_group(self, group_name):
        self.groupService.create_group(group_name)

    def add_user_to_group(self, group_name, user_name):
        self.groupService.add_user_to_group(group_name, user_name)

    def add_expense_to_group(self, group_name, user_paid, user_split_list, total_anount):
        self.expenseService.add_expense_to_group(group_name, user_paid, user_split_list, total_anount)

    def simplify_group_debts(self, group_name):
        self.expenseService.simplify_group_debts(group_name)


# test  
system = System.get_instance()
user1 = system.create_user("user1", "user1@gmail.com")
user2 = system.create_user("user2", "user2@gmail.com")
user3 = system.create_user("user3", "user3@gmail.com")


group1 = system.create_group("group1")

system.add_user_to_group("group1", "user1")
system.add_user_to_group("group1", "user2")
system.add_user_to_group("group1", "user3")

system.add_expense_to_group("group1", "user1", ["user2", "user3"], 100)
system.add_expense_to_group("group1", "user2", ["user1", "user3"], 200)
system.add_expense_to_group("group1", "user3", ["user1", "user2", "user3"], 300)

system.simplify_group_debts("group1")
