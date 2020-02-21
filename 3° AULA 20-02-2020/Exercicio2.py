def calcular_media(dicionario, nome_aluno):
    if nome in dic_notas:
        media = sum(dic_notas[nome])/len(dic_notas[nome])
        return media
    else:
        return "SEM VALOR PARA MOSTRAR"

# Programa Principal:

dic_notas = {}
for x in range(3):
    nome = (input("Nome:"))
    nota = float(input('Firt Nota:'))
    nota2 = float(input('Segunda Nota:'))
    dic_notas[nome] = [nota, nota2]
# print(dic_notas)
nome = input('Digite o nome do Aluno:')
media = calcular_media(dic_notas, nome)
print('Media do Aluno:', media)
