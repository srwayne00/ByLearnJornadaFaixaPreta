# Calculo do (I)ndice de (M)assa (C)orporal do Usuario

peso = int(input('Informe seu peso'))
altura = float(input('Informe sua altura'))

imc = peso/(altura * altura)
if imc < 18.5:
    print('Seu IMC é: ' ,imc, 'vamos para uma rodizio já!')
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é: ' ,imc, 'Continue o que esta fazendo que esta normal')
elif imc >= 25 and imc < 30:
    print('Seu IMC é: ' ,imc, 'Recomendo aumentar a frequencia das saladas')
elif imc >= 30 and imc < 40:
    print('Seu IMC é: ' ,imc, 'PAROU Lanches e pizzas, Vamos cuidar da saude primeiro')
else:
    print('Seu IMC é: ' ,imc, 'Está querendo morrer, sai desse computador e vai procurar um exercicio e uma dieta imediatamente :(')