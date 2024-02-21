x1,y1,x2,y2,x3,y3=map(int,input(). split())
if (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)==0:
    print(x2+x3-x1,y2+y3-y1)
elif (x3-x2)*(x1-x2)+(y3-y2)*(y1-y2)==0:
    print(x3+x1-x2,y3+y1-y2)
else:
    print(x1+x2-x3,y1+y2-y3)