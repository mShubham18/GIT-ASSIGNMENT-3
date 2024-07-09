def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n = 10 
print(f"Fibonacci series up to {n} terms:")
print(fibonacci_series(n))
