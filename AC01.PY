# Atividade Contínua 01
# Aluno 01: Insira seu nome aqui
# Aluno 02: Insira seu nome aqui


def adicionar_aluno(alunos, nome, notas):

    '''
    Essa função acrescenta os dados de um novo aluno no dicionário
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
        notas: lista com as notas de um aluno (valor)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave já exista, nenhuma alteração deve ser realizada.
    '''

def remover_aluno(alunos, nome):
    '''
    Essa função exclui os dados de um aluno do dicionário.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista, nenhuma alteração deve ser realizada
    '''



    '''
    Essa função deve retornar a lista com as notas de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar uma lista com as notas do aluno
    Observação:
        Caso a chave não exista, deve retornar uma lista vazia
    '''
def pesquisar_aluno(alunos, nome):
    dic_alunos = {'Pedro': [10.0, 9.0], 'Rafael': [9.0, 9.0], 'Thyana': [8.0, 7.0]}
    return (dic_alunos[nome])

# Programa Principal

nomealuno = input('Digite o nome do aluno:')
notas = (pesquisar_aluno, nomealuno)
print(notas)

    '''
    Essa função retorna a média de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar a média do aluno
    Observação:
        Caso a chave não exista, deve retornar zero
    '''
#def calcular_media(alunos, nome):


'''dic_alunos = {'Pedro': [10.0, 9.0], 'Rafael': [9.0, 9.0], 'Thyana': [8.0, 7.0]}
media = sum(dic_alunos['Pedro'])/len(dic_alunos['Pedro'])
print(dic_alunos['Pedro'])
print (media)'''

#Programa Principal

'''dic_notas = {}
for x in range(3):
    nome = (input("Nome:"))
    nota = float(input('Firt Nota:'))
    nota2 = float(input('Segunda Nota:'))
    dic_notas[nome] = [nota, nota2]
# print(dic_notas)
nome = input('Digite o nome do Aluno:')
media = calcular_media(dic_notas, nome)
print('Media do Aluno:', media)'''


def calcular_media_turma(alunos):
    '''
    Essa função retorna a média geral da turma
    (soma de todas as notas dividida pela quantidade de todas as notas)
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar a média da turma
    '''

dic_alunos = {'Pedro': [10.0, 9.0], 'Rafael': [9.0, 9.0], 'Thyana': [8.0, 7.0]}
for aluno in dic_alunos:
    somanotas = sum(dic_alunos[aluno])


mediageral = sum(dic_alunos[])/len(dic_alunos[])
print(dic_alunos[])
print (media)



def melhores_alunos(alunos):
    '''
    Essa função retorna o nome do aluno com a maior média
    Entrada:
        alunos: dicionario com os dados dos alunos
    Retorno:
        A função deve retornar o nome do aluno que obteve a maior média
    Observação:
        Caso a chave não exista, deve retornar uma string vazia.
    '''