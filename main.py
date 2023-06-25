from bank import Bank
from user import User
from admin import Admin

def main():
    Brac = Bank('Brac Bank')
    ssd = User('SSD','ssd@gmail.com',12334565,50000)
    ps = User('Ps','ps@gmail.com',54321,40000)
    admin = Admin(Brac)
    Brac.create_an_account(ssd)
    Brac.create_an_account(ps)
    Brac.deposit(1001,30000)
    Brac.deposit(1002,20000)
   
    Brac.give_loan(1001,15000)
   
    Brac.Transfer(1001,1002,20000)
    Brac.Transaction_history(1001)
    Brac.check_balance(1001)
    Brac.give_loan(1002,20000)
    Brac.withdraw(1001,50000)
    admin.disable_loan_features()
    Brac.give_loan(1002,20000)
    Brac.withdraw(1001,50000)
    admin.check_total_loan_amount()
    print(Brac)
    mi = User('MI','mi@gmail.com',65748392,30000)
    mi.Create_an_account(Brac)
    
if __name__ == '__main__':
    main()
