a=input()

counter=0

for syb in a:
    if 97<=ord(syb)<=122:
        counter+=1
        break
for syb in a:
    if 65<=ord(syb)<=90:
        counter+=1
        break
for syb in a:
    if 48<=ord(syb)<=57:
        counter+=1
        break
for syb in a:
    if 33<=ord(syb)<=43:
        counter+=1
        break
for syb in a:
    if len(a)>=8:
        counter+=1
        break

print(counter)