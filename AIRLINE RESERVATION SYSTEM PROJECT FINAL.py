import csv,random,os,pickle,time
from tabulate import tabulate
from datetime import date
from datetime import datetime
import mysql.connector

pass1=input("enter sql pass:")
obj=mysql.connector.connect(host="localhost",user="root",password=pass1)

def checkref(refno,file):                                             #checks if refno exists in the inputted csv file
    f1=open(file,'r')
    r=csv.reader(f1)
    flag=0
    for i in r:
        if i[0]==refno:
            flag=1
    f1.close()
    if flag==0:
        return 'no'
    else:
        return 'yes'

def getlist(refno,file):                                             #returns list of details for inputted refno
    f1=open(file,'r')
    r=csv.reader(f1)
    flag=0
    for i in r:
        if i[0]==refno:
            return i
    f1.close()

def cost():  
        f1=open("seat.csv","r")                                          #Payment
        r=csv.reader(f1)
        line=0
        cost=0
        ref=input("enter reference number of passenger:")
        for i in r:
            if line!=0:
                if ref==i[0]:
                    if i[1]=="first":
                        cost=cost+19000
                    elif i[1]=="business":
                        cost+=10000
                    elif i[1]=="economy":
                        cost+=4500
                    d1=i[1]
                    d2=i[4]
                    d3=i[2]+i[3]
                    d4=i[5]
                        
            line+=1
        print("\n")
        print("--------------------TICKET-------------------")
        print("\n")
        print("Name of passenger:",d4)
        print("Class chosen:",d1)
        print("Meal chosen:",d2)
        print("Seat chosen:",d3)
        print("Amount to be paid is AED",cost)
        print("\n")
        print("--------Thank you and enjoy your flight------")
        print("\n")               
        print("\n")
        f1.close()    
              

                
def create(filename,h):                                                       #creates a new csv file
        f=open(filename,"w",newline="") 
        w=csv.writer(f)
        w.writerow(h)
        f.close()

def book(n):                                                                    #Booking flight
    f=open("booking.csv","a",newline="")
    w=csv.writer(f)
    for i in range(n):
        refno=random.randint(1,12345678)
        fna=input("Enter first name of passenger"+str(i+1)+":")
        lna=input("Enter last name of passenger"+str(i+1)+":")
        ch_ad=input("child or adult:")
        dbirth=eval(input("Enter date of birth:"))
        mbirth=eval(input("Enter month of birth:"))
        ybirth=eval(input("Enter year of birth:"))
        dob=date(ybirth,mbirth,dbirth)
        print("\n")
        pno=input("Enter passport no:")
        dexp=eval(input("Enter date of passport expiry:"))
        mexp=eval(input("Enter month of passport expiry:"))
        yexp=eval(input("Enter year of passport expiry:"))
        doexp=date(yexp,mexp,dexp)
        print("\n")
        num=eval(input("Enter primary contact number:"))
        num2=eval(input("Enter second contact number:"))
        email=input("Enter primary email address:")
        email2=input("Enter secondary email address:")
        airmile=eval(input("Enter air miles number:"))
        a=input("Enter address of passenger:")
        print("\n")
        mi=input("Are you minor?")
        spn=input("Do you require special needs assistance?")
        cstat="No"
        list1=[refno,fna,lna,ch_ad,dob,pno,doexp,num,num2,email,email2,airmile,a,mi,spn,cstat]
        w.writerow(list1)
        print()
        print("Your booking has been confirmed","\n"+"Your reference number is",refno,"\n"+"Proceed to book your seat"+"\n")
    f.close()
    print()


def bookseat(fclass,seatno,seatl):                                             #books seat in the seat chart
    if fclass=='first' or fclass=='business':
        seatdict={'A':1,'B':2,'C':3,'D':4}
    elif fclass=='economy':
        seatdict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
    else:
        return 'no'
    f=open(fclass+'.csv','r')
    read=csv.reader(f)
    f2=open("bookseatnew.csv","w",newline='')
    w=csv.writer(f2)
    line=0
    flag=0
    for i in read:
        if line!=0 and seatl in seatdict:
            if i[0]==str(seatno) and i[seatdict[seatl]]=='':
                i[seatdict[seatl]]='X'
                flag=1
        w.writerow(i)
        line+=1
    f.close()
    f2.close()
    os.remove(fclass+'.csv')
    os.rename('bookseatnew.csv',fclass+'.csv')
    if flag==0:
        return 'no'
    else:
        return 'yes'
        
