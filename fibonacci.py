import matplotlib.pyplot as plt

# Usando loop
def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usando recursão
def fibonacci_recursao(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursao(n-1) + fibonacci_recursao(n-2)

# Número de termos
n = 10

# Gerar sequência
fibonacci_numeros = list(fibonacci_loop(n))

# Exibir sequência no terminal
print("Sequência de Fibonacci (loop):")
print(fibonacci_numeros)
print("\n10º termo da Sequência de Fibonacci (recursão):", fibonacci_recursao(n - 1))

# Criar gráfico
plt.plot(range(n), fibonacci_numeros, marker='o', linestyle='-', color='blue')
plt.title('Sequência de Fibonacci')
plt.xlabel('Índice (n)')
plt.ylabel('Valor de Fibonacci')
plt.grid(True)
plt.show()