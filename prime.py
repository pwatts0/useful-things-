def is_prime(n):
    prime = True
    for num in range(2, int(n ** .5) + 1):
        if n % num == 0:
            prime = False
    return prime
   
def find_divisors(n):
    divisors = []
    prime = True
    for num in range(2, int((n**.5)) + 1):
        if n % num == 0:
            divisors.append(num)
            prime = False
    return divisors, prime
    
 
