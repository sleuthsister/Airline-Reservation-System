import csv,os
import mysql.connector
from tabulate import tabulate
import time
import random
from datetime import datetime


def create(filename,h):                                                       #creates a new csv file
        f=open(filename,"w",newline="") 
        w=csv.writer(f)
        w.writerow(h)
        f.close()

pass1=input("enter sql pass:")
obj=mysql.connector.connect(host="localhost",user="root",password=pass1)
h=[["Welcome to the Airmiles Customer Loyalty Program"]]
print(tabulate(h,tablefmt='grid'))
print()
print("Select options to view, redeem and deposit AIRPOINTS")
print()
def makeacc():
    c=obj.cursor()
    c.execute("USE AIRMILES")
    f1=open("password.csv","a",newline="")
    w=csv.writer(f1,delimiter=",")
    print("Membership options available:")
    print("1.Blue Rewards")
    print("2.Silver Rewards")
    print("3.Gold Rewards")
    print("4.Platinum Rewards")
    letter=input("enter membership (B/S/G/P):").upper()
    acno=letter+str(random.randint(1,10000))
    b=input("enter name:")
    ap=eval(input("enter AIRPOINTS:"))
    pp=input("enter passport no:")
    dob=input("Enter dob in yyyy-mm-dd format:")
    pas=input("Set a password to access your account:")
    T=(acno,b,ap,pp,dob)
    l=[acno,b,pas]
    q="INSERT INTO AIRMILE VALUES(%s,%s,%s,%s,%s)"
    c.execute(q,T)
    obj.commit()
    w.writerow(l)
    print("Your Airmiles account has been successfully created!")
    print("Airmiles number:",acno)
    c.close()
    f1.close()

def forgotpas():
        c=obj.cursor()
        print("Forgot password? change your password here:")
        n=input("enter username:")
        e=input("enter airmile no.:")
        f1=open("password.csv","r",newline="")
        r=csv.reader(f1,delimiter=",")
        pole=0
        for i in r:
                if i[0]==e and i[1]==n:
                        pole=1
        f1.close()
        if pole==0:
                print("Oops! User not found")
                return()
        
        pn=input("enter new password:")
        pn1=input("Re-enter password to change:")
        
        flag=0
        if pn==pn1:
                ans=input("Are you sure you want to change your password?")
                if ans=="yes":
                        flag=1
                else:
                        print("Password not updated")
        else:
                print("Re-entered password does not match")
                
        if flag==1:
                f=open("password.csv","r",newline="")
                f1=open("upass.csv","w",newline="")
                w=csv.writer(f1,delimiter=",")
                r=csv.reader(f,delimiter=",")
                a=[]
                line=0
                h=["AIRMILENO","NAME","PASSWORD"]
                w.writerow(h)
                for i in r:
                        if line!=0:
                                if i[0]==e and i[1]==n:
                                        flag=2
                                        a=[i[0],i[1],pn1]
                                        w.writerow(a)
                                else:
                                        w.writerow(i)
                        line+=1
                f1.close()
                f.close()
                os.remove("password.csv")
                os.rename("upass.csv","password.csv")
                h=[["Password updated successfully!"]]
                print(tabulate(h,tablefmt='grid'))
        c.close()
                        

def viewacc():
    print("To view your Airmiles account, Login:")
    h=[["LOGIN"]]
    print(tabulate(h,tablefmt='grid'))
    fp=input("Forgot password?")
    if fp=="yes":
            forgotpas()
    login=input("Do you want to LOGIN to your AIRMILES ACCOUNT?")
    pole=0
    if login=="no":
            pole=1

            
    print()
    if pole==0:
            h=[["LOGIN"]]
            print(tabulate(h,tablefmt='grid'))
            flag=0
            c=obj.cursor()
            c.execute("USE AIRMILES")
            usn=input("enter username:")
            pas=input("enter password:")
            f1=open("password.csv","r",newline="")
            r=csv.reader(f1,delimiter=",")
            for i in r:
                    if i[1]==usn and i[2]==pas:
                            flag=1
            if flag==0:
                    print("invalid Login ID or Password")
            else:
                    print("Login Successfull")
                    c.execute("SELECT * FROM AIRMILE")
                    d=datetime.today()
                    da=datetime.isoformat(d)
                    date=da[:10]
                    tym=da[11:19]
                    print("Login Time:",tym)
                    print("Login Date:",date)
                    for i in c:
                            if i[1]==usn:
                                    print("Loading Details...")
                                    time.sleep( 3 )
                                    print("--------------------------------------------")
                                    print("Account details")
                                    print()
                                    print("Account number is",i[0])
                                    print("Name of account holder is",i[1])
                                    print("Total AIRPOINTS in the account is",i[2])
                                    print()
                                    print("--------------------------------------------")
                                    time.sleep(1)
            f1.close()
            c.close()
    
