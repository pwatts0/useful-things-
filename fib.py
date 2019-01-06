def fib(n):
    first = 1
    second = 1
    for i in range(1, n):
        temp = first + second
        first = second
        second = temp
    
    return first
