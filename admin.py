class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, user):
        self.bank.create_account(user)

    def check_bank_balance(self):
        self.bank.check_bank_balance()

    def check_total_loan_amount(self):
        self.bank.check_total_loan_amount()

    def disable_loan_features(self):
        self.bank.loan_status = False
        
    def enable_loan_features(self):
        self.loan_status = True
