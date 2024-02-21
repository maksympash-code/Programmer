# for n in range(1,21):
#     x=int(input())
#     if -10<=x<=10 and x%2==0:
#         print(x,"is even")
#     elif x==0:
#         print(x, "is even")
#     elif -10<=x<=10 and x%3==0 :
#         print(x,"is odd")
#     elif -10<=x<=10 and x%5==0:
#         print(x, "is odd")
#     elif -10<=x<=10 and x%7==0:
#         print(x, "is odd")


# for i in range(1,21):
#     x=int(input())
#     if -10 <= x <= 10 and x % 2 == 0 or x==0:
#         print(x,"is even")
#     else:
#         if -10 <= x <= 10 and x % 2 != 0:
#             print(x, "is odd")


n=int(input())

for i in range(n):
    x=int(input())
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")