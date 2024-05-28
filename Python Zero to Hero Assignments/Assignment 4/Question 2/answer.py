class BankAccount:
    def __init__(self, initial_balance):
        assert initial_balance >= 0, "Assertion Error"
        self.balance = initial_balance

initial_balance = int(input())
try:
    account = BankAccount(initial_balance)
    print("Assertion Passed")
except AssertionError as e:
    print(e)