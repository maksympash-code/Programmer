n=int(input())
lst=input().split()

lst1=[int(lst[i]) for i in range(n)]

print(min(lst1))