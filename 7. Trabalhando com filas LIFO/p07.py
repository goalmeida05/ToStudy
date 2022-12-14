# -*- coding: utf-8 -*-
"""p07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jazkvCWw5MarVYlrZIfU9MlCo7N-2_Fc
"""

#Nome: Gustavo de Oliveira Almeida
#Matrícula: Es86755 
#Descrição: O programa analisará uma expressão aritimética e então retornar se o
#usuário digitou a quantidade certa de parênteses.

def main():
  while True:
    expr = str(input("Digite uma expressão com parênteses (ENTER para terminar):"))
    if not expr:
      break
    else: 
      print(analise_parenteses(expr)[0], analise_parenteses(expr)[1])


def analise_parenteses(expr):
  pilha = []
  for i in expr:
    if (i == '('):
      pilha.append('(')
    elif (i == ')'):
      if len(pilha) == 0:
        return expr, "Está ERRADO"
      ultimo = pilha.pop()
      if ultimo == i:
        return expr, "Está ERRADO"
  if len(pilha) != 0:
    return expr, "Está ERRADO"
  return expr, "Está OK"


main()