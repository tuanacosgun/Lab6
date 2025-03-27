import math

#factorial function
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

#sine function
def sine_x(x, n):
    x = math.radians(x)
    term = lambda i: ((-1) ** i * x ** (2 * i + 1)) / factorial(2 * i + 1)

    result = 0
    for i in range(n):
        result += term(i)

    return result

harmonic_sum = 0

#harmonic function
def harmonic(n):
    global harmonic_sum
    if n == 0:
        return
    harmonic(n - 1)
    harmonic_sum += 1 / n

print("Factorial of 5:", factorial(5))
print("sin(30) approximation (5 terms):", sine_x(30, 5))
harmonic(5)
print("Harmonic number H_5:", harmonic_sum)
