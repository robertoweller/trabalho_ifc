"""
6. Em outra tabela, o National Health and Nutrition Examination Survey (NHNES). classifica-se homens de mulheres de modo diferente de acordo com o IMC:
Homens: 
a) abaixo do peso ideal - IMC abaixo de 20,7 
b) no peso ideal - IMC entre 20,8 e 27,8 
c) acima do peso ideal - IMC entre 27.9 e 31.1 
d) obeso - IMC acima de 31.1


a) abaixo do peso ideal - IMC abaixo de 19,1 
b) no peso ideal - IMC entre 19,2 e 27,3 
c) acima do peso ideal - IMC entre 27.4 e 32,3 
d) obeso - IMC acima de 32.3

Escreva um algoritmo e um DFD que solicite ao usuário, o sexo, o peso e a altura e classifique-o de acordo com esta nova tabela"""


# Peso homem
h_baixo = 20.7
h_ideal = [20.8, 27.8]
h_acima = [27.9, 31.1]
# h_obeso = 31.1

# Peso mulher
m_baixo = 19.1
m_ideal = [19.2, 27.3]
m_acima = [27.4, 32.3]
# m_obeso = 32.3

# Upper é para deixar a letra maiuscula caso o usuario digite minuscolo
sexo = input("Digite seu sexo (F/M): ").upper()

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = float(f"{peso / (altura * altura):.1f}")


print(f"\nSeu IMC é de {imc}\n")

if sexo == "M":
    if imc <= h_baixo:
        print("Seu IMC está baixo do peso ideal - IMC abaixo de 20,7.")
    
    elif imc >= h_ideal[0] and imc <= h_ideal[1]:
        print("Seu IMC está no peso ideal - IMC entre 20,8 e 27,8")

    elif imc >= h_acima[0] and imc <= h_acima[1]:
        print("Seu IMC está acima do peso ideal - IMC entre 27.9 e 31.1")

    else:

        print("Seu IMC está obeso - IMC acima de 31.1")


if sexo == "F":
    if imc <= m_baixo:
        print("Seu IMC está abaixo do peso ideal - IMC abaixo de 19,1 ")

    elif imc >= m_ideal[0] and imc <= m_ideal[1]:
        print("Seu IMC está no peso ideal - IMC entre 19,2 e 27,3")

    elif imc >= m_acima[0] and imc <= m_acima[1]:
        print("Seu IMC está acima do peso ideal - IMC entre 27.4 e 32,3")

    else:

        print("Seu IMC está obeso - IMC acima de 32.3")

