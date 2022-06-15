
"""
1. Em uma loja, compras a prazo possuem juros simples de 2% ao mês. Já as compras a
vista, possuem desconto de 10%. Escreva um algoritmo e um DFD que leia do usuário o valor da compra, e a forma de pagamento (1: pagamento a vista - 2: pagamento a prazo) o prazo, no caso das compras a prazo, e informe total a pagar ou o valor da parcela mensal da mercadoria Ex: Uma mercadoria que custe R$ 100,00 e será parcelada em 5 vezes, terá um acréscimo de 10% e, portanto valor total de R$110,00, sendo dividido em 5 parcelas de $22,00. Esta mesma mercadoria à vista teria um total a pagar de R$90,00


"""

# *Juros simples 2% ao mês
# *Compra a vista possuem desconte de 10%

### --------------------- ###

valor = float(input("Digite o valor da compra: "))
no_valor = 0
# Tenha opção de pagamento a prazo e pagamento a vista
entrada = input("Pagamento a vista ou a prazo (1/2): ")

# O programa vai ter o laço que representa quantas vezes vai pagar

vezes = 0

# 2% de algo é 0.02 * o valor

if entrada == '1':
    # pagamento a vista
    # é o valor menos o valor vezes 0.1 que é 10% do produto, é o desconto
    valor -= valor * 0.1

elif entrada == '2':
    # pagamento a prazo
    vezes = int(input("Quantas vezes quer pagar? "))
    # Precisa saber a porcentagem 
    # gravando o acrescimo que é 2% 
    acrescimo = valor * .02

    # O programa vai ter o laço que representa quantas vezes vai pagar
    for i in range(vezes):

        no_valor += acrescimo + (valor/vezes)


print(f"Total a pagar é {no_valor}, sendo R${no_valor/vezes:.2f} cada parcela.")
