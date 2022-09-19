# p08.py
# Nome: Gustavo de Oliveira Almeida 
# Matrícula: 86755
# Data: 25/03/2021
# Atualização: 25/03/2021
# Este programa irá receber uma data e nos retornar o dia anterior a ela
# verificando se o ano é bissexto ou não e as alterações que isso pode acarretar
# na subtração de datas.

def main():
    while True:
        linha = input('\nEntre com uma data (dd mm aaaa):\n')
        dia, mes, ano = tuple(map(int, linha.split(' ')))
        dia1, mes1, ano1 = subtraia_1dia(dia, mes, ano)
        print('O dia anterior é {:02d}/{:02d}/{:4d}.'.format(dia1, mes1, ano1))
        resp = input('Deseja continuar (s/n)? ')
        if resp == 'n' or resp == 'N': break

# Implemente aqui a função bissexto(a).
def bissexto(a):
    bis = bool
    if (a % 4 == 0 and a% 100 !=0) or (a % 400==0):
        bis = True
    else:
        bis = False
    return bis
        


# Implemente aqui a função num_dias_no_mes(m, a).
def num_dias_no_mes(m,a):
    numDiasMes = [31,29 if bissexto(a) else 28,31,30,31,30,31,31,30,31,30,31]
    return numDiasMes[m-1]



# Implemente aqui a função subtraia_1dia(d, m, a).    
def subtraia_1dia(d,m,a):
    if d == 1:
        if m ==1:
            m = 12
            a = a - 1
        else:
            m = m - 1
        d = num_dias_no_mes(m,a)
    else:
        d = d - 1
    return d,m,a
            


main()
