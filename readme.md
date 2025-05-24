# Algoritmo de Repetido Quadrado em Curvas de Edwards

## 📝 Descrição
Este trabalho prático tem como objetivo implementar o algoritmo de repetido quadrado para realizar multiplicaçõoes escalares eficientes em curvas de Edwards. As curvas de Edwards são uma forma de curva elíptica com propriedades aritméticas interessantes, particularmente no que diz respeito à completeza da lei de grupo.

### Algoritmo de Repetido Quadrado
O algoritmo de repetido quadrado é um método eficiente para calcular o múltiplo escalar de um ponto em uma curva elíptica. Dado um ponto P e um inteiro n, o algoritmo calcula nP da seguinte forma:

1. Escreva **n** em sua representação binária: n = (bk bk−1 . . . b1 b0)2.
2. Inicialize R = O.
3. Para i de k até 0:
    - R = R + R (Duplicação)
    - Se bi = 1, então R = R + P (Adição)
4. Retorne R

---

## 🛠️ Ferramentas utilizadas
- Linguagem Python.

---

## ⚙️ Funcionalidades

---

## 🧠 Como funciona
O programa executa os seguintes passos:

1. Recebe como entrada os parâmetros da curva de Edwards (a, b, d), um ponto P = (x, y)
na curva e um inteiro n;
2. Implementa a lei de grupo para a adição de pontos em curvas de Edwards;
3. Implementa algoritmo de repetido quadrado para calcular nP;
4. Retorna as coordenadas do ponto nP.
