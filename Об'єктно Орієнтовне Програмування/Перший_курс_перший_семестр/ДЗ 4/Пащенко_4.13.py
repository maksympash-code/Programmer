n=int(input())
counter=0
for i in range(10,100):
   a=i//10+i%10
   b=n*i
   c=b//100+b%10+(b%100)//10
   if a==c:
       counter+=1
print(counter)