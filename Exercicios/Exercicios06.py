"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora ')

try:
    hora = float(entrada)

    if hora >= 0 and hora <= 11.59:
        print(" Bom dia!")
    
    elif hora >= 12 and hora <= 17.59:
        print('Boa tarde!')
    
    elif hora >= 18 and hora <= 23.59:
        print('Boa noite!')
    
    else:
        print('Não conheço esse horario.')

except:
    print('Digite apenas números.')