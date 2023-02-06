print("Formatação de valores")

# Atribuindo valores por ordem de índice informado.
print("Tentativa {1} de {0}".format(3, 10))
# Imprime: "Tentativa 10 de 3", ao invés de "Tentativa 3 de 10"


""" Formatando valor recebido para Float  (f)"""

# Após o ponto, retornará apenas 2 casas decimais. Caso valor seja próximo, ele arredondará.
print("R$ {:.2f}".format(1.455667))
# Imprime: "R$ 1.46"

# Após o ponto, retornará 7 caracteres. Dentro destes 7 após o ponto, deve retornar apenas 2.
print("R$ {:7.2f}".format(1234.45))
# Imprime: R$ 1234.45

# Caso o valor que seja informado não comporte 7 caracteres, ele completará o restante com "espaço em branco", respeitando a formatação do ponto conforme os demais.
print("R$ {:7.2f}".format(234.45))

# Caso o valor que seja informado não comporte 7 caracteres, ele completará o restante com "0", respeitando a formatação do ponto conforme os demais.
print("R$ {:07.2f}".format(234.45))


""" Formatando valor recebido Int  (d)"""


# Retornará 2 caracteres. Caso venha abaixo de 2 caracteres, ele completará com espaço em branco.
print("R$ {:2d}".format(8))
# Imprime: R$  8

# Retornará 2 caracteres. Caso venha abaixo de 2 caracteres, ele completará com 0.
print("R$ {:02d}".format(8))
# Imprime: R$  08


#Formatando uma data com o int
print("Data {:02d}/{:02d}/{:4d}".format(5,2,2023))
# Imprime: Data 05/02/2023
