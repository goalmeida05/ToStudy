# p13.py
# Programador: Gustavo de Oliveira Almeida
# Matrícula: es86755
# Data de criação: 07/05/2021
# Data de atualização: 07/05/2021
# Produz um horário escolar usando uma heurística muito simples baseada
# na estrutura de dados conjunto. Os dados de entrada são as dsiciplinas
# a ser oferecidas e as matrículas dos alunos que farão algumas das
# disciplinas oferecidas.

import sys

def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDisc = 'disciplinas.txt'
    nomeArqMatric = 'matriculas.txt'
    if len(sys.argv) > 1:
        nomeArqDisc = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatric = sys.argv[2]
    
    discs = leia_arq_disciplinas(nomeArqDisc)
    matrics = leia_arq_matriculas(nomeArqMatric)

    hor = faz_horario_escolar(discs, matrics)
    # Imprime as sessões não conflitantes do horário.
    print('\nSessões:')
    for i in range(len(hor)):
        print('{:3d}: '.format(i), sorted(hor[i]))


# Lê uma disciplina por linha do arquivo cujo nome externo é 'nomearq'.
# Retorna a lista de disciplinas lidas.
####                                                                 ####
def leia_arq_disciplinas(nomearq):
    try:
        with open(nomearq, 'r') as arq:
          linhas = arq.readline().rstrip('\n')
          arqdisciplinas = []
          while linhas != '':
            arqdisciplinas.append(linhas)
            linhas = arq.readline().rstrip('\n')
          arq.close()
        return arqdisciplinas
    except:
        print("Erro o arquivo nao existe.")
        return 0
####                                                                 ####




# Lê, por linha, o nome de um aluno e as disciplinas em que ele se matriculou.
# Os dados em cada linha são separados por uma vírgula. O nome externo do
# arquivo é passado como parâmetro. Retorna um dicionário em que a chave é o
# nome de um aluno e o valor associado é o conjunto de disciplinas em que o
# aluno se matriculou.
####                                                                 ####
def leia_arq_matriculas(nomearq):
    try:
        with open(nomearq, 'r') as arq:
          linhas = arq.readline().rstrip('\n')
          dicmatriculas = {}
          while linhas != '':
            dados = linhas.split(',') 
            dicmatriculas[dados[0]]= dados[1]
            linhas = arq.readline().rstrip('\n')
          arq.close()
        return dicmatriculas
    except:
        print("Erro o arquivo nao existe.")
        return 0
####                                                                 ####




####                                                                    ####
def faz_horario_escolar(disciplinas, matriculas):
    emptySet = set()
    conflitos = [ emptySet for d in disciplinas]
    for a in matriculas.keys():
        for d in range(len(disciplinas)):
            if disciplinas[d] in matriculas[a]:
                conflitos[d] = conflitos[d].union(matriculas[a])
    restantes= set(disciplinas)
    horario = []
    while restantes != emptySet:
        i = 0
        d = disciplinas[i]
        while d not in restantes:
            i = i + 1
            d = disciplinas[i]
        sessao = { d }
        tentativa = restantes - conflitos[i]
        for s in range(len(disciplinas)):
            if disciplinas[s] in tentativa:
                if(conflitos[s] & sessao) == emptySet:
                    sessao.add(disciplinas[s])
        restantes = restantes - sessao
        horario.append(sessao)
        return horario
####                                                                    ####


#Não entendi o porque do erro, as listas disciplinas e matriculas estão identicas
#E quando vai produzir a parte final da erro, trabalhei alterando o return horario
# em outros pontos da identação e sempre retorna o mesmo resultado   

if __name__ == '__main__':
    main()
