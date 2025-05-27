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


# Entradas a serem fornecidas:
print("Insira os parâmetos da curva de Edwards:")
a = int(input("a: "))
b = int(input("b: "))
d = int(input("d: "))

p = {"x": None, "y": None}

print("\nInsira um ponto P = (x, y):")
p["x"] = int(input("Valor de x: "))
p["y"] = int(input("Valor de y: "))

n = int(input("\nInsira um inteiro n: "))

print(dobra_e_soma(n, p, a, d))
