
def calcNumerador(n):
  #fatorial não recursivo
  result = 0
  for x in range(n+1):
    if x == 0:
      result = 1
    else:
      result = result * x
  print(result)

#def calDenominador(x,n)

calcNumerador(4)

