from logging import exception
from multiprocessing.sharedctypes import Value
# from datetime import datetime
import time
import random
import datetime
import os

s=3
ter=0
name=[] 
Val=0
lo=0
index=0
tranam=0
Accountno=[]
Password=[]
Depo=[]
Atm=[]
Cvv=[]
atmpin=[]
os.system("cls")

#following code for through atm widthraw
def atmw():
  try:
   l=input("Enter Atm Pin No ==> ")
   for i in range(index):
    if(l==atmpin[i]):
      amount=int(input("Enter Amount ==> ")) # this is for cash widthrawing through atm card
      print("Your Debited Amount is ==> ",amount)
      Depo[i]=Depo[i]-amount
   f=input("Press Enter key for balance checking ==> ")
   if(f==''):
    Displayac()
  except:
    print("ATM Card has not Created")
    atm()

#following code for atm card 
def atm():
  global index
  print("             ATM Card           ")
  at=input("Press 'Enter' Key For ATM Card Generating ==> ")
  if(at==''):
    for i  in range (index):
      Atm.append(0)
      Cvv.append(0)
      atmpin.append(0)
      atm=random.randint(123456789230,150089430987) #this is for atm card number generating
      cvv=random.randint(145,577) #this is for cvv number generating
      Atm[i]=atm
      Cvv[i]=cvv
      print("Your ATM Card Number is ==> ",atm)
      print("Your Cvv Number ==>  ",cvv)
      d=datetime.date(2028,8,10)
      print("Expiry Date : ",d)
      a=(input("Set Your Password ==> ")) #this is for atm card password setting
      atmpin[i]=a
      print("Your Atm Password is ==> ",atmpin[i])
    c=input("Press 'Enter' For Balance Checking ==> ") #function calling for balance checking
    os.system("cls")
    displaydetails()
    if(c==''):
      balance_Checking()


# display Account Details
def displaydetails():
  global index
  print("                 Paytm Payment BANK                 ")
  for i in range (index):
    print("Account Holder's Name ==> ",name[i])
    print("Account Number ==> ",Accountno[i])
#display Amount in your account
def Displayac():
  global index
  temp=0
  displaydetails()
  k=input("Enter Your Account No ==> ") 
  for i in range (index): 
    if(k==Accountno[i]):
      print("The Amount in your Account is ==> ",Depo[i])
      temp=1   # here,this is for amount checking in account
      break
  if(temp==0):
    os.system("cls")
    print("Something Went to Wrong ")
    Displayac()
  w=input("Enter 'o' For exit ")
  if(w=='o'):
    print("Thankyou!!!")


#Following code for Cash Widthraw
def cashwidthraw():
  global index
  global Val
  print("                Here,You Can Widthraw Your Money            ")
  k=input("Enter Account Number ==> ")
  pa=input("Enter Password ==> ")
  for j in range(index):
    if(k==Accountno[j] and pa==Password[j]):
        amount=int(input("Enter Amount ==> "))   #this code for cash widthraw 
        print("Your Debited Amount is ==> ",amount)
        Depo[j]=Depo[j]-amount
  che=input("Press Enter Key For Balance Checking ") #this is for balance checking
  if(che==''):
     os.system("cls")
     Displayac()   
     

#Following Code for money transfer
def transfer():
  global index,tranam
  tr=input("Enter the Sender Account Number ==> ")
  try:
     for i in range(index):
       if(tr==Accountno[i]):
        tranam=int(input("Enter the Amount ==> ")) #this is for sender account
        Depo[i]=Depo[i]-tranam
        print("Rest Amount ==> ",Depo[i])
     re=(input("Enter Reciever Account no ==> "))
     for i in range(index):
      if(re==Accountno[i]):
       Depo.append(0)         #this is for reciver account
       Depo[i]=Depo[i]+tranam
       break
  except: 
    print("Inalid Input")
    transfer()

  temp=input("'Enter' For Balance Checking ")
  if(temp==''):
    os.system("cls")
    # displaydetails()
    Displayac()

