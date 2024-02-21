N = abs(int(input()))
if 100<=N<=999:
    od = N % 10
    de = N // 10 % 10
    co = N // 100
    if od != de and de != co and od != co:
        print("YES")
    else:
        print("NO")