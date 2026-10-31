# Captura-Pokemon

EP2 – Simulador de captura de pokémons (MAC2166 – Introdução à Computação, Poli-USP)

Neste projeto em Python, implementei o núcleo de um jogo simples: um treinador lança pokébolas contra um pokémon parado, e o programa simula a trajetória até que a bola capture o pokémon ou atinja o chão.

Como funciona

O pokémon é modelado como um círculo (posição e raio) e a pokébola também. A captura ocorre quando a distância entre os centros é menor ou igual à soma dos raios.
O treinador tem até 3 tentativas, e a cada uma informa posição inicial, velocidade e ângulo de lançamento (de 0° a 180°, podendo lançar “para trás”).
A trajetória é calculada de forma iterativa, em intervalos de tempo Δt: movimento uniforme no eixo x e uniformemente variado no eixo y, com gravidade de 9,81 m/s².
Se não houver captura, o programa informa a menor distância entre a pokébola e o pokémon e as coordenadas do ponto mais próximo da trajetória.

O diferencial: sem bibliotecas matemáticas
Em vez de usar math, implementei do zero:

Seno e cosseno pela série de Taylor, com critério de parada de 1e-10 e conversão de graus para radianos.
Raiz quadrada pelo método de Newton (recorrência de Heron), usada no cálculo de distâncias.

Organização do código
O programa foi dividido em funções com responsabilidades claras: seno, cosseno, raizQuadrada, atualizaPosicao, atualizaVelocidade, distanciaPontos e simulaLancamento.

O que pratiquei: modularização com funções, laços e condicionais, aproximação numérica de funções, simulação física discreta e tratamento de casos de borda.

#Python #USP #Programação #Física #MétodosNuméricos #Engenharia