# Following code for Money Deposite
def Deposite():
 global Val
 global index
 temp=0
 print("               Here,You Can Deposite Your Money          ")
 e=(input("Enter The account no ==> "))
 f=(input("Enter The Password ==> "))
 try:
  for i in range (index):
    Depo.append(0)
    if(e==Accountno[i] and f==Password[i]):
      a=int(input("Enter Deposite Amount ==> "))
      Depo[i]=a
      os.system("cls")      # this code for money deposite in account
      displaydetails()
      print("DEPOSITE AMOUNT ==> ",Depo[i])
      Val=Depo[i]
      temp=1
      break
 except:
   print("   INVALID AMOUNT   ")
   os.system("cls")
   displaydetails()
   Deposite() 
 temp=input("\nFor CashWidthraw Through Account No Press Enter Key\t Press For 'm' Key For Money Transfer\nEnter 'n' For Another Account Opening\tFor Exit Press 'o'\nFor CashWidthraw through ATM Card Press 't' ") #this is for instruction
 if(temp==''):
  os.system("cls")
  displaydetails()
  cashwidthraw()
 if(temp=='t'):
   os.system("cls")
   displaydetails()
   atmw()
 if(temp=='m'):
  os.system("cls")
  displaydetails()
  transfer()
 if(temp=='n'):
  os.system("cls")
  displaydetails()
  opening_account()
 if(temp=='o'):
  os.system("cls")
  displaydetails()
  print("Thankyou!!!")


#Following code for balance checking
def balance_Checking():
    global index
    global Val
    temp=0
    print("                       Here,You Can Check Balance                      ")
    t=input("  Enter Your Account Number ==> ")
    p=input("  Enter Your Password ==> ")
    for i in range(index):
      if(t==Accountno[i] and p==Password[i]):
          os.system("cls")
          print("         The Amount in Your Account is ==> ",Val) #this code for showing balance 
                                                               # in acccount
          temp=1
          break
    if(temp==0):
      os.system("cls")
      displaydetails()
      print("Something Went to Wrong ")
      balance_Checking()
   
    dep=input("\nFor Money Deposite Press 'd'\tFor Cash Widthraw Press 'Enter' Key\nFor Money Transfer Press 'm'\t For Exit Press 'o'\nFor New Account Opening Press 'n' ") #this is for    instruction
    if(dep=='d'):
        os.system("cls")
        displaydetails()
        Deposite()
    if(dep==''):
        os.system("cls")
        displaydetails()
        cashwidthraw()
    if(dep=='m'):
      os.system("cls")
      displaydetails()
      transfer()
    if(dep=='n'):
      os.system("cls")
      displaydetails()
      opening_account()
    if(dep=='o'):
      os.system("cls")
      displaydetails()
      print("Thankyou!!")


#Following Code for user login       
def Login():
  global index,Val,ter
  global s
  temp=0
  if(ter==3):
   os.system("cls")
   print("      \n\n     Your Account Has Been Blocked     \n\n")
   print("Now,Your are on Main Menu ") #this is for account blocking after three times try
   opening_account()
   return 0
  print("Please Login Your Account ==> ")
  b=input("Enter The account no ==> ")
  c=input("Enter The Password ==> ")
  for k in range(index):
      if(b==Accountno[k] and c==Password[k]):
        os.system("cls")
        displaydetails()
        print("Your Account is Successfully Login")
        temp=1
        break

  if(temp==1): 
    l=input("Do You Want To Create ATM Card Press 'y' Otherwise Press 'n' ")
    if(l=='y'):
      atm()
    if(l=='n'):
      l1=input("\nFor Balance Checking Press 'b' ")
      if(l1=='b'):
       os.system("cls")
       displaydetails()
       Val=0
       balance_Checking()
  if(temp==0):
     os.system("cls")
     displaydetails()
     print("Something Went to Wrong\n")
     s=s-1
     print(s,"Chance Left ")
     ter=ter+1
    
     Login()   


#following code for account opening
def opening_account():
  global index
  global lo
  ch=(input("For Account Opening Press 'Enter' Key "))
  os.system("cls")
  displaydetails()
  if(ch==''):
     for i in range(lo,25):
         print("--------------------------------------------------------")
         
         account=str(random.randint(12334567891,45234567899)) #this is for random account generating
         Accountno.append(account)
         print("Your Account Number is ==> ",account)
         nam=input("Enter The Account Holder's Name ==> ")
         name.append(nam)
         passw = input("Enter Your password ==> ") #this is for new password
         s=passw
         Password.append(passw)
         lo=lo+1
         index=lo
         
         break
     
     if(s==''):
      os.system("cls")
      print("   Invalid Password,Please Try Again   ")
      opening_account()
     b=input("Press 'Enter' Key for Login ")
     if(b==''):
      os.system("cls")
      displaydetails()
      Login()




# datetime object containing current date and time
current=datetime.datetime.now()
print("now =",current)

#following code for system information 
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:"+IPAddr)


opening_account() #Function Calling for new account opening
