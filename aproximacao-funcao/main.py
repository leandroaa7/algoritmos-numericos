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
  print(numeradorList)

def calcDenominador(x,n):
  denominador = 0
  for i in range(n+1):
    denominador = x**i
    denominadorList.append(denominador)
  print(denominadorList)

