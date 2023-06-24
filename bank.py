class Bank:
    def __init__(self,name):
        self.name = name
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.current_balance =0
        self.loan_status = True

    def create_an_account(self,user):
        account_no = 1001 + len(self.accounts)
        user.account_no = account_no
        self.total_balance += user.balance
        self.current_balance += user.balance
        self.accounts[account_no] = user
        print(f'Account Created successfully. your acount No is {account_no}')

    def deposit(self,account_no,amount):
        if account_no in self.accounts:
            self.accounts[account_no].deposit(amount)
            self.total_balance += amount
            self.current_balance += amount
            print(f'{amount} taka deposited successfully')
        else:
            print('Invalid account_no')
    
    def check_balance(self,account_no):
        if account_no in self.accounts:
            self.accounts[account_no].check_balance()
            
    def withdraw(self,account_no,amount):
        if account_no in self.accounts:
            if  self.current_balance >= amount:
                x= self.accounts[account_no].withdraw(amount)
                if x:
                    self.current_balance -= amount
                    self.total_balance -= amount
                
            else:
                print('bank is bankrupt')

    def Transfer(self,from_account_no, to_account_no,amount):
        if from_account_no in self.accounts and to_account_no in self.accounts:
            if self.accounts[from_account_no].balance >=amount:
                self.accounts[from_account_no].transfer_money(amount)
                self.accounts[to_account_no].deposit(amount)
            else:
                print('user has don\'t enough money')
        else:
            print('Invalid account no')
    
    def give_loan(self,account_no,amount):
        if self.current_balance >= amount and self.loan_status:
            if account_no in self.accounts:
                x = self.accounts[account_no].take_loan(amount)
                if x:
                    self.total_loan_amount += amount
                    self.current_balance = self.total_balance - self.total_loan_amount
        else:
            print('loan application has been denied')

    def check_bank_current_balance(self):
        print(f"Total available balance in the bank: {self.current_balance}")

    def check_total_balance(self):
        print(f'Total balance in the bank :{self.total_balance}')

    def check_total_loan_amount(self):
        print(f"Total loan amount in the bank: {self.total_loan_amount}")

    def __repr__(self) -> str:
        print(f'Bank name : {self.name}  Total Money : {self.total_balance} current Money : {self.current_balance} Loan given: {self.total_loan_amount} Total User : {len(self.accounts)}')
        return ''

    def Transaction_history(self,account_no):
        if account_no in self.accounts:
            self.accounts[account_no].check_transaction_history()
        else:
            print('Invalid account no')      



