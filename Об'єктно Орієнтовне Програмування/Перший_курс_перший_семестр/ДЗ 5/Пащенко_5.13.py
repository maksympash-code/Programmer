N=float(input())
lst=[float(el) for el in input().split()]


i=0
NEWlst=[]
summa=0
for el in range (len(lst)):
    if lst[el]>0:
        NEWlst.append(lst[el])


for el2 in NEWlst:
    summa+=el2
    sa =summa/len(NEWlst)
    i=1



if i==1:
    print(f"{sa:0.2f}")
elif i==0:
    print("Not Found")