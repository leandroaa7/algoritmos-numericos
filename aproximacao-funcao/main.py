#!/usr/bin/env python
# -*- coding: utf-8 -*-

denominadorList = []
numeradorList = []

def calcFatorial(n):
  #fatorial não recursivo
  result = 0
  for i in range(n+1):
    if i == 0:
      result = 1
    else:
      result = result * i
  #print(result)
  return result

def calcNumerador(n):
  numerador = 0
  for i in range(n+1):
    numerador = calcFatorial(i)
    numeradorList.append(numerador)
  #print(numeradorList)

def calcDenominador(x,n):
  denominador = 0
  for i in range(n+1):
    denominador = x**i
    denominadorList.append(denominador)
  #print(denominadorList)

def calcTaylor(x,n):
  calcNumerador(n)
  calcDenominador(x,n)
  somatoria = 0 #resultado da serie de taylor
  somatoriaArrendondada = 0
  for i in range(n+1):
    somatoria += denominadorList[i]/numeradorList[i]
  #print(somatoria)
  somatoriaArrendondada = round(somatoria, 4)
  print(' ')
  print(somatoriaArrendondada)

def main():
  print('Série de Taylor')
  x = int(input('Digite o valor de x: '))
  n = int(input('Digite o valor de n: '))
  calcTaylor(x,n)

if __name__ == "__main__":
  main()

