'''
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
if idade < 18:
    print("Você é menor de idade.")
'''
'''
    idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
'''
'''
nota = 7

if nota >= 9:
    print("Aprovado com distinção.")
elif nota >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
'''
'''
idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir.")
else:
    print("Você é menor de idade.")
'''
'''
idade = 20
tem_carteira = False

if idade >= 18 and tem_carteira:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")
'''
#exercicios
'''
codigo = 1
if codigo == 1:
    print('Lapis')
codigo = 2
if codigo == 2:
    print('Caneta')
codigo = 3
if codigo == 3:
    print('Borracha')
codigo = 4
if codigo == 4:
    print('Caderno')
codigo = 5
if codigo == 5:
    print('Régua')
'''

'''
codigo = 6
produto = 'Produto não encontrado'
if codigo == 1:
    produto('Lapis')
codigo = 2
if codigo == 2:
    produto('Caneta')
codigo = 3
if codigo == 3:
    produto('Borracha')
codigo = 4
if codigo == 4:
    produto('Caderno')
codigo = 5
if codigo == 5:
    produto('Régua')
'''

#MEU
'''
salario = 1000
descricao = 1
if descricao == 1:
    desconto = salario * (30/100)
    porcentagem = '30%'
    descontado = salario - desconto
    
if descricao == 2:
    desconto = salario * (20/100 )
    porcentagem = '20%'
    descontado = salario - desconto

if descricao == 3:
    desconto = salario * (25/100 ) 
    porcentagem = '25%'
    descontado = salario - desconto

print('valor de desconto é:', desconto)
print('Seu salario:', salario)
print('porcentagem da aliquota:', porcentagem)
print('salario descontado:', descontado)
'''

#PROF
'''
#Salário Bruto
#Percentual de Desconto
#Desconto
#Salário Descontado

#1 - Solteiro = 30%
#2 - Casado = 20%
#3 - Outros = 25%

#desconto = salario * (percentual / 100)

salario_bruto = 10000
salario_liquido = salario_bruto
codigo_estado_civil = 2
percentual = 0
descricao_estado_civil = "Não Identificado"

if codigo_estado_civil == 1:
    percentual = 30
    descricao_estado_civil = "Solteiro"

if codigo_estado_civil == 2:
    percentual = 20
    descricao_estado_civil = "Casado"

if codigo_estado_civil == 3:
    percentual = 25
    descricao_estado_civil = "Outros"

salario_liquido = salario_bruto - (salario_bruto * (percentual / 100))

print(salario_bruto)
print(salario_liquido)
print(codigo_estado_civil)
print(descricao_estado_civil)
'''
'''
lado1 = 1
lado2 = 1
lado3 = 1
triangulo = 'isosceles'

if lado1 == lado2 and lado2 == lado3:
    triangulo = 'Equilatero'

if lado1 != lado2 and lado2 != lado3 and lado1 and lado3:
    print('escaleno')

'''
