import time


def print_permutations(p):
    print(p)


def johnson_trotter(n):

    p = list(range(1, n + 1))
    directions = [-1] * n


    print_permutations(p)

    def get_mobile():
        mobile = -1
        for i in range(n):
            if (directions[i] == -1 and i > 0 and p[i] > p[i - 1]) or \
                    (directions[i] == 1 and i < n - 1 and p[i] > p[i + 1]):
                if mobile == -1 or p[i] > p[mobile]:
                    mobile = i
        return mobile

    count = 1
    while True:
        mobile = get_mobile()
        if mobile == -1:
            break


        if directions[mobile] == -1:
            p[mobile], p[mobile - 1] = p[mobile - 1], p[mobile]
            directions[mobile], directions[mobile - 1] = directions[mobile - 1], directions[mobile]
            mobile -= 1
        else:
            p[mobile], p[mobile + 1] = p[mobile + 1], p[mobile]
            directions[mobile], directions[mobile + 1] = directions[mobile + 1], directions[mobile]
            mobile += 1


        for i in range(n):
            if p[i] > p[mobile]:
                directions[i] *= -1

        count += 1
        if count <= 50:
            print_permutations(p)


johnson_trotter(6)


for n in range(5, 11):
    start_time = time.time()
    johnson_trotter(n)
    end_time = time.time()
    print(f"Час генерації для n={n}: {end_time - start_time:.4f} секунд")

