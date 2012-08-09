
def factorial(n):
    i = 1;
    f = 1;
    while (i <= n):
        f = f*i;
        print f;
        print i;
        i = i+1;
    return f;

print factorial(5);
