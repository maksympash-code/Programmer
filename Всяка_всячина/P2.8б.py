import itertools

def count_inversions(perm):
    """Функція для підрахунку кількості інверсій у перестановці"""
    inversions = 0
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions

def find_permutations_with_inversions(n, target_inversions):
    """Знаходить кількість перестановок з точно target_inversions інверсіями"""
    perms = itertools.permutations(range(1, n + 1))
    count = 0
    for perm in perms:
        if count_inversions(perm) == target_inversions:
            count += 1
    return count

# Шукаємо кількість перестановок для n=6 з рівно 13 інверсіями
n = 6
target_inversions = 13
result = find_permutations_with_inversions(n, target_inversions)
print(result)