def cancelseat(fclass,seatno,seatl):                                             #cancels seat in the seat chart
    seatdict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
    f=open(fclass+'.csv','r')
    read=csv.reader(f)
    f2=open("cancelseatnew.csv","w",newline='')
    w=csv.writer(f2)
    line=0
    for i in read:
        if line!=0:
            if i[0]==seatno:
                i[seatdict[seatl]]=''
        w.writerow(i)
        line+=1
    f.close()
    f2.close()
    os.remove(fclass+'.csv')
    os.rename('cancelseatnew.csv',fclass+'.csv')


def seat(n):                                                                            #Seat Selection
      f1=open("seat.csv","a",newline="")
      w=csv.writer(f1,delimiter=",")
      for i in range(n):
        r=input("Enter refno:")
        answer=checkref(r,'booking.csv')
        if answer=='no':
                print(tabulate([["reference number entered is incorrect"]],tablefmt='grid'))
                break
        detlist=getlist(r,'booking.csv')
        na=detlist[1]+" "+detlist[2]
        c=input("Enter class:").lower()
        n=eval(input("Enter seat no:"))
        a=input("Enter seat letter:").upper()
        ans=bookseat(c,n,a)
        if ans=='no':
            print()
            print(tabulate([['seat not available']],tablefmt='simple'))
            print()
        else:
            m=input("Enter type of meal:")
            print()
            print("Your seat has been successfully booked")
            print("\n")
            l=[r,c,n,a,m,na]
            w.writerow(l)
      f1.close()


def upgrade():                                                                          #Upgrade Seat/Meal
    y=input('Enter reference number:')
    cw=0
    while True:
        f1=open('seat.csv','r')
        f2=open('upnew.csv','w',newline='')
        r=csv.reader(f1)
        w=csv.writer(f2)
        if cw==0:
            answer=checkref(y,'seat.csv')
            if answer=='no':
                print(tabulate([["reference number entered is incorrect"]],tablefmt='grid'))
                break
        print("1.Upgrade class")
        print("2.Change seat")
        print('3.Change seat letter')
        print('4.Change meal')
        print('5.Take me back to seat menu')
        print()
        x=eval(input('Enter choice:'))
        flags=0
        if x==5:
            break
        for i in r:
            if i[0]==y:
                if x==1:
                    olda,oldb,oldc=i[1:4]
                    a=input('Enter new class:').lower()
                    b=input('Enter new seat number:')
                    c=input('Enter new seat letter:').upper()
                    ans=bookseat(a,b,c)
                    if ans=='no':
                        print()
                        print(tabulate([['seat not available']],tablefmt='simple'))
                        print()
                        flags=1
                    else:
                        cancelseat(olda,oldb,oldc)
                        i[1:4]=[a,b,c]
                elif x==2:
                    olda,oldb,oldc=i[1:4]
                    a=input('Enter new seat number:')
                    ans=bookseat(i[1],a,i[3])
                    if ans=='no':
                        print()
                        print(tabulate([['seat not available']],tablefmt='simple'))
                        print()
                        flags=1
                    else:
                        cancelseat(olda,oldb,oldc)
                        i[2]=a
                elif x==3:
                    olda,oldb,oldc=i[1:4]
                    a=input('Enter new seat letter:').upper()
                    ans=bookseat(i[1],i[2],a)
                    if ans=='no':
                        print()
                        print(tabulate([['seat not available']],tablefmt='simple'))
                        print()
                        flags=1
                    else:
                        cancelseat(olda,oldb,oldc)
                        i[3]=a
                elif x==4:
                    a=input("Enter veg or non veg:")
                    i[4]=a
                if flags==0:
                    print("\n")
                    print(tabulate([['Details are updated']],tablefmt='grid'))
                    print("\n")
            w.writerow(i)
        f1.close()
        f2.close()
        cw+=1
        os.remove('seat.csv')
        os.rename('upnew.csv','seat.csv')

