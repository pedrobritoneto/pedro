import AC02


# Pedro Pereira de Brito Neto RA: 1902175
# Scarlet Fernanda Machado Barros da Silva RA: 1902346

# RETORNAR ERRO
lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 4000.00, "OTHER OFFICE"]
salario = AC02.calcular_salario(lista_inf)
if salario == TypeError:
    print('ESSE CARGO NÃO EXISTE')

# TESTE PARA DESENVOLVEDOR
try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 5000.00, "DESENVOLVEDOR"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 4000.
    print("TESTE DESENVOLVEDOR MAIOR OU IGUAL 3K ESTÁ CERTO")
except AssertionError:
    print('TESTE DESENVOLVEDOR MAIOR OU IGUAL 3K DEU ERRO')

try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 2000.00, "DESENVOLVEDOR"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 1800.
    print("TESTE DESENVOLVEDOR MENOR QUE 3K ESTÁ CERTO")
except AssertionError:
    print('TESTE DESENVOLVEDOR MENOR QUE 3K DEU ERRO')

# TESTE PARA ANALISTA
try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 2000.00, "ANALISTA"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 1500
    print("TESTE ANALISTA MAIOR OU IGUAL 2K ESTÁ CERTO")
except AssertionError:
    print('TESTE ANALISTA MAIOR QUE 2K DEU ERRO')

try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 1000.00, "ANALISTA"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 850
    print("TESTE GERENTE MENOR QUE 2K ESTÁ CERTO")
except AssertionError:
    print('TESTE ANALISTA MENOR QUE 2K DEU ERRO')

# TESTE PARA GERENTE
try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 5000.00, "GERENTE"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 3500
    print("TESTE GERENTE MAIOR OU IGUAL 5K ESTÁ CERTO")
except AssertionError:
    print("TESTE GERENTE MAIOR OU IGUAL 5K DEU ERRO")

try:
    lista_inf = ["Pedro Brito", "pp.n@hotmail.com", 4000.00, "GERENTE"]
    salario = AC02.calcular_salario(lista_inf)
    assert salario == 3200
    print("TESTE GERENTE MENOR QUE 2K ESTÁ CERTO")
except AssertionError:
    print('TESTE GERENTE MENOR QUE 2K DEU ERRO')
