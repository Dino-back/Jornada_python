'''
Faça um comparador onde indique se o primeiro número é maior que o segundoe vice versa, e verifique se é um número ou não
'''
primeiro_valor = input("Digite um valor:")
segundo_valor = input("Digite outro valor:")

if  (primeiro_valor.isdigit() and  segundo_valor.isdigit()) and (primeiro_valor < segundo_valor):
    print (f"O primeiro valor {primeiro_valor} é maior que o segundo {segundo_valor}")

elif (primeiro_valor.isdigit() and  segundo_valor.isdigit()) and (segundo_valor < primeiro_valor):
    print(f"O segundo valor {segundo_valor} é maior que o primeiro {primeiro_valor}")

elif (primeiro_valor.isdigit() and segundo_valor.isdigit()) and (primeiro_valor == segundo_valor):
    print("Valores iguais.")

else:
    print("Não é um número")
    