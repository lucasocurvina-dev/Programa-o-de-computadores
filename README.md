🏫 Sistema de Gerenciamento Escolar - Intelectos

Este é um script em Python desenvolvido para o gerenciamento de notas e frequência de alunos do Ensino Fundamental 
1. O sistema calcula médias bimestrais, valida critérios de aprovação com base na frequência e notas, e gera um relatório final detalhado.

---

 🚀 Funcionalidades

 Cadastro de Alunos e Disciplinas: Permite registrar o nome do aluno e a matéria correspondente.
  Cálculo de Frequência: Recebe a quantidade de presenças (baseada em 200 dias letivos) e calcula a porcentagem final.
  Cálculo de Notas por Bimestre: Valida e soma as notas de 4 bimestres diferentes, divididas por categorias:
  * Notebook/Caderno (Máx: 2.5)
  * Teste (Máx: 1.5)
  * Trabalho em Grupo (Máx: 1.0)
  * Prova (Máx: 5.0)
  Definição Automática de Situação:**
   🔴 **Reprovado por falta:** Frequência abaixo de 75%.
   🟢 **Aprovado !!:** Média final igual ou superior a 6.0 (e frequência maior ou igual a 75%).
   🟡 **Recuperação !!:** Média final abaixo de 6.0 (e frequência maior ou igual a 75%).
  Relatório Final:** Exibe um resumo organizado de todos os cadastros realizados antes de encerrar o programa.

---

🛠️ Pré-requisitos

Antes de executar o projeto, você precisará ter instalado em sua máquina:

 [Python 3.x](https://www.python.org/)

---

💻 Como Executar

1. Faça o clone deste repositório ou baixe o arquivo `arquivo_1.py`.
2. Abra o terminal ou prompt de comando na pasta onde o arquivo está salvo.
3. Execute o seguinte comando:

```bash
python arquivo_1.py

