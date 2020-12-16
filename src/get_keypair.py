import random
from get_large_prime import get_large_prime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def egcd(a, b):
    stack = []
    while (a):
      stack.append((a, b))
      a, b = b % a, a
    gcd = b
    x = 0
    y = 1
    for a, b in reversed(stack):
      x, y = y - (b // a) * x, x
    return gcd, x, y

def modular_multiplicative_inverse(base, mod):
    gcd, x, y = egcd(base, mod)
    if gcd != 1:
      raise Exception('no modular inverse')
    return x % mod

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
    d = modular_multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
