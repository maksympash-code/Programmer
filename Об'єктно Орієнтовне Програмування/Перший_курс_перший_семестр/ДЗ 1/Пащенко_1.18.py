x1,y1,x2,y2,x3,y3,x4,y4 = [float(d) for d in input().split()]

S = 0.5*abs(int(x1*y2-y1*x2)+int(x2*y3-y2*x3)+int(x3*y4-y3*x4)+int(x4*y1-y4*x1))
print(round(S))