def cancel(ref,filename):                                                                   #Cancellation
    f1=open(filename,"r")
    f2=open("cbooking.csv","w",newline="")
    w=csv.writer(f2)
    r=csv.reader(f1)
    line=0
    for i in r:
        if line!=0:
            if int(i[0])!=ref:
                w.writerow(i)
        else:
            w.writerow(i)
        line+=1
    f1.close()
    f2.close()
    os.remove(filename)
    os.rename("cbooking.csv",filename)

def connecting():                                                              #Passengers on Connecting Flights
    f1=open("booking.csv","r")
    f2=open("connecting.csv","a",newline="")
    r=csv.reader(f1)
    w=csv.writer(f2)
    y=eval(input("Enter reference number:"))
    line=0
    for i in r:
        if line!=0 and int(i[0])==y:
            a=input("Enter arrival destination 2:")
            f=input("Enter connecting flight number:")
            t=input("Enter arrival time in destination 2:")
            l=[i[0],i[1]+" "+i[2],i[7],a,f,t]
            w.writerow(l)
        line+=1
    f1.close()
    f2.close()
    print()
    print("Connecting flight details recorded")
    print("\n")
                                                                                 #Display csv

def display(f):
        c1=open(f,"r")
        r=csv.reader(c1,delimiter=",")
        l=[]
        for i in r:
            l.append(i)
        c1.close()
        return l
        print("\n")
        

def boarding():                                                                 #Printing Boarding Pass
    f1=open("seat.csv","r")
    r=csv.reader(f1)
    d=datetime.today()
    da=datetime.isoformat(d)
    date=da[:10]
    time1=da[11:19]
    n=eval(input("Enter reference number to print boarding pass:"))
    line=0
    print("printing boarding pass...")
    time.sleep(3)
    for i in r:
        if line!=0 and n==int(i[0]):
            print("\n")
            print("_______________________________________________________________________________________________")
            print("\t","\t","\t","\t","\t","\t","Boarding Pass")
            print("_______________________________________________________________________________________________")
            print()
            print("ticket number:",i[0],"\t","passenger name:",i[5],"\t","date:",date)
            print()
            print("class:",i[1],"\t","\t","seat:",i[2]+i[3],"\t""\t""\t","time:",time1)
            print()
            print("meal:",i[4],"\t","\t","terminal:",terminal)
            print()
            print("Departure:",fr,"\t""\t","Arrival:",to,"\t")
            print()
            print("\t","\t","\t","\t","Enjoy your flight")
            print("_______________________________________________________________________________________________")
            print("\n")
            
        line+=1
    f1.close()

            
def checkin():                                                                               #Check in
        ref=eval(input('Enter reference number:'))
        answer=checkref(str(ref),'booking.csv')
        if answer=='no':
            print(tabulate([["reference number entered is incorrect"]],tablefmt='grid'))
                 
        else:
            f1=open('booking.csv','r')
            f2=open('newb.csv','w',newline="")
            r=csv.reader(f1)
            w=csv.writer(f2)
            line=0
            for i in r:
                if line!=0 and int(i[0])==ref:
                    i[-1]="Yes"
                    w.writerow(i)
                else:
                    w.writerow(i)
                line+=1
            f1.close()
            f2.close()
            os.remove('booking.csv')
            os.rename('newb.csv','booking.csv')
            print("\n")
            print("Check in successful")
            print("\n")

