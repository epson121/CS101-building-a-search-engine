#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n == 0:
        return 0;
    if n == 1:
        return 1;
    fib1 = 0;
    fib2 = 1;
    i = 1;
    while i < n:
        fib3 = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib3;
        i = i + 1;
    return fib3;

print fibonacci(36);
#>>> 14930352
