class Bank:
    def __init__(self):
        pass

    def set_account(self, acc, name, balance):
        self.__acc = acc
        self.__name = name
        self.__balance = balance
    
    def _get_balance(self): # This is a private function (attribute)
        return f'Your Total Deposit: {self.__balance}'
    
    def set_deposit(self, deposit_amount):
        self.__balance += deposit_amount

    def __get_my_account(self):
        return f'Account Holder Name: {self.__name}\nAccount Number: {self.__acc}\nTotal Balance: {self.__balance}'

bank = Bank()

bank.set_account("Bijay Budha", "94820482029", 9836)
print(bank._get_balance())
bank.set_deposit(10000)
print(bank._get_balance())
print(bank._Bank__get_my_account())
    


        



