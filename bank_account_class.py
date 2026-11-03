class BankAccount:
  def __init__(self, account_holder, account_number,passs, balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.balance = balance
    self.password = passs

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print("Amount deposited successfully.")
    else:
      print("Invalid deposit amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= amount
      print("Amount withdrawn successfully.")
    else:
      print("Insufficient balance or invalid amount.")
      
  def display_balance(self):
    print("Current Balance:", self.balance)

  def display_details(self):
    print("Account Holder:", self.account_holder)
    print("Account Number:", self.account_number)
    self.display_balance()

  def password_verify(self,passs):
    return self.password == passs