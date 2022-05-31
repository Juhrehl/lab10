#atm program
import datetime

#getting pin
print ("Enter your pin: ")
upin = int(input())

f = open("pin.txt", "r")
fpin = int(f.read())

#menu
if upin == fpin:
  print("Pin is valid")
  f = open ("balance.txt", "r")
  balance = int(f.read())
  f.close()
  print ("Your current balance is $",balance)
  print ("1. Withdraw 2. Deposit")
  n = int(input())
else:
  print ("Pin invalid, please try again")

#withdraw
if n == 1:
  print ("Enter the amount to withdraw ")
  amount = int(input())
  balance = balance - amount
  message = "\nwithdrawed $"  + str(amount)
  
#deposit
elif n == 2:
  print ("Enter the amount to deposit")
  amount = int(input())
  balance = balance + amount
  message = "\ndeposited $" + str(amount)
  
f = open("balance.txt", "w")
f.write(str(balance))
f.close()

#logfile
message = message + "at" + str(datetime.datetime.now())
f = open("logfile.txt", "a")
f.write(message)
f.close()


#change pin on pin.txt
#view logfile on logfile.txt