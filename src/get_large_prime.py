import random
import json
import os
current_dir=os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir,"first-primes.json")) as json_file:
  first_primes = json.load(json_file)

def miller_test(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def is_prime_miller_rabin(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        if not miller_test(d, n):
            return False
    return True

def is_low_level_prime(candidate):
    for divisor in first_primes:
      if candidate % divisor == 0 and divisor**2 <= candidate:
        return False
    return True

def get_prime_candidate(bits):
    return random.randrange(2**(bits-1)+1, 2**bits - 1)

def get_low_level_prime(bits):
    while True:
        candidate = get_prime_candidate(bits)
        if is_low_level_prime(candidate):
          return candidate

def get_large_prime(bits=1024, trials=20):
  while True:
    candidate = get_low_level_prime(bits)
    if is_prime_miller_rabin(candidate, trials):
      return candidate
