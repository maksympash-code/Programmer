#1
# n = int(input())
#
# b1 = 1 # b_1
# P1 = 3 # P_1
#
# for k in range(2,n+1):
#     b1 = b1 / k
#     P1 = P1 * (2 + b1)
#
# print(P1)

#2
# def gen():
#     T3 = 1
#     yield T3
#     T2 = 0
#     yield T2
#     T1 = 2
#     yield T1
#
#     while True:
#         T = T1 + T3 * 7
#         yield T
#         T3 = T2
#         T2 = T1
#         T1 = T
#
#
# for t in gen():
#     print(t)
#     if n == 10:

#3
x = 0.5

s = x
a = x

k = 0

while True:
    k += 1
    a *= x**2
    s_new = s
    s += a / (2*k + 1)

    if abs(s-s_new) < 0.00001:
        break

print(s)