def modify():                                                                                  #modify details in booking.csv
    y=input('Enter reference number:')
    cw=0
    while True:
        f1=open('booking.csv','r')
        f2=open('modnew.csv','w',newline='')
        r=csv.reader(f1)
        w=csv.writer(f2)
        if cw==0:
            answer=checkref(y,'booking.csv')
            if answer=='no':
                print(tabulate([["reference number entered is incorrect"]],tablefmt='grid'))
                break
        print("\n")
        print("1.Edit name")
        print("2.Edit child or adult")
        print('3.Edit date of birth')
        print('4.Edit passport number and expiration date')
        print('5.Edit contact details')
        print("6.Edit minor/need special needs details")
        print("7.Edit airmile number")
        print("8.Take me back to the booking menu")
        print()
        x=eval(input('Enter choice:'))
        print("\n")                                                           
        if x==8:
            break
        for i in r:
            if i[0]==y:
                if x==1:
                    fna=input("Enter first name of passenger:")
                    lna=input("Enter last name of passenger:")
                    i[1:3]=[fna,lna]
                    print("\n")
                elif x==2:
                    ch_ad=input("child or adult:")
                    i[3]=ch_ad
                    print("\n")
                elif x==3:
                    dbirth=eval(input("Enter date of birth:"))
                    mbirth=eval(input("Enter month of birth:"))
                    ybirth=eval(input("Enter year of birth:"))
                    dob=date(ybirth,mbirth,dbirth)
                    i[4]=dob
                    print("\n")
                elif x==4:
                    pno=input("Enter passport no:")
                    dexp=eval(input("Enter date of passport expiry:"))
                    mexp=eval(input("Enter month of passport expiry:"))
                    yexp=eval(input("Enter year of passport expiry:"))
                    doexp=date(yexp,mexp,dexp)
                    i[5:7]=[pno,doexp]
                    print("\n")
                elif x==5:
                    num=eval(input("Enter primary contact number:"))
                    num2=eval(input("Enter second contact number:"))
                    email=input("Enter primary email address:")
                    email2=input("Enter secondary email address:")
                    address=input("Enter address of passenger:")
                    i[7:11]=[num,num2,email,email2]
                    i[12]=address
                    print("\n")
                elif x==6:
                    mi=input("Are you minor?")
                    spn=input("Do you require special needs assistance?")
                    i[13:15]=[mi,spn]
                    print("\n")
                elif x==7:
                    airmile=eval(input("Enter air miles number:"))
                    i[11]=airmile
                    print("\n")
                print(tabulate([['Details are successfully modified in the booking file']],tablefmt='grid'))
            w.writerow(i)
        f1.close()
        f2.close()
        cw+=1
        os.remove('booking.csv')
        os.rename('modnew.csv','booking.csv')

def create_avail():                                             #creates first.csv,business.csv and economy.
    create("first.csv",["seat no.","A","B","C","D"])
    create("business.csv",["seat no.","A","B","C","D"])
    create("economy.csv",["seat no.","A","B","C","D","E","F"])
    with open('first.csv',"a",newline='') as f1:
        w=csv.writer(f1)
        for i in range(1,6):
            l=[i,'','','','']
            w.writerow(l)
    with open('business.csv',"a",newline='') as f1:
        w=csv.writer(f1)
        for i in range(6,14):
            l=[i,'','','','']
            w.writerow(l)
    with open('economy.csv',"a",newline='') as f1:
        w=csv.writer(f1)
        for i in range(14,32):
            l=[i,'','','','','','']
            w.writerow(l)

def display_avail():
    flist=display('first.csv')
    print("          FIRST CLASS")
    print(tabulate(flist,headers='firstrow',tablefmt='grid'))
    time.sleep(2)
    print()
    blist=display('business.csv')
    print("         BUSINESS CLASS")
    print(tabulate(blist,headers='firstrow',tablefmt='grid'))
    time.sleep(2)
    print()
    elist=display('economy.csv')
    print("         ECONOMY CLASS")
    print(tabulate(elist,headers='firstrow',tablefmt='grid'))
    time.sleep(2)
    print()

def countseat(file):
    f1=open(file,'r')
    r1=csv.reader(f1)
    counts=0
    for i in r1:
        for j in i:
            if j=="":
                counts+=1
    f1.close()
    return counts

