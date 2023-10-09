nome = input("Qual seu nome?")
peso = float (input("Seu peso?"))
altura = float (input("Sua altura em cm?"))
altura2 = altura / 100
imc= peso / (altura2 * altura2)

print("{} você tem {:.2f} de altura,\n Seu peso é {} e seu IMC é: {:.2f}".format(nome, altura, peso, imc))
 
if imc < 18.5:
    print("Com base no seu IMC você esta em baixa de peso.")

elif imc >= 18.5 and imc < 24.9:
    print ("Com base no seu IMC você está com peso normal.")

elif imc >= 24.9 and imc < 30:
    print ("Com base no seu IMC você esta em sobrepeso:")

else:
    print("Com base no seu IMC você esta com obesidade.")