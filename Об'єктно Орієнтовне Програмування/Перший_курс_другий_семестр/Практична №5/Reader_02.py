from Equation import *
from QuadraticEquation import *
from BiQuadraticEquation import *

def read_file(input02):
    with open(input02, 'r') as file:
        not_solves= []
        one_solve = []
        two_solves = []
        tree_solves = []
        four_solves = []
        infinity_solves = []
        solves = []

        for line in file:
            number = line.strip().split()
            # numbers.append(number)

            if len(number) == 2: # Лінійне рівняння bx + c = 0
                b,c = int(number[0]),int(number[1])
                eq = Equation(b,c)
                solve = eq.solve()
                if solve == ():
                    not_solves.append(str(eq))
                elif len(solve) == 1:
                    one_solve.append(str(eq))
                    solves.append(solve[0])
                elif solve == "infinity":
                    infinity_solves.append(str(eq))
                else:
                    continue


            elif len(number) == 3: # Квадратне рівняння ax^2 + bx + c = 0
                a,b,c = number[0],number[1],number[2]
                qu = QuadraticEquation(int(a),int(b),int(c))
                solve = qu.solve()
                if solve == ():
                    not_solves.append(str(qu))
                elif len(solve) == 1:
                    one_solve.append(str(qu))
                    solves.append(solve[0])
                elif len(solve) == 2:
                    two_solves.append(str(qu))
                elif solve == "infinity":
                    infinity_solves.append(str(qu))
                else:
                    continue


            elif len(number) == 5: # Біквадратне рівняння ax^4 + bx^2 + c = 0
                a,b,c = number[0],number[2],number[4]
                bi = BiQuadraticEquation(int(a),int(b),int(c))
                solve = bi.solve()
                if solve == ():
                    not_solves.append(str(bi))
                elif len(solve) == 1:
                    one_solve.append(str(bi))
                    solves.append(solve[0])
                elif len(solve) == 2:
                    two_solves.append(str(bi))
                elif len(solve) == 3:
                    tree_solves.append(str(bi))
                elif len(solve) == 4:
                    four_solves.append(str(bi))
                elif solve == "infinity":
                    infinity_solves.append(str(bi))
                else:
                    continue
        return not_solves, one_solve, two_solves, tree_solves, four_solves, infinity_solves, solves

input02 = "input02"
read = read_file(input02)

min_value = min(read[6])
min_index = read[6].index(min_value)

max_value = max(read[6])
max_index = read[6].index(max_value)


for i in range(1):
    print("These equations have no solutions: " , read[0])
    print("These equations have no solutions: ", len(read[0]))

    print("These equations have one solution: ", read[1])
    print("These equations have one solution: ", len(read[1]))

    print("These equations have two solutions: ", read[2])
    print("These equations have two solutions: ", len(read[2]))

    print("These equations have tree solutions: ", read[3])
    print("These equations have tree solutions: ", len(read[3]))

    print("These equations have four solutions: ", read[4])
    print("These equations have four solutions: ", len(read[4]))

    print("These equations have infinity solution: ", read[5])
    print("These equations have infinity solutions: ", len(read[5]))

    print("Equation with a minimum value: ", read[1][min_index])
    print("Equation with a maximum value: ", read[1][max_index])


