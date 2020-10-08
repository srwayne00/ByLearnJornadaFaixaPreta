# Condicionais
    # Principal forma de atribuir uma lógica ao seu código.
    # Basicamente é uma tomada de decisão caso a condição seja verdadeira.

# Ex:
    # Se o dia estiver quente:
        # Vou tomar um sorvete
        # Vou para a praia

    # Do contrário (se não):
        # Comer um chocolate
        # Maratonar Netflix

temperatura = 'frio'

print(temperatura)

###############################################

if temperatura == 'quente':
  print('Vou tomar um sorvete de Flocos')
  print('Vou para a praia (mentira, aqui não tem praia)')
else:
  print('Vou comer um chocolate')
  print('Vamos assistir Cobra Kai')

###############################################

horario = 'tarde'

if horario == 'manhã':
  print('O sol está quente')
elif horario == 'tarde':
  print('O por do sol está chegando')
else:
  print('A lua está linda')
  print('Esta na hora da jornada python')

###############################################

idade = 17

if idade >= 18:
  print('Você já pode beber, mas com moderação')
else:
  print('Você não pode beber')

###############################################
temperatura = 37

if temperatura <= 30:
  print('Aceitável')
else: 
  print('Socorro está muito quente')

###############################################

altura = 1.75

if altura > 1.80:
  print('O Felipe é alto')
else:
  print('O Felipe é baixinho')

###############################################

quente = False
gosta_praia = False
gosta_chocolate_quente = True

if quente == True:
  print('Está quente')
  if gosta_praia == True:
    print('Vá para a praia')
  else: 
    print('Não vá a praia')
else:
  print('Está frio')
  if gosta_chocolate_quente == True:
    print('Tome um chocolate quente')
  else:
    print('Não tome chocolate quente')

###############################################

dia = input('Que dia da semana é hoje? ')

if dia == 'sabado' or dia == 'domingo':
  print('É fim de semana, bora beber :D')
else: 
  print('Não é fim de semana, partir trampar/estudar :)')

###############################################

# 1, 3, 6 e 10  => Válido
# qualquer outro => Inválido

numero = 11

if numero == 1:
  print('é valido')
elif numero == 3:
  print('é valido')
elif numero == 6:
  print('é valido')
elif numero == 10:
  print('é valido')
else:
  print('é inválido')

###############################################

# Operadores Lógicos
    # Servem para fazer uma condição composta

    # E => Ambas precisam ser verdade
    # OU => Pelo Menos UMA precisa ser verdade

# Ex:

    # Se for manhã E estiver sol
    # Se for sábado OU domingo
    # E => AND
    # OU => OR

###############################################

numero_sorte = 10

numero = int(input('Escolha um numero: '))

if numero != 10:
  print('errou o numero')
else : print('Acertou, miseravi!')

numero = 6

###############################################

if numero == 1 or numero == 3 or numero == 6 or numero == 10:
  print('É válido')
else:
  print('É inválido')

###############################################

# Laços de Repetição
    # É uma excelente forma de evitar repetição de código.
    # Ele vai executar n vezes uma operação.

# n => Quantidade de vezes definida.

# De 1 até 10 vamos printar todos os numeros
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)


# Na programação o Minimo (1) é INCLUSIVO => Ele existe
# Já é Maximo (10) é EXCLUSIVO => Ele não existe

# for => Nossa palavra-chave para Repetição.
# variavel => O dado que estamos trabalhando no momento atual.
# in => Nossa palavra-chave para "onde vamos repetir?"
# invervalo/sequencia => O que vamos repedir
for numero in range(10):
  print(numero)

nomes = ['Felipe', 'Fabiana', 'Paulo', 'Katia']
for nome in nomes:
  print('O nome atual é', nome)
  if nome == 'Felipe':
    print('(Ou Zarcky)')


# len => Tamanho em ingles (abreviação)
      #  1  2   
notas = [6, 7.5]
len(notas)

# range = intervalo em ingles
# range(1, 10) => intervalo de 1 até 10
###############################################

# Função
    # Toda função é uma rotina.
    # Eu defino (def) uma rotina e a executo quantas vezes quiser.
    # É uma excelente forma de deixar nosso dinâmico e sem repetição.

# Definindo a função
def nome_funcao(): 
  # Código da função
  print('Codigo da função')

# Chamando a função
nome_funcao()

def mostrar_nome():
  print('Wagner Oliveira')

mostrar_nome()

###############################################

# Parâmetro/Argumento da função
    # É uma maneira de enviar dados para a função

def mostrar_nome(nome_atual):
  print(nome_atual)
  
mostrar_nome('Edgar')
mostrar_nome('Fabiana')
mostrar_nome('Paulo')
mostrar_nome('Katia')


def calcular_media(nota1, nota2):
  soma = nota1 + nota2
  media = soma / 2 
  print(media)


primeira_nota = float(input('Sua primeira nota: '))
segunda_nota = float(input('Sua segunda nota: '))

calcular_media(primeira_nota, segunda_nota)
###############################################

# Return
    # Quando queremos retornar um valor da função, ou seja, a função devolve um valor calculado, nós usamos o Return.
def calcular_media(nota1, nota2):
  soma = nota1 + nota2
  media = soma / 2 
  return media


media_calculada = calcular_media(10,8)

print(media_calculada)

##########

# IMC => PESO (KG) / ALTURA (M)²

def numero_quadrado(numero):
  quadrado = numero * numero 
  return quadrado 

def calcular_imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada

  return meu_imc

imc = calcular_imc(66, 1.75)
print(imc)

#############

# IMC => PESO (KG) / ALTURA (M)²

def numero_quadrado(numero):
  quadrado = numero * numero 
  return quadrado 

def calcular_imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada

  return meu_imc

def classificar_imc(meu_imc):
  if imc < 18.5:
    print('Magreza')
  elif imc >= 18.5 and imc < 25:
    print('Normal')
  elif imc >= 25 and imc < 30:
    print('Sobrepeso')
  elif imc >= 30 and imc < 40:
    print('Obesidade')
  else:
    print('Obesidade Grave')

imc = calcular_imc(66, 1.75)

print('Seu IMC é:', imc)

print('Sua classificação é:')
classificar_imc(imc)
###############################################