def depacc():
    c=obj.cursor()
    c.execute("USE AIRMILES")
    ap=0
    ref=input("enter airmile number:")
    de=eval(input("enter amount to deposit:"))
    c.execute("SELECT * FROM AIRMILE")
    for i in c:
        if i[0]==ref:
            ap=i[2]
            print("Your current balance is",ap)
            
    co=input("Are you sure you want to deposit AIRPOINTS?")
    if co=="yes":
        ap+=de
        T=(ap,ref)
        q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
        c.execute(q,T)
        obj.commit()
        print("Deposit successful")
        print("Your current balance is",ap)
    else:
        obj.rollback()
    c.close()

def redeem(r,ref):
    c=obj.cursor()
    c.execute("USE AIRMILES")
    
    de=r
    flag=0
    c.execute("SELECT * FROM AIRMILE")
    for i in c:
        if i[0]==ref:
            ap=i[2]
            flag=0
        else:
                flag=1
    if flag==1:
            break
    if ap<de:
        print("Insufficient balance")
        print("Your current balance is",ap)
    else:
        co=input("Are you sure you want to redeem AIRPOINTS?")
        if co=="yes":
            ap-=de
            T=(ap,ref)
            q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
            c.execute(q,T)
            obj.commit()
            print("Amount redeemed successfully")
            print("Your current balance is",ap)
        else:
            obj.rollback()
    c.close()
    
def plounge():
        print("PAID LOUNGE ACCESS")
        a=input("enter airmile no:")
        if a[0]=="B":
            redeem(250,a)
            
            
        elif a[0]=="S":
            redeem(300,a)
            
            
        elif a[0]=="G":
            redeem(400,a)
            

        elif a[0]=="P":
            redeem(500,a)


def deleteair():
    c=obj.cursor()
    c.execute("USE AIRMILES")
    n=input("enter airmile number:")
    u=input("enter username:")
    p=input("enter password:")
    f1=open("password.csv","r")
    r=csv.reader(f1,delimiter=",")
    flag=0
    for i in r:
        if i==[n,u,p]:
            flag=1
    f1.close()
    if flag==0:
        print("Invalid username/Account is not created")
    else:
        T=(n,)
        c.execute("SELECT * FROM AIRMILE WHERE AIRMILENO=%s",T)
        for i in c:
            ap=i[2]
        ans=input("Are you sure you want to delete your Airmiles account?").lower()
        if ans=="yes":
            print("Airpoints available:",ap)
            cp=input("Do you want to convert your AIRPOINTS to AED?").lower()
            print("NOTE: AIRPOINTS below 1000 can not be convertd to AED")
            if cp=="yes":
                if ap<1000:
                    print("Sorry can not convert AIRPOINTS")
                else:
                    print("AED",ap/100,"to be collected from the AIRMLES counter at your airport")
            c.execute("DELETE FROM AIRMILE WHERE AIRMILENO=%s",T)
            obj.commit()
            print("Account deleted succesfully")
            f1=open("password.csv","r")
            f2=open("newpass.csv","w",newline="")
            r=csv.reader(f1,delimiter=",")
            w=csv.writer(f2)
            for i in r:
                if i[1]!=u:
                        w.writerow(i)   
            f2.close()
            f1.close()
            os.remove("password.csv")
            os.rename("newpass.csv","password.csv")
    c.close()
                
                
                        
    
while True:
    print()
    print("1.Create database,table and csv file")
    print("2.Create my Airmiles account")
    print("3.View my Airmiles account")
    print("4.Deposit my AIRPOINTS")
    print("5.Redeem my AIRPOINTS")
    print("6.Paid Lounge Access")
    print("7.Change password")
    print("8.Delete my Airmile acount")
    print("9.Exit")
    choice=eval(input("eneter your choice:"))
    print()
    if choice==1:
        c=obj.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS AIRMILES")
        c.execute("USE AIRMILES")
        c.execute("CREATE TABLE IF NOT EXISTS AIRMILE(AIRMILENO VARCHAR(8),NAME VARCHAR(15),AIRPOINTS INTEGER,PASSPORTNO VARCHAR(15),DOB DATE)")
        c.close()
        create('password.csv',['airmileno','username','password'])
    elif choice==2:
        makeacc()
    elif choice==3:
        viewacc()
    elif choice==4:
        depacc()
    elif choice==5:
        ref=input("enter airmile no:")
        de=eval(input("enter how many points to redeem:"))
        redeem(de,ref)
    elif choice==6:
        plounge()
    elif choice==7:
        forgotpas()
    elif choice==8:
        deleteair()
    else:
        h=[["Thank You for choosing the Airmiles Customer Loyalty Program"],["Airmiles, Fly high"]]
        print(tabulate(h,tablefmt='grid'))
        break
    _cntnue=input("press enter to continue..")
    print()
    
