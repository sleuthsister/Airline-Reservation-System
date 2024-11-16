import csv,random,os,pickle
from tabulate import tabulate
from datetime import date
from datetime import datetime

def checkref(refno,file):
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

def cost():
        
        f1=open("seat.csv","r",newline="")                                          #Payment
        r=csv.reader(f1)
        line=0
        cost=0
        d1=0
        d2=0
        d3=0
        n=eval(input("enter number of seats booked:"))
        c=n//2
        for j in range(n):
                ref=input("enter name of passenger:")
                for i in r:
                        if line!=0:
                                if ref==i[5]:
                                        if i[1]=="first":
                                                cost=cost+19000
                                        elif i[1]=="business":
                                                cost+=10000
                                        elif i[1]=="economy":
                                                cost+=4500
                                        d1=i[1]
                                        d2=i[4]
                                        d3=i[2]+i[3]
                        
                        line+=1
        print("\n")
        print("--------------------TICKET-------------------")
        print("\n")
        print("Name of passenger:",ref)
        print("Class chosen:",d1)
        print("Meal chosen:",d2)
        print("Seat chosen:",d3)
        print("Amount to be paid is AED",cost)
        print("\n")
        print("--------Thank you and enjoy your flight------")
        print("\n")
                                        
                        
        print("\n")
        f1.close()    
              

def count():                                                                             #Seat Availability
        f1=open("booking.csv","r")
        r=csv.reader(f1)
        line=0
        count=0
        for i in r:
                if line!=0:
                        count+=1
                line=1
        seat=160-count
        return seat
        f1.close()
        print("\n")
    
    
                
def create(filename,h):
        f=open(filename,"w",newline="") 
        w=csv.writer(f)
        w.writerow(h)
        f.close()

def book(n):                                                                               #Booking flight
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
        print("Your booking has been confirmed, procced to book your seat")
    f.close()
    print()




def seat(n):                                                                            #Seat Selection
      f1=open("seat.csv","a",newline="")
      w=csv.writer(f1,delimiter=",")
      for i in range(n):
        r=input("Enter refno:")
        answer=checkref(r,'booking.csv')
        if answer=='no':
                print("reference number entered is incorrect")
                break
        na=input("Enter name:")
        c=input("Enter class:")
        n=eval(input("Enter seat no:"))
        a=input("Enter seat letter:")
        m=input("Enter type of meal:")
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
        f2=open('new.csv','w',newline='')
        r=csv.reader(f1)
        w=csv.writer(f2)
        if cw==0:
            answer=checkref(y,'seat.csv')
            if answer=='no':
                print("reference number entered is incorrect")
                break
        print("1.Upgrade class")
        print("2.Change seat")
        print('3.Change seat letter')
        print('4.Change meal')
        print('5.Take me back to main menu')
        x=eval(input('Enter choice:'))
        if x==5:
            break
        for i in r:
            if i[0]==y:
                if x==1:
                    a=input('Enter new class:')
                    b=input('Enter new seat number:')
                    c=input('Enter new seat letter:')
                    i[1:4]=[a,b,c]
                elif x==2:
                    a=input('Enter new seat number:')
                    i[2]=a
                elif x==3:
                    a=input('Enter new seat letter:')
                    i[3]=a
                elif x==4:
                    a=input("Enter veg or non veg:")
                    i[4]=a
                print("\n")
                print('Details are updated')
                print("\n")
            w.writerow(i)
        f1.close()
        f2.close()
        cw+=1
        os.remove('seat.csv')
        os.rename('new.csv','seat.csv')

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
    print("flight cancelation successful")
    print("\n")

def connecting():                                                              #Passengers on Connecting Flights
    f1=open("booking.csv","r")
    f2=open("connecting.csv","a",newline="")
    r=csv.reader(f1)
    w=csv.writer(f2)
    y=eval(input("Enter reference number:"))
    line=0
    for i in r:
        if line!=0 and int(i[0])==y:
            a=input("Enter arrival destination:")
            f=input("Enter connecting flight number:")
            t=input("Enter arrival time in destination 2:")
            l=[i[0],i[1]+" "+i[2],i[7],a,f,t]
            w.writerow(l)
        line+=1
    f1.close()
    f2.close()
    print("Connecting flight booked successfully")
    print("\n")
                                                                                 #Display csv
from datetime import datetime
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
    time=da[11:19]
    n=eval(input("Enter reference number to print boarding pass:"))
    line=0
    for i in r:
        if line!=0 and n==int(i[0]):
            print("\n")
            print("_______________________________________________________________________________________________")
            print("\t","\t","\t","\t","\t","\t","Boarding Pass")
            print("_______________________________________________________________________________________________")
            print()
            print("ticket number:",i[0],"\t","passenger name:",i[5],"\t","date:",date)
            print()
            print("class:",i[1],"\t","\t","seat:",i[2]+i[3],"\t""\t""\t","time:",time)
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

def luggage():                                                                                 #Luggage Details
  while True:
    print("1.Travelling alone")
    print("2.Travelling with friends/family/other")
    print("3.Take me back to main menu")
    x=eval(input("enter choice:"))
    if x==3:
            break
    elif x==1:
        f=open("luggage.dat",'ab')
        ref=eval(input("Enter reference number:"))
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
        bt=30   
        if total>bt:
            e=total-bt
            print("Over weight")
            print("1.Remove extra weight")
            print("2.Pay for extra baggage")
            y=eval(input("enter choice:"))
            if y==1:
                print("You have to remove",e,"kg")
                   
            elif y==2:
                p=55*e
                print("You have to pay",p,"AED")
        else:
            print("Not overweight")
    elif x==2:
        f=open("luggage.dat",'ab')
        n=eval(input("Enter number of passengers:"))
        bn=eval(input("enter number of luggage:"))
        total=0
        hl=eval(input("Enter number of hand luggage:"))
        for i in range(bn):
            l=[]
            ref=eval(input("Enter reference number:"))
            we=eval(input("Enter weight of luggage:"))
            total+=we
            fr=input("Fragile:")
            l=[ref,we,fr]
            pickle.dump(l,f)
        f.close()
        bt=n*30   
        if total>bt:
            e=total-bt
            print("Over weight")
            print("1.Remove extra weight")
            print("2.Pay for extra baggage")
            x=eval(input("enter choice:"))
            if y==1:
                print("You have to remove",e,"kg")
                   
            elif y==2:
                p=55*e
                print("You have to pay",p,"AED")
        else:
            print("Not overweight")
    print("\n")

        
    


        
def ldisplay():                                                                                 #Displaying luggage binary file
    f1=open("luggage.dat","rb")
    try:
        while True:
            l=pickle.load(f1)
            print(l)
            
    except EOFError:
            f1.close()
    print("\n")
            
            
def checkin():                                                                               #Check in
        ref=eval(input('Enter reference number:'))
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
        print("Check in successful")
        print("\n")

def modify():                                                                                  #modify details in booking.csv
    y=input('Enter reference number:')
    cw=0
    while True:
        f1=open('booking.csv','r')
        f2=open('new.csv','w',newline='')
        r=csv.reader(f1)
        w=csv.writer(f2)
        if cw==0:
            answer=checkref(y,'booking.csv')
            if answer=='no':
                print("reference number entered is incorrect")
                break
        print("\n")
        print("1.Edit name")
        print("2.Edit child or adult")
        print('3.Edit date of birth')
        print('4.Edit passport number and expiration date')
        print('5.Edit contact details')
        print("6.Edit minor/need special needs details")
        print("7.Edit airmile number")
        print("8.Take me back to the main menu")
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
                print('Details are successfully modified in the booking file')
            w.writerow(i)
        f1.close()
        f2.close()
        cw+=1
        os.remove('booking.csv')
        os.rename('new.csv','booking.csv')
            

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
    print("9. Proceed to luggage")
    print("10. Sign Out")

    x=eval(input("enter choice:"))
    print("\n")
    if x==1:
        print("INTRODUCTION")
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
                print("\n")
            elif m2==2:
                 n=eval(input("Enter no. of members travelling:"))
                 book(n)
                 print("\n")
            elif m2==3:
                 modify()
                 print("\n")
            else:
                break
            
    elif x==3:
        
        while True:
            print("1. Create seat file")
            print("2. Book a seat")
            print("3. Smart Pay")
            print("4. Display seat details of each passenger")
            print("5. Display Minors travelling")
            print("6. Display Passengers requiring special needs")
            print("7. Upgrade seat or meal")
            print("8. Seat Availability")
            print("9. Take me back to main menu")
            print("\n")
            m3=eval(input("enter choice:"))
            print("\n")
            if m3==1:
                h=["ref no","class","seat number","seat letter","meal","name"]
                create('seat.csv',h)
                print('Proceed and enter details to confirm seat booking')
                
            elif m3==2:
                n=eval(input("Enter no. of members travelling:"))
                seat(n)
                print("Thank You for choosing our flight, Enjoy your Journey")
                
            elif m3==3:
                cost()
            elif m3==4:
                slist=display("seat.csv")
                print(tabulate(slist,headers='firstrow',tablefmt='grid'))
                
            elif m3==5:
                f1=open('booking.csv','r')
                r=csv.reader(f1)
                print("Minors on board:")
                for i in r:
                    if i[13]=="yes":
                         print("reference number=",i[0])
                         print("first name=",i[1])
                         print("last name=",i[2])
                         print()
                         
            elif m3==6:
                f1=open('booking.csv','r')
                r=csv.reader(f1)
                print("Special needs passengers on board:")
                for i in r:
                    if i[14]=="yes":
                         print("reference number=",i[0])
                         print("first name=",i[1])
                         print("last name=",i[2])
                         print()
                
            elif m3==7:
                upgrade()

            elif m3==8:
                print(count(),"seats available")
            else:
                break
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
                print('File is created')
                
            elif m4==2:
                connecting()
                
            elif m4==3:
                clist=display('connecting.csv')
                print(tabulate(clist,headers='firstrow',tablefmt='grid'))
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
                 for i in r:
                    if i[-1]=='Yes':
                        print(i[0],i[1]+" "+i[2])
                 f.close()
                 
            elif m5==3:
                f=open('booking.csv','r')
                r=csv.reader(f)
                for i in r:
                    if i[-1]=='No':
                        print(i[0],i[1]+" "+i[2])
                f.close()
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
        print("additional details:")
        print(tabulate(l2,headers='firstrow',tablefmt='grid'))
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
        cancel(ref,'booking.csv')
        cancel(ref,'seat.csv')
        cancel(ref,'connecting.csv')
        count+=1
    elif x==9:
        luggage()
        
    


   
        
    else:
        break
    _cntnue=input("Press enter to continue...")
    print("\n")
