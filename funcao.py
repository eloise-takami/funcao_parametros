from random import randint
numeros = list()
def maior(num):
    return max(num)
def sorteio(num):
    for x in range(1,6):
        n = randint(1,100)
        num.append(n)
def somapar(num):
    soma = 0
    for x in num:
        if x % 2 == 0:
            soma += x
    return soma
print("Antes dos valores",numeros)
sorteio(numeros)
print("Depois dos valores",numeros)
print("---------")
print("O maior numero é",maior(numeros))
print("A soma dos numeros pares é:",somapar(numeros))
