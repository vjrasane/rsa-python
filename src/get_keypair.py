import random
from get_large_prime import get_large_prime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_random_coprime(num):
    while True:
      coprime = random.randrange(1, num)
      if coprime % 2 != 0 and gcd(num, coprime) == 1:
        return coprime


def get_keypair(bits):
    p = get_large_prime(bits)
    q = get_large_prime(bits)
    n = p * q
    phi = (p-1) * (q-1)
    e = get_random_coprime(phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))
