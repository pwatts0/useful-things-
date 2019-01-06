# Find length of a number's Collatz sequence

def Collatz(n):
    path = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            path += 1
        else:
            n = (3*n + 1)
            path += 1
    return path