def lcost(total,bt=30): 
        if total>bt:
            e=total-bt
            l1=[["Your baggage is overweight"+"\n"+"You can remove excess luggage or pay for extra baggage"]]
            print(tabulate(l1,tablefmt="grid"))
            print()
            print("1.Remove extra weight")
            print("2.Pay for extra baggage")
            y=eval(input("enter choice:"))
            print()
            if y==1:
                print("You have to remove",e,"kg")
                   
            elif y==2:
                p=55*e
                print("You have to pay",p,"AED")
        else:
            print("Not overweight")

        
def ldisplay():                                                                   #Displaying luggage binary file
    f1=open("luggage.dat","rb")
    lulist=[]
    try:
        while True:
            l=pickle.load(f1)
            lulist.append(l)
    except EOFError:
            f1.close()
    print(tabulate(lulist,headers=['ref no','weight','fragile'],tablefmt='grid'))
    print("\n")

def lcreate():
    f=open('luggage.dat',"wb")
    f.close()
    print()
    print("\n"+"Luggage file is created"+"\n")
    print()

def viewdatabase():
    c=obj.cursor()
    c.execute("USE AIRMILES")
    c.execute("SELECT * FROM AIRMILE")
    l=c.fetchall()
    for i in l:
        print(i)
    c.close()

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
        f1=open("password.csv","r")
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
                f=open("password.csv","r")
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
    print()
    while True:
            flag=0
            c=obj.cursor()
            c.execute("USE AIRMILES")
            usn=input("enter username:")
            pas=input("enter password:")
            f1=open("password.csv","r")
            r=csv.reader(f1,delimiter=",")
            for i in r:
                    if i[1]==usn and i[2]==pas:
                            flag=1
            f1.close()
            if flag==0:
                    print("invalid Login ID or Password")
                    fp=input("Forgot password?")
                    if fp=="yes":
                            forgotpas()
                    login=input("Do you want to LOGIN to your AIRMILES ACCOUNT?")
                    if login=="no":
                            break 
                    print()
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
                    break
            c.close()
    
def depacc():
        print("TO BUY ADDITIONAL AIR POINTS")   
        c=obj.cursor()
        c.execute("USE AIRMILES")
        ano=input("enter airmile number:")
        answer=checkref(ano,'password.csv')
        if answer=='yes':
            x=ano[0]
            t=(ano,)
            c.execute("SELECT AIRPOINTS FROM AIRMILE WHERE AIRMILENO=%s",t)
            l=c.fetchall()
            ap=l[0][0]
            de=eval(input("enter amount to deposit:"))
            c.execute("SELECT * FROM AIRMILE")
            l=c.fetchall()
            for i in l:
                if i[0]==ano:
                    print("Your current balance is",ap)
                        
            co=input("Are you sure you want to deposit AIRPOINTS?").lower()
            if co=="yes":
                if x=="B":
                    ap+=de
                    T=(ap,ano)
                    q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
                    c.execute(q,T)
                    obj.commit()
                    print("Deposit successful")
                    print("Your current balance is",ap)
                elif x=="S":
                    ap+=(de*2)
                    T=(ap,ano)
                    q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
                    c.execute(q,T)
                    obj.commit()
                    print("Deposit successful")
                    print("Your current balance is",ap)
                elif x=="G":
                    ap+=(de*3)
                    T=(ap,ano)
                    q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
                    c.execute(q,T)
                    obj.commit()
                    print("Deposit successful")
                    print("Your current balance is",ap)
                elif x=="P":
                    ap+=(de*4)
                    T=(ap,ano)
                    q="UPDATE AIRMILE SET AIRPOINTS=%s WHERE AIRMILENO=%s"
                    c.execute(q,T)
                    obj.commit()
                    print("Deposit successful")
                    print("Your current balance is",ap)
                
            else:
                obj.rollback()
        else:
            print("invalid airmileno")




def redeem(r,ref):
    answer=checkref(ref,'password.csv')
    if answer=='yes':
        c=obj.cursor()
        c.execute("USE AIRMILES")
        de=r
        c.execute("SELECT * FROM AIRMILE")
        for i in c:
            if i[0]==ref:
                ap=i[2]
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
    elif answer=="no":
        print("Ooops! User not found")

    
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
        l=[["Payment successful, Enjoy services on land and in air"]]
        print(tabulate(l,tablefmt="grid"))


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


