n=int(input())

counter=0

for i in range(100,1000):
    od=i%10
    de=i//10%10
    co=i//100
    if n==1:
        if od%2==0 and de%2==0 and co%2==0:
            counter+=i
    elif n==2:
        if co<de<od:
            counter+=1

    elif n==3:
        if od%2!=0 and de%2!=0 and co%2!=0:
            counter+=i
    elif n==4:
        if co>de>od:
            counter+=1
    elif n==5:
        if od**3+de**3+co**3==i:
            counter+=i
    elif n==6:
        if od!=de and de!=co and co!=od:
            counter+=1
print(counter)