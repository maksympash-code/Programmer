def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_twin_primes(n):
    count = 0
    for i in range(2, n):
        if is_prime(i) and is_prime(i + 2):
            count += 1
    return count

def main():
    limit = 10**6
    primes_count = 0
    twin_primes_count = 0
    for i in range(2, limit):
        if is_prime(i):
            primes_count += 1
    twin_primes_count = count_twin_primes(limit)
    print("Усього простих чисел від 1 до", limit, ":", primes_count)
    print("Кількість чисел близнюків серед простих чисел від 1 до", limit, ":", twin_primes_count)

if __name__ == "__main__":
    main()