def payair(cls,airmileno):
    f={'P':20000,'G':25000,'S':30000,'B':35000}
    b={'P':10000,'G':15000,'S':20000,'B':25000}
    e={'P':5000,'G':10000,'S':15000,'B':20000}
    letter=airmileno[0]
    if cls=='first':
        redeem(f[letter],airmileno)
    elif cls=="business":
        redeem(b[letter],airmileno)
    elif cls=="economy":
        redeem(e[letter],airmileno)
    

        
print("Welcome to the flight booking and management project")
print("\n")
fr=input("Enter place of departure:")
to=input("Enter destination:")
terminal=input("Enter terminal:")
print("\n")

while True:                                                                     #Menu
    print("1. Introduction to the project")
    print("2. Booking")
    print("3. Seat")
    print("4. Connecting")
    print("5. Check In")
    print("6. Display all passenger details")
    print("7. Display name and reference number of all passengers")
    print("8. Cancel Flight Ticket")
    print("9. Seat Availability")
    print("10. Airmiles")
    print("11. Proceed to luggage")
    print("\n")
    x=eval(input("enter choice:"))
    print("\n")
    if x==1:
        print("\t"*5+"INTRODUCTION")
        f=open('INTRODUCTION.txt','w+')
        f.write('The proposed project “Airline Reservation System” has been developed to make Airline reservation easier and more feasible.\n')
        f.write('This Reservation System manages booking,cancellation,upgrade,modification,luggage etc.\n')
        f.write('This program is specifically designed for Passenger Service Agents to carry out their operations in a smooth and effective \nmanner.\n')
        f.write('\n')
        f.write('A few guidelines to the user before executing the program are as follows:\n')
        f.write('   # All files must be created before inputting any data.\n')
        f.write('   # Reference number created while booking must be noted before proceeding with other functions.\n')
        f.write('   # Once files are created they need not be created again.\n')
        f.write('\n                                                                     MADE BY ANDREA SAJU, LIYANA NAJEER AND RITIKA PAREKH\n')
        f.write('                                                                     12 SCI B\n')
        f.seek(0)
        ilist=[[" ".join(f.readlines())]]
        f.close()
        print(tabulate(ilist,tablefmt='grid'))
        print("\n")
    elif x==2:
        while True:
            print("1. Create Booking File")
            print("2. Book a flight")
            print("3. Modify details in booking file")
            print("4. Take me back to main menu")
            print("\n")
            m2=eval(input("enter choice:"))
            print("\n")
            if m2==1:
                h=["reference number","first name","last name","Child or adult","dob","passport number","passport expdate","num","num2","email","email2","airmile","address","minor","special needs","cstat"]
                create('booking.csv',h)
                print('Your booking file has been created, proceed to book your flight')
            elif m2==2:
                 n=eval(input("Enter no. of members travelling:"))
                 book(n)
            elif m2==3:
                 modify()
            else:
                break
            print()
            
    elif x==3:
        
        while True:
            print("1. Create seat file")
            print("2. Book a seat")
            print("3. Smart Pay")
            print("4. Display seat details of each passenger")
            print("5. Display Minors travelling")
            print("6. Display Passengers requiring special needs")
            print("7. Upgrade seat or meal")
            print("8. Take me back to main menu")
            print("\n")
            m3=eval(input("enter choice:"))
            print("\n")
            if m3==1:
                h=["ref no","class","seat number","seat letter","meal","name"]
                create('seat.csv',h)
                create_avail()
                print('Proceed and enter details to confirm seat booking')
                
            elif m3==2:
                seatl=[['Class','Rows','Seat letter','Price'],['First','1-5','A-D','19000 AED'],['Business','6-13','A-D','10000 AED'],['Economy','14-31','A-F','4500 AED']]
                print(tabulate(seatl,headers='firstrow',tablefmt='grid'))
                n=eval(input("Enter no. of members travelling:"))
                seat(n)
                
            elif m3==3:
                while True:
                    print("1.Pay using cash")
                    print("2.Pay using airmiles")
                    x=eval(input("enter choice:"))
                    if x==1:
                        cost()
                    else:
                        a=input("enter airmile no:")
                        ref=input("enter ref no:")
                        ans=checkref(a,'password.csv')
                        ans2=checkref(ref,'booking.csv')
                        print(ans,ans2)
                        if ans=="yes" and ans2=="yes":
                            l=getlist(ref,"seat.csv")
                            cls=l[1]
                            payair(cls,a)
                            break
                        else:
                            print("Oops! User not found")

            elif m3==4:
                slist=display("seat.csv")
                print(tabulate(slist,headers='firstrow',tablefmt='grid'))
                
            elif m3==5:
                f1=open('booking.csv','r')
                r=csv.reader(f1)
                print("Minors on board:")
                for i in r:
                    if i[13].lower()=="yes":
                         print("Reference number:",i[0])
                         print("First name:",i[1])
                         print("Last name:",i[2])
                         print()
                f1.close()
                         
            elif m3==6:
                f1=open('booking.csv','r')
                r=csv.reader(f1)
                print("Special needs passengers on board:")
                for i in r:
                    if i[14].lower()=="yes":
                         print("Reference number:",i[0])
                         print("First name:",i[1])
                         print("Last name:",i[2])
                         print()
                f1.close()
                
            elif m3==7:
                upgrade()

            else:
                break
            print()
    elif x==4:
        while True:
            print("1. Create connecting flights file")
            print("2. Enter name for connecting flight")
            print("3. Display passengers flying via connecting flight")
            print("4. Take me back to main menu")
            print("\n")
            m4=eval(input("enter choice:"))
            print("\n")
            if m4==1:
                h=["ref no","name","passport number","destination","flight","time"]
                create('connecting.csv',h)
                print('Connecting file is created')
                print()
            elif m4==2:
                connecting()
                
            elif m4==3:
                clist=display('connecting.csv')
                print(tabulate(clist,headers='firstrow',tablefmt='grid'))
                print()
            else:
                break
    elif x==5:
       while True:
            print("1. Check In")
            print("2. Display passengers checked in")
            print("3. Display passengers not checked in")
            print("4. Print Boarding pass")
            print("5. Take me back to main menu")
            print("\n")
            m5=eval(input("enter choice:"))
            print("\n")
            if m5==1:
                checkin()
              
            elif m5==2:
                 f=open('booking.csv','r')
                 r=csv.reader(f)
                 lcheck=[]
                 for i in r:
                    if i[-1]=='Yes':
                        lcheck.append([i[0],i[1]+" "+i[2]])
                 f.close()
                 print(tabulate(lcheck,headers=['ref no','name'],tablefmt='grid'))
    
            elif m5==3:
                f=open('booking.csv','r')
                r=csv.reader(f)
                lcheck=[]
                for i in r:
                    if i[-1]=='No':
                        lcheck.append([i[0],i[1]+" "+i[2]])
                f.close()
                print(tabulate(lcheck,headers=['ref no','name'],tablefmt='grid'))
                
            elif m5==4:
                boarding()
            else:
                break

    elif x==6:
        dlist=display("booking.csv")
        l1=[]
        l2=[]
        l3=[]
        for i in dlist:
                l1.append(i[:7])
                l2.append(i[:1]+i[11:12]+i[-1:-4:-1])
                l3.append(i[:1]+i[7:11]+i[12:13])
        #print(tabulate(dlist,headers='firstrow',tablefmt='grid'))
        print("primary details:")
        print(tabulate(l1,headers='firstrow',tablefmt='grid'))
        print()
        print("additional details:")
        print(tabulate(l2,headers='firstrow',tablefmt='grid'))
        print()
        print("contact details:")
        print(tabulate(l3,headers='firstrow',tablefmt='grid'))
        
    elif x==7:
        f1=open("booking.csv","r")
        r=csv.reader(f1)
        mainlist=[]
        line=0
        for i in r:
                if line==0:
                        heading=[i[0],'full name']
                else:
                        mainlist.append([i[0],i[1]+" "+i[2]])
                line+=1
        f1.close()
        print(tabulate(mainlist,headers=heading,tablefmt='grid'))

    elif x==8:
        ref=eval(input("Enter reference number to cancel ticket:"))
        if checkref(str(ref),'booking.csv')=='no':
            print('ref no is wrong')
            continue
        print()
        detlist=getlist(str(ref),'seat.csv')
        a,b,c=detlist[1:4]
        cancelseat(a,b,c)
        cancel(ref,'booking.csv')
        cancel(ref,'seat.csv')
        cancel(ref,'connecting.csv')
        print("flight cancelation successful")
    elif x==9:
        while True:
            print('1. Create new file')
            print('2. Display available seats')
            print("3. Number of seats available")
            print('4. Take me back to main menu')
            print()
            m9=eval(input("enter choice:"))
            print("\n")
            if m9==1:
                create_avail()
                print("File is created")
            elif m9==2:
                display_avail()
            elif m9==3:
                cf=countseat('first.csv')
                cb=countseat('business.csv')
                ce=countseat('economy.csv')
                countlist=[['first class',cf],['business class',cb],['economy class',ce]]
                print(tabulate(countlist,tablefmt='grid'))
            else:
                break
            print("\n")
    elif x==10:
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
            print("9.Display airmile table")
            print("10.Go back to the main menu")
            choice=eval(input("eneter your choice:"))
            print()
            if choice==1:
                c=obj.cursor()
                c.execute("CREATE DATABASE IF NOT EXISTS AIRMILES")
                c.execute("USE AIRMILES")
                c.execute("CREATE TABLE IF NOT EXISTS AIRMILE(AIRMILENO VARCHAR(8),NAME VARCHAR(15),AIRPOINTS INTEGER,PASSPORTNO VARCHAR(15),DOB DATE)")
                c.close()
                create('password.csv',['airmileno','username','password'])
                print("Database,file and table created")
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
            elif choice==9:
                viewdatabase()

            else:
                h=[["Thank You for choosing the Airmiles Customer Loyalty Program"],["Airmiles, Fly high"]]
                print(tabulate(h,tablefmt='grid'))
                break
            _cntnue=input("press enter to continue..")
            print()
    else:
        break
    print()
    _cntnue=input("Press enter to continue...")
    print("\n")


