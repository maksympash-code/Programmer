a = input()
b = []
c = ""
for el in a:
    el1 = ord(el)
    b.append(el1)

b.sort()
for el1 in b:
    c += chr(el1)

print(c)