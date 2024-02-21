a = input()

s = ""

for el in a:
    if el.islower():
        s = s + el

c = s[::-1]

if s==c :
    print("YES")
else:
    print("NO")