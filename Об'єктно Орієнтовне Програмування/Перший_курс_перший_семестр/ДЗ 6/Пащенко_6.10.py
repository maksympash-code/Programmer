a=input() #welcome to python

new = ""
for c in a:
    new = new + c
    if c in "abcdefghijklmnopqrstuvwxyz":
        new = new + c

print(new)