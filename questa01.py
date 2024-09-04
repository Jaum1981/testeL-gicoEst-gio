def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

num = int(input("Digite um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
