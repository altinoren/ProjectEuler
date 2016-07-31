def get_n_primes(amount):
    "Get a list of first n primes"
    primes = []
    primes.append(2)
    current = 3
    while len(primes) < amount:
        is_prime = True
        for p in primes:
            if current % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current)
        current += 1
    
    return primes