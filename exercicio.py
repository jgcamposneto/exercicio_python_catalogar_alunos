class Aluno:
    def __init__(self,nome,curso) :
        self.nome = nome
        self.curso = curso

lista_estados = ['RS','SC','SP','RJ','MG']
lista_cursos = ['ADS','RDS','PMM','SPI']

dic_estudantes = {}

def menuPrincipal():
    while True:
        escolha = input(
        """
        0- Finalizar o Programa
        1- Catalogar Aluno
        2- Imprimir Alunos por Estado
        3- Imprimir Alunos por Curso
        4- Localizar um aluno por nome
        Escolha:
        """
        )

        if escolha == '0': break
        elif escolha == '1': catalogar_aluno()
        elif escolha == '2': imprimir_alunos_por_estado()
        elif escolha == '3': imprimir_alunos_por_curso()
        elif escolha == '4': localizar_aluno_por_nome()
        else:
            input("\n> Escolha inválida. [Enter]")

def mostrar_estados_cadastrados():
    print("\nEstados cadastrados")
    for estado in lista_estados:
        print(estado)

def catalogar_aluno():
    mostrar_estados_cadastrados()
    nome_estado = input("Informe o nome do Estado:")
    while nome_estado not in lista_estados:
        nome_estado = input("Estado Inválido. Informe o nome do Estado:")
    nome_aluno = input("Informe o nome do Aluno:")
    while nome_aluno.isdigit():
        nome_aluno = input("Nome inválido. Informe o nome do Aluno:")
    mostrar_cursos_cadastrados()
    nome_curso = input("Informe o nome do Curso:")
    while nome_curso not in lista_cursos:
        nome_curso = input("Curso Inválido. Informe o nome do Curso:")
    aluno = Aluno(nome_aluno, nome_curso)
    lista_estudantes = dic_estudantes.get(nome_estado,[])
    lista_estudantes.append(aluno)
    dic_estudantes[nome_estado] = lista_estudantes

def imprimir_alunos_por_estado():
    mostrar_estados_cadastrados()
    nome_estado = input("Informe o nome do Estado:")
    while nome_estado not in lista_estados:
        nome_estado = input("Estado Inválido. Informe o nome do Estado:")
    lista_estudantes = dic_estudantes.get(nome_estado,[])
    for estudante in lista_estudantes:
        print(f'Aluno: {estudante.nome}, Curso: {estudante.curso}')

def mostrar_cursos_cadastrados():
    print("Cursos cadastrados")
    for curso in lista_cursos:
        print(curso)

def imprimir_alunos_por_curso():    
    mostrar_cursos_cadastrados()
    nome_curso = input("Informe o nome do Curso:")
    while nome_curso not in lista_cursos:
        nome_curso = input("Curso Inválido. Informe o nome do Curso:")
    for estado, lista_alunos in dic_estudantes.items():
        for aluno in lista_alunos:
            if aluno.curso == nome_curso:
                print(f'Aluno: {aluno.nome}, Curso: {aluno.curso}')

def localizar_aluno_por_nome():
    nome_aluno = input("Informe o nome do Aluno:")
    for estado, lista_alunos in dic_estudantes.items():
        for aluno in lista_alunos:
            if aluno.nome == nome_aluno:
                print(f'Estado: {estado}, Curso: {aluno.curso}')        

if __name__ == "__main__":
    menuPrincipal()