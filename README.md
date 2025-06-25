# 📊 study-repository - Fibonacci em Python

Este repositório apresenta duas formas simples de calcular a **Sequência de Fibonacci** utilizando Python: uma com **loop (iterativa)** e outra com **recursão**.

## 📌 Métodos Implementados

### 1. `fibonacci_loop(n)`
Gera os `n` primeiros termos da sequência de Fibonacci utilizando um loop.

```python
def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
