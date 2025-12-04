# Static Method (Define static method)
# Answer: Static method is a method that belongs to a class rather than an instance of a class
# Problem: Add a static method to the Car class that returns a general description of a car.

class Bank:
    def __init__(self):
        self.name = None
        self.account = None
        self.__balance = 0


    def set_account(self, name, account, balance):
        self.name = name
        self.account = account
        self.__balance = balance
        print(f'Mr./Mrs. {name} your account created successfully')
        return None

    def set_deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'NRs. {amount} your account deposited successfully'
        else:
            return f'NRs. {amount} your account deposited failed, please try again'

    def set_withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount
            print(f'NRs. {amount} your account withdrawn successfully, remaining balance: {self.__balance}')
            return None
        else:
            return f'NRs. {amount} your account withdrawn failed, please try again'

    def get_balance(self):
        return f'Your balance: {self.__balance}'

    def get_my_account(self):
        return f'Account Holder Name: {self.name} \nAccount Number: {self.account}'

    @staticmethod
    def general_info():
        return "A bank account allows secure deposit and withdrawal of funds."

account1 = Bank()

account1.set_account("Bijay Budha", 983627362, 10000)
print(account1.get_my_account())
account1.set_deposit(20000)
print(account1.get_balance())
account1.set_withdraw(15000)

# Static Method
print(account1.general_info())