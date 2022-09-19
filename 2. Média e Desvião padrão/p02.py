#
# Nome do programador: Gustavo de Oliveira Almeida
# Matrícula: es86755
# Data: 09/02/2021
# Dado um arquivo que contém N notas, o programa realizará cálculos e fornecer dados estatísticos em relação a essas notas
#como a média, desvião padrão e localização da maior e menor nota.
#

import math
import numpy as np

def main():
    nomeArq  = 'notas_inf100.dat'
    arqNotas = open(nomeArq, 'r')
    linhas = arqNotas.read().split('\n')

    notas = np.array(list(map(float, linhas)))

    print('%d notas lidas.' % len(linhas))
    print()
    print('Média das notas:         %5.1f' % media(notas))
    print('Desvio padrão das notas: %5.1f' % desvioPad(notas))
    print('Maior nota:              %5.1f' % maximo(notas))
    print('Menor nota:              %5.1f' % minimo(notas))

#
# Insira abaixo a implementação das funções requeridas:
#

def media(notas): #Aqui estamos calculando a média das notas
    if len(notas)>0: #teste para o arquivo de notas recebido
        soma = 0
        for i in range (0, len(notas)):
            soma = soma + notas[i] #percorrendo o arranjo sem alterá-lo
        soma = soma/len(notas)
        return soma #retorno ocorrendo ok
    else:
        print('Faltando dados para concluir o cálculo')


def desvioPad(notas):
    if len(notas)>1: #teste para o arquivo de notas recebido
        desvioquad = 0 #definindo a variável da soma dos quadrados
        desvioquadmed = 0 # definindo a media do quadrado da soma
        for i in range(0, len(notas)):  #percorrendo novamente as notas sem alterá-las
            desvioquad = desvioquad + notas[i]**2
            desvioquadmed = desvioquadmed + notas[i]
        desvioquadmed = (desvioquadmed**2)/len(notas)
        desvio = math.sqrt((desvioquad - desvioquadmed)/(len(notas)-1)) #expressão final
        return desvio #retorno ocorrendo ok
    else:
        print('Faltando dados para concluir o cálculo')

def maximo(notas):
    if len(notas)>0: #teste para o arquivo de notas recebido
        maximo = max(notas, key=float) #percorrendo o arranjo e proucurando a maior nota
        return maximo #retornando ok
    else:
        print('Faltando dados para concluir o cálculo')

def minimo(notas):
    if len(notas)>0: #teste para o arquivo de notas recebido
        minimo = min(notas, key=float) #percorrendo o arranjo e proucurando a menor nota
        return minimo #retornando ok
    else:
        print('Faltando dados para concluir o cálculo')

if __name__ == '__main__':
    main()

