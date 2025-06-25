# 📊 study-repository - Fibonacci em Python

Este repositório apresenta duas formas simples de calcular a **Sequência de Fibonacci** utilizando Python: uma com **loop (iterativa)** e outra com **recursão**.

## 📌 Métodos Implementados

### 1. `fibonacci_loop(n)`
Gera os `n` primeiros termos da sequência de Fibonacci utilizando um loop.

### 2. `fibonacci_recursao(n)`
Retorna o `n`-ésimo termo da sequência de forma recursiva simples (sem memoização).

## ▶️ Exemplo de Uso

- Imprime os 10 primeiros termos da sequência com loop.
- Calcula o 10º termo da sequência com recursão.

## ⚠️ Observações

- A versão **com loop** é muito mais eficiente e indicada para gerar sequências.
- A versão **recursiva** é útil para fins didáticos, mas é ineficiente para valores grandes de `n` (tempo de execução cresce rapidamente).

## 🐍 Requisitos

- Python 3.x

## 🚀 Execução

    python fibonacci.py
"""

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

# Imprimindo os primeiros 10 termos usando o loop
print("Sequência de Fibonacci (loop):")
for numero in fibonacci_loop(10):
    print(numero, end=" ")
print("\n")

# Imprimindo o 10º termo usando a recursão
print("10º termo da Sequência de Fibonacci (recursão):", fibonacci_recursao(10 - 1))