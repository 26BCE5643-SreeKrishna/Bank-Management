from bank_account_class import BankAccount
from accounts import account 1

valid = False

num = int(input("Enter account number:"))
if num == 1001:
  print('Hello Rahul. Please enter your password')
  passs=input()
  if not account1.password_verify(passs):
    print ('Incorrect password.')
    valid = False
  else:
    valid = True
  
if valid:
  print("--- BANK MANAGEMENT SYSTEM ---")
  print("1. Display Account Details")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Check Balance")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    account1.display_details()

  elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    account1.deposit(amount)

  elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))
    account1.withdraw(amount)

  elif choice == "4":
    account1.display_balance()

  elif choice == "5":
    print("Thank you for using the Bank Management System.")

  else:
    print("Invalid input.")
else:
  print('Try later')