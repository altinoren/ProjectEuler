import prime

primes = prime.get_n_primes(1000)
last_prime = 0
number = 600851475143
found = False

while True:
    for i in range(0, len(primes)):
        last_prime = primes[i]
        while True:
            if number % last_prime == 0:
                number = number / last_prime
                if number == 1:
                    found = True
                    break
            else:
                break

        if found:
            break
        
    if found:
        break

print(last_prime)