def calcular_salario(lista):
    try:
        if lista[3] != 'DESENVOLVEDOR' and lista[3] != 'ANALISTA' \
             and lista[3] != 'GERENTE':
            raise TypeError
    except TypeError:
        return TypeError
    if 'DESENVOLVEDOR' in lista:
        if lista[2] >= 3000:
            salario = lista[2] - (lista[2]/100)*20
            return salario
        else:
            salario = lista[2] - (lista[2]/100)*10
            return salario
    elif 'ANALISTA' in lista:
        if lista[2] >= 2000:
            salario = lista[2] - (lista[2]/100)*25
            return salario
        else:
            salario = lista[2] - (lista[2]/100)*15
            return salario
    elif 'GERENTE' in lista:
        if lista[2] >= 5000:
            salario = lista[2] - (lista[2]/100)*30
            return salario
        else:
            salario = lista[2] - (lista[2]/100)*20
            return salario
