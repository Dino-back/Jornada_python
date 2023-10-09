'''
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
#RESOLUÇÂO_1(Má pratica definição de variavel: Definir nova varíavel dentro de um bloco)
"""
numero_inteiro = input("Digite um número inteiro:")

if numero_inteiro.isdigit():
    numero = int(numero_inteiro)
    if numero % 2 == 1:
        print("O número é impar.")

if numero_inteiro.isdigit():
    numero = int(numero_inteiro)
    if numero % 2 == 0:
        print("O número é par.")

else:
    print ("Não é um número inteiro.")

print ("-"*10)
"""
#SOLUÇÃO_2(usando try e except)

entrada =input("Digite um número")

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro.')