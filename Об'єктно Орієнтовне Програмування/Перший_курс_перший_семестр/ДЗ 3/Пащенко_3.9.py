n=int(input())
i=0
k=1
while i < n:
    if  (k % 2 != 0) and (k % 3 != 0) and (k % 5 != 0):
        print(k, end=" ")
        k+=1
        i+=1
    else:
        k+=1
        i+=0
