import csv
def amount(n):
        f=open("seat.csv","r",newline="")
        r=csv.reader(f)
        line=0
        for i in r:
            cost=0
            print(i)
            print(i[1])
            if line!=0:
                if i[1]=="economy":
                    cost+=600
                elif i[1]=="bussiness":
                    cost+=1000
                elif i[1]=="first":
                    cost+=1750
            print(cost,"is the total cost")
            line+=1

        f.close()

