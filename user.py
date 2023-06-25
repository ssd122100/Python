class User:
    def __init__(self,name,email,nid,initial_amount):
        self.name = name
        self.email = email
        self.__password = None
        self.__nid = nid
        self.balance = initial_amount
        self.account_no = None
        self.loan_balance = 0
        self.total_balance =initial_amount
        self.transaction_history =[]

    def set_password(self):
        password = input('please enter your password:')
        n =len(password)     
        if n>=8:
            password2 = input('Please re_enter your password:')
            if password == password2:
                self.__password = password
         
    def Create_an_account(self,bank):
        bank.create_an_account(self)

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            self.total_balance += amount
            self.transaction_history.append(f'deposit:{amount}')
        else:
            print('Please deposit a valid amount')

    def withdraw(self,amount):
        if self.balance >= amount:
            print(f'please collect your money : {amount}')
            self.balance -= amount
            self.total_balance -= amount
            self.transaction_history.append(f'withdraw :{amount}')
            return 1
        
        else:
            print('you do not have sufficient balance')
            return 0

    def check_balance(self):
        print(f'your Main account balance is : {self.balance}')
        print(f'your loan account balance is : {self.loan_balance}')
        print(f'your total account balance is :{self.total_balance}')

    def check_transaction_history(self):
        if(len(self.transaction_history)):
            print(f'------------Transaction history for {self.name}------------')
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print(f'No transaction history is available for {self.name}')
     
    def take_loan(self,amount):
        max_limit = (self.balance - self.loan_balance)

        if amount <=max_limit:
           
            self.loan_balance = amount
            self.total_balance += amount
            self.transaction_history.append(f'loan taken :{amount}')
            print(f'your request for loan {amount} taka has been granted successfully')
            return 1
        else:
            print('you exceeded your limit')
            return 0

    def transfer_money(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_balance -= amount
            self.transaction_history.append(f'Transfer money :{amount}')
        else:
            print('you do not have sufficient money')





