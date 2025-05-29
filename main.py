import matplotlib.pyplot as plt
import numpy as npy

# Função que implementa a Lei de Grupo para a adição de pontos em curvas de Edwards
def lei_do_grupo(x1, y1, x2, y2, a, d):
    # Novo ponto obtido a partir da soma dos dois pontos.
    np = {"x": None, "y": None}

    # Calculando o valor de x:
    np["x"] = (x1 * y2 + x2 * y1) / (1 + d * x1 * x2 * y1 * y2)

    # Calculando o valor de y:
    np["y"] = (y1 * y2 - a * x1 * x2) / (1 - d * x1 * x2 * y1 * y2)

    return np


# Função que implementa o Algoritmo de Dobra e Soma
def dobra_e_soma(n, p, a, d):
    # "r" recebe o ponto neutro da curva de Edwards O = (0, 1).
    r = {"x": 0, "y": 1}

    # Convertendo o inteiro "n" pra binário
    nb = int_para_binario(n)

    # Para cada byte no número "n" fazemos:
    for i in nb:
        #r += r
        r = lei_do_grupo(r["x"], r["y"], r["x"], r["y"], a, d)

        if int(i) == 1:
            #r += p
            r = lei_do_grupo(r["x"], r["y"], p["x"], p["y"], a, d)
    
    return r


# Função que converte o inteiro "n" para binário
def int_para_binario(n):
    if n == 0:
        return "0"
    
    binario = ""

    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2

    return binario

# Função que gera o gráfico da curva com os pontos P e nP
def plotar_curva_e_pontos(a, d, p, np):
    x_vals = npy.linspace(-15, 15, 1000)
    y_vals = npy.linspace(-15, 15, 1000)
    X, Y = npy.meshgrid(x_vals, y_vals)
    
    F = a * X**2 + Y**2 - 1 - d * X**2 * Y**2

    plt.contour(X, Y, F, levels=[0], colors='blue', linewidths=1.5, linestyles='solid')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)

    plt.plot(p["x"], p["y"], 'go', label='Ponto P')
    plt.plot(float(np["x"]), float(np["y"]), 'ro', label='nP = {}P'.format(n))

    plt.title("Curva de Edwards e Pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.show()


# Entradas a serem fornecidas:
print("Insira os parâmetos da curva de Edwards:")
a = int(input("a: "))
d = int(input("d: "))

p = {"x": None, "y": None}

print("\nInsira um ponto P = (x, y):")
p["x"] = float(input("Valor de x: "))
p["y"] = float(input("Valor de y: "))

n = int(input("\nInsira um inteiro n: "))

np = dobra_e_soma(n, p, a, d)

print(f"\nPonto nP: {np}")
plotar_curva_e_pontos(a, d, p, np)
