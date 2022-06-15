

# Primeiro pensei em como dar o desconto do produto

# Primeiro pego o que o usuario digitou e 
# digo que é um numero flutuante
valor = float(input("Digite o valor da compra: "))

# Essa é a conta que usei para dar o desconto de 10%
# que é o valor - 10% dele mesmo é ele descontado
valor -= valor * 0.1

# E temos o produto descontado
print(f"Esse é o valor descontado 10% R${valor:.2f}" )
