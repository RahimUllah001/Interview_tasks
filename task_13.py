# 13. Create a program that generates a list of prime numbers up to a given limit.

def prime_number(limit):
    for i in range(2,limit + 1):
        is_prime = True
        j = 2

        while j < i and i != 2:
            if i % j == 0:
                is_prime = False
            
                break
            else:
                j = j + 1

        if is_prime:
            print(i)

prime_number(101)



# Another way
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

# Example usage:
limit = 50
prime_numbers = generate_primes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")
