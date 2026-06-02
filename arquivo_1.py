import os

cadastros = []

def calcular_frequencia():
    while True:
        presenca = int(input("Digite a quantidade de presença (0 a 200): "))

        if presenca < 0 or presenca > 200:
            print("Quantidade de presença inválida.")
        else:
            porcentagem_presenca = (presenca / 200) * 100
            return porcentagem_presenca

def calcular_notas():
    notas = []

    for i in range(1, 5):
        print(f"\n------------ {i}º BIMESTRE ------------")

        while True:
            caderno = float(input("Digite a nota do caderno(max 2.5): "))

            if caderno < 0 or caderno > 2.5:
                print("Nota inválida.")
            else:
                break

        while True:
            teste = float(input("Digite a nota do teste(max 1.5): "))

            if teste < 0 or teste > 1.5:
                print("Nota inválida.")
            else:
                break

        while True:
            trabalho = float(input("Digite a nota do trabalho em grupo(max 1.0): "))

            if trabalho < 0 or trabalho > 1.0:
                print("Nota inválida.")
            else:
                break

        while True:
            prova = float(input("Digite a nota da prova(max 5.0): "))

            if prova < 0 or prova > 5:
                print("Nota inválida.")
            else:
                break

        media_bimestre = caderno + teste + trabalho + prova

        print(f"\nMédia do {i}º bimestre: {media_bimestre:.2f}")

        notas.append(media_bimestre)

    media_final = sum(notas) / len(notas)

    return notas, media_final


def cadastrar_aluno():
    print("\n---------------- Intelectos - Ensino Fundamental 1 ----------------")

    nome = input("Digite o nome do aluno: ")
    disciplina = input("Digite a disciplina (matemática, português, ciências, artes, história): ")

    porcentagem_presenca = calcular_frequencia()

    notas, media = calcular_notas()

    if porcentagem_presenca < 75:
        situacao = "Reprovado por falta"

    elif media >= 6:
        situacao = "Aprovado !!"

    else:
        situacao = "Recuperação !!"

    aluno = {
        "nome": nome,
        "disciplina": disciplina,
        "porcentagem_presenca": porcentagem_presenca,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    return aluno

def relatorio_final(cadastros):
    print("\n========== Resultado Final do Aluno ==========")

    for aluno in cadastros:
        print(f"\nNome: {aluno['nome']}")
        print(f"Disciplina: {aluno['disciplina']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média Final: {aluno['media']:.2f}")
        print(f"Porcentagem de Presença: {aluno['porcentagem_presenca']:.1f}%")
        print(f"Situação: {aluno['situacao']}\n\n\n")

while True:
    os.system("cls")
    aluno = cadastrar_aluno()
    cadastros.append(aluno)
    continuar = input("\nDeseja cadastrar outra matéria? (s/n): ").lower()

    if continuar != "s":
        break

relatorio_final(cadastros)