counter=0
while True:
    a=int(input())
    if a==0:
        break
    elif a < 0:
        counter += 1
print(counter)
