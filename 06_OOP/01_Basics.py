def first_func(acc_num):
    def second_func(balance):
        return f'Account number: {acc_num}, Balance: NRs. {balance}'
    return second_func

user1 = first_func(10092383)
print(user1(10238))

