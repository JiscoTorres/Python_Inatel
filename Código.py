

'''
As tres aspas servem para comentários em bloco.
'''

# Serve para comentário em linha.


# Não existe diferença da utilização de ("") e ('').


#--------------------------------------------------------#



#CALCULOS - Com o comando print.

print(3+3+3) # Com esse tipo de comando,sem os apóstrofos, a soma dos números será impressa na tela. ~Resultado = 9~

print(5*2) # Multiplicação de números, utiliza-se um asterisco. ~Resultado = 10~

print(4**2) #Exponeciação, ou seja, quatro elevado a dois; para isso, utiliza-se dois asteriscos. ~Resultado = 16~



#--------------------------------------------------------#





#-------------------------1------------------------------#



'''IMPRIMIR MENSAGENS - Com o comando print.'''

print("Olá, mundo")
print('Hello World') # Quando se coloca textos dentro dos apóstrofos, o mesmo texto será impresso na tela(Console).


#--------------------------------------------------------#





#--------------------------2-----------------------------#



'''DECLARANDO VARIÁVEIS '''



nome= "João Francisco" #Declarou a variável "nome"
sobrenome = "Torres"

print(nome + sobrenome) # Por serem palavras, pode-se usar no print o simbolo de + para colocar o nome e sobrenome em sequencia.
print(f'Meu Nome é: {nome}') #ou
print('Meu nome é: ' + nome)#ou
print(f'Meu Nome é: {nome} ' + sobrenome)



Idade = 17
Altura = 1.80 # Variável do tipo Float
Faz_Ete = True #Variável do tipo Booleanea
Coordenada = 5 +2j #Para números complexos

print(Idade)
print(Altura)
print(Faz_Ete)
print(Coordenada)
print(f'Eu tenho {Idade} anos') #f é para poder não comentar a parte {}
print('Meu nome é', nome, 'e eu tenho', Idade, 'anos')


#--------------------------------------------------------#




#---------------------------3----------------------------#


'''ENTRADA DE DADOS'''
#Para fazer com que a pessoa informe algo, colocar "input"
#Fazer com que o Usuário informe os valores impregados às variáveis


name= input('Digite o seu nome?')#isso serve para o usuário informar qual é seu nome
idade= input('Qual a sua idade?')
cidade= input('Em qual cidade você mora?')

print(name, idade, cidade)
print('O nome do usuário é: ' + name)

NumeroPreferido = int(input("Digite seu número inteiro predileto:")) # int serve para converter a string criada para um número inteiro
SuaAltura = float(input("Digite sua altura: ")) # Float para números "quebrados"
print(type(name)) #mostrará o tipo da variável


#--------------------------------------------------------#


''' EXERCICIOS '''

# 1.
# a) Faça um programa que pergunte o nome, a idade e a altura do usuário, e em seguida, mostre os resultados na tela.
NomeUser= input("Informe seu Nome: ")
IdadeUser= int(input("Informe sua idade: "))
AlturaUser= float(input("Informe sua altura: "))

print(f'O nome do usuário é: {NomeUser}, sua idade é {IdadeUser} e sua altura é {AlturaUser}') #ou
print(f'O nome do usuário é: {NomeUser}\n Sua idade é {IdadeUser}\n Sua altura é {AlturaUser}') # \n para pular para a próxima linha


# b) Faça um programa que solicite dois números inteiros para o usuário, realize a soma e mostre o resultado na tela.
Numero1= int(input("Informe o primeiro número: "))
Numero2= int(input("Informe o segundo número: "))

print(f"Seu número é {Numero1+Numero2}")


#--------------------------------------------------------#





#----------------------4---------------------------------#

'''ESTRUTURA CONDICIONAL (IF, ELSE, ...) '''



# EXEMPLO: informar se o usuário de menor ou maior de idade.
idadeUsuario= int(input('Informe sua idade: '))

if idadeUsuario < 18:
    print('O usuário é menos de idade!')

else:
    print('O usuário é maior de idade!')
#--------------------------------------------------------#




#-------------------------5------------------------------#

''' Utilização dos Operadores E, AND, OR, NOT '''
# E =
# OR = or
# AND = and
# NOT = not


#EXEMPLO and: Informar se o número está entre 0 e 10:

Num= int(input('Digite um número inteiro'))

if Num>=0 and Num<=10:
    print('O número digitado está entre 0 e 10!')
else:
    print('O número está fora do intervalo de zero e 10!')


#EXEMPLO not: Utilizar o not para inverter o valor de variaveis booleanas.
Valor= bool(input("Informe um valor lógico para inverter (TRUE ou FALSE): "))
Valor_Invertido= not Valor
print(f"O valor invertido foi {Valor_Invertido}")

#--------------------------------------------------------#




#------------------------6-------------------------------#

'''ESTRUTURAS DE REPETIÇÃO (WHILE, FOR)'''


#EXEMPLO while:
NumeroWhile = int(input("Até qual número você quer contar?"))

i = 0 # i é uma variável que serve para o controle de repetição

while i <= NumeroWhile:
    print(i)
    i= i +1



#EXEMPLO for:
NumeroFor = int(input("Até que número voce quer contar? "))# FOR é um loop, para fazer várias operações ao mesmo tempo.

for i in range (0, NumeroFor+1):
    print(i)


#EXEMPLO for 2:
frutas = {'Banana Nanica', 'Abacaxi', 'Maça Papaia', 'Naiga', 'Limão'}
for i in range(len(frutas)):
    if frutas[i] == 'Limão' or frutas[i] == 'Naiga':
        print(frutas[i])
        print(i)

#--------------------------------------------------------#



'''          MÓDULOS                 '''

'''

#--------------------------------------------------------#
MÓDULO OS


#EXEMPLOS DE COMANDOS:
# ipconfig
# arp-a
# whoami - Diz qual o nome do usuário que está usando o computador
# dir
# ping www.uol.com.br-n 1
# netstat -an


import os
os.system("ipconfig")
os.system('www.etefmc.com')

resultado = os.popen("ping www.etefmc.com.br").read() # "popen" serve para salvar em uma variável; ".read" no final serve para converter o resultado final em uma string.
print(resultado)
#--------------------------------------------------------#


#--------------------------------------------------------#
MÓDULO THREADING

# Este codigo pingará em 3 sites diferentes, um atrás do outro.
# No final irá dizer quanto tempo levou para executar esse código.


urls = ["www.icarly.com", "www.clubpenguin.com", "www.facebook.com"]
tempo1 = time.time()

for i in urls:
    os.system("ping " + i)
    
    tempo = time.time - tempo1
    print(f"\ nTempo de execução: {tempo} segundos.")
    
#--------------------------------------------------------#



#--------------------------------------------------------#
Módulo Socket

from socket import*
import threading

servidor = socket(AF_INET,SOCK_STEAM)
servidor.bind(("121.0.0.1",1234))
servidor.listen(1)

cliente, endereco = servidor.acept()
#--------------------------------------------------------#
'''
