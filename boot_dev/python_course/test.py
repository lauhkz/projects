def primes(n: int):

    sieve = [True] * n

    res = []

    for i in range(2, n):
        if sieve[i]:
            res.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False

    return res

xs = primes(100)

#print(xs)

def area_of_circles(r):

    pi = 3.14

    result = pi * r * r

    return result

#print(area_of_circles(5))

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
# main()

def nothing():
    return None
# doesn't give anything

nothing()

#print(0b10000)


number = 9

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
