# p09.py
# Nome do programador: Gustavo de Oliveira Almeida
# Matrícula: es86755
# Data de criação: 06/04/2021
# Data atualização: 06/04/2021 - 10:30
# O programa tem como objetivo calcular o salário bruto dos funcionários
# de uma empresa.

def main():
    funcionarios = leiaFunc('funcionarios.csv')
    salariosBrutos = calcSalBruto('horas_trab.dat', funcionarios)

    # Imprime relatório dos salários brutos de todos os funcionários.
    print("\n***     Relatório dos Salários Brutos     ***"
          "\nMatrícula         Nome          Salário Bruto")
    for i in range(len(funcionarios)):
        print("{:7d}    {:20s}    {:8.2f}".format(funcionarios[i][0],
                                                  funcionarios[i][1],
                                                  salariosBrutos[i]))


def leiaFunc(nomeArq):
    # Abre o arquivo no formato csv contendo os dados dos funcionários:
    # matr,nome,cargo,salPorHora
    arqFuncs = open(nomeArq, 'r')

    # Gera o banco de dados dos funcionarios armazenando-o em uma lista
    # de tuplas.
    bd = []
    linha = arqFuncs.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')
        #print(dados)
        matr = int(dados[0])
        nome = dados[1]
        cargo = dados[2]
        salPorHora = float(dados[3])
        bd.append((matr, nome, cargo, salPorHora))
        linha = arqFuncs.readline().rstrip('\n')
    arqFuncs.close()
    return bd

def calcSalBruto(nomeArq, bd):
    arqSBrutos = open(nomeArq, 'r')
    bds = []
    i = 0
    linha = arqSBrutos.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(' ')
        horas_regulares = float(dados[0])
        horas_extras = float(dados[1])
        salBrutos = bd[i][3]*horas_regulares + (1.5*bd[i][3])*horas_extras
        bds.append((salBrutos))
        linha = arqSBrutos.readline().rstrip('\n')
        i = i + 1
    arqSBrutos.close()
    return bds
    

main()
