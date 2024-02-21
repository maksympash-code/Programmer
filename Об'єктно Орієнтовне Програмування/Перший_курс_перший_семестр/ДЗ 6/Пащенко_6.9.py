a=input()

counter=0
cou=0
for symbol in a:
        if ord(symbol) in [37,42,43,45,47]:
            if a[cou] != a [cou+1]:
                counter += 1
        cou+=1

print(counter)