while True:
    print("1.Create luggage file")
    print("2.Travelling alone")
    print("3.Travelling with friends/family/other")
    print("4.Display luggage file")
    print("5.Sign Out")
    print()
    lx=eval(input("enter choice:"))
    if lx==5:
            break
    elif lx==1:
        
        lcreate()
   
    elif lx==2:
        f=open("luggage.dat",'ab')
        ref=input("Enter reference number:")
        if checkref(ref,'booking.csv')=='no':
            print()
            print('ref no is wrong')
            continue
        bn=eval(input("enter number of luggage:"))
        total=0
        hl=eval(input("Enter number of hand luggage:"))
        for i in range(bn):
            l=[]
            we=eval(input("Enter weight of luggage:"))
            total+=we
            fr=input("Fragile:")
            l=[ref,we,fr]
            pickle.dump(l,f)
        f.close()
        lcost(total) 
        
    elif lx==3:
        f=open("luggage.dat",'ab')
        n=eval(input("Enter number of passengers:"))
        bn=eval(input("enter number of luggage:"))
        total=0
        hl=eval(input("Enter number of hand luggage:"))
        flag=0
        for i in range(bn):
            l=[]
            ref=eval(input("Enter reference number:"))
            if checkref(str(ref),'booking.csv')=='no':
                print()
                print('Ref no is wrong')
                print()
                flag=1
                continue
            we=eval(input("Enter weight of luggage:"))
            total+=we
            fr=input("Fragile:")
            l=[ref,we,fr]
            pickle.dump(l,f)
        f.close()
        if flag==0:
                bt=n*30   
                lcost(total,bt)

    elif lx==4:
        ldisplay()
    print()

obj.close()
l=[["Thank You for choosing us, have a nice journey!"]]
print("\n")
print(tabulate(l))
       
