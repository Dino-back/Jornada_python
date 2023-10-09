"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Qual seu nome:")
idade = input("Sua idade:")
 
if nome and idade :
    print("Seu nome é {} e tem {} idade.".format(nome, idade))
    print("Seu nome de tras pra frente é {}".format(nome[::-1]))
    if " " in nome:
            print("Seu nome contem espaços")

    else :
            print("Seu nome não contem espaços.")
    
    print("Seu nome tem {} número de letras".format(len(nome)))
    print("A primeira letra do seu nome é {}".format(nome[0]))
    print("A ultima letra é {}".format(nome[-1]))
else :
    print("Desculpe, você deixou campos vazios.")
