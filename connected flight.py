# CONNECTING FLIGHTS

import csv
def connecting():
    f1=open("booking.csv","r")
    f2=open("connecting.csv","a",newline="")
    r=csv.reader(f1)
    w=csv.writer(f2)
    w.writerow(h)
    y=eval(input("enter reference number:"))
    line=0
    for i in r:
        if line!=0 and int(i[0])==y:
            a=input("enter arrival destination:")
            f=input("enter connecting flight number:")
            t=eval(input("enter arrival time in destination 2:"))
            l=[i[0],i[1]+" "+i[2],i[7],a,f,t]
            w.writerow(l)
        line+=1
    f1.close()
    f2.close()
connecting()
