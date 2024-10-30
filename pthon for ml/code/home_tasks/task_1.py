class account:
    def __init__(self,amount) -> None:
        self.amount=amount
        
    def bank_account(self,balance):
        def deposit(amount):
            nonlocal balance
            balance +=amount
            print(f'Deposited {amount}. New balance: {balance}')

        def withdraw(amount):
            nonlocal balance
            if amount > balance:
                print('Insufficient funds')
            else:
                balance -= amount
                print(f'Withdrew {amount}. New balance: {balance}')

        def check_balance():
            print(f'Current balance: {balance}')

        return deposit, withdraw, check_balance

    # Usage
    
    
    
c=account(0)
deposit, withdraw, check_balance =c.bank_account(100)
deposit(50)
withdraw(30)
check_balance()
