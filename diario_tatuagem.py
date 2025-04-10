def mostrar_menu():
    print("\n" + "="*40)
    print(" MENU DO DIÁRIO DE TATUAGEM")
    print("="*40)
    print("1 - Registrar nova sessão")
    print("2 - Ver histórico de sessões")
    print("3 - Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        break  # Continua o código normalmente
    elif escolha == "2":
        print("\n🗂️  Histórico de Sessões:\n")
        try:
            with open("historico_sessoes.txt", "r", encoding="utf-8") as h:
                print(h.read())
        except FileNotFoundError:
            print("Ainda não há sessões registradas.")
    elif escolha == "3":
        print("Saindo... Até a próxima sessão!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")


# Base de preços dos materiais (exceto agulhas, que agora são livres)
precos_materiais = {
    "tinta_preta_ml": 1.20,
    "luva": 0.50,
    "filme_cm": 0.10,
    "papel_toalha": 0.05
}

# Informações da sessão
cliente = input("Nome do cliente: ")
data = input("Data da sessão (dd/mm/aaaa): ")
estilo = input("Estilo da tatuagem: ")
parte_corpo = input("Parte do corpo tatuada: ")
referencia = input("Referência ou inspiração usada: ")
tintas = input("Tintas usadas: ")
valor = input("Valor cobrado (R$): ")
duracao = input("Duração da sessão: ")
acertos = input("O que deu certo na sessão? ")
melhorias = input("O que pode melhorar? ")
dificuldades = input("Quais foram as dificuldades encontradas? ")

# 🪡 Agulhas usadas (agora você escolhe tipo e preço!)
custo_agulhas = 0
qtd_tipos_agulha = int(input("Quantos tipos diferentes de agulhas foram usados? "))

for i in range(qtd_tipos_agulha):
    tipo = input(f"Tipo da agulha {i+1} (ex: 3RL, 7M, 9RS): ")
    preco = float(input(f"Preço da agulha {tipo} (R$): "))
    qtd = int(input(f"Quantidade usada da agulha {tipo}: "))
    custo_agulhas += preco * qtd

# 📦 Outros materiais
qtd_tinta_ml = float(input("Quantos ml de tinta preta usados? "))
qtd_luvas = int(input("Quantos pares de luvas usados? "))
qtd_filme_cm = float(input("Quantos cm de plástico filme usados? "))
qtd_papel_toalha = int(input("Quantas folhas de papel toalha usadas? "))

# 🧮 Cálculo de custo total
custo_total = (
    custo_agulhas +
    qtd_tinta_ml * precos_materiais["tinta_preta_ml"] +
    qtd_luvas * precos_materiais["luva"] +
    qtd_filme_cm * precos_materiais["filme_cm"] +
    qtd_papel_toalha * precos_materiais["papel_toalha"]
)

relatorio = f"""
========================================
           RELATÓRIO DA SESSÃO
========================================

Cliente: {cliente}
Data: {data}
Estilo: {estilo}
Parte do corpo: {parte_corpo}
Referência: {referencia}
Tintas: {tintas}
Valor cobrado: R${valor}
Duração da sessão: {duracao}
----------------------------------------
O que deu certo:
{acertos}

O que pode melhorar:
{melhorias}

Dificuldades encontradas:
{dificuldades}
----------------------------------------
Custo total dos materiais: R${custo_total:.2f}
========================================
"""
import calendar

# Extrair mês e ano da data (formato dd/mm/aaaa)
dia, mes, ano = data.split("/")
nome_mes = calendar.month_name[int(mes)].lower()
nome_arquivo = f"sessoes_{nome_mes}_{ano}.txt"

# Formatar texto da sessão
relatorio = f"""
Cliente: {cliente}
Data: {data}
Estilo: {estilo}
Parte do corpo: {parte_corpo}
Referência: {referencia}
Tintas: {tintas}
Valor cobrado: R${valor}
Duração: {duracao}
O que deu certo: {acertos}
O que pode melhorar: {melhorias}
Dificuldades: {dificuldades}
Custo total dos materiais: R${custo_total:.2f}
------------------------------
"""

# Salvar no arquivo do mês
with open(nome_arquivo, "a", encoding="utf-8") as f:
    f.write(relatorio)

# Mostra no terminal
print(relatorio)

# Salva no histórico
with open("historico_sessoes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(relatorio + "\n\n")

# Salvando o relatório em um arquivo .txt
with open(f"relatorio_{cliente.replace(' ', '_')}.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("--- RELATÓRIO DA SESSÃO ---\n")
    arquivo.write(f"Cliente: {cliente}\n")
    arquivo.write(f"Data: {data}\n")
    arquivo.write(f"Estilo: {estilo}\n")
    arquivo.write(f"Parte do corpo: {parte_corpo}\n")
    arquivo.write(f"Referência: {referencia}\n")
    arquivo.write(f"Tintas: {tintas}\n")
    arquivo.write(f"Valor cobrado: R${valor}\n")
    arquivo.write(f"Duração: {duracao}\n")
    arquivo.write(f"O que deu certo: {acertos}\n")
    arquivo.write(f"O que pode melhorar: {melhorias}\n")
    arquivo.write(f"Dificuldades: {dificuldades}\n")
    arquivo.write(f"→ Custo total dos materiais: R${custo_total:.2f}\n")

print(f"\n✅ Relatório salvo como relatorio_{cliente.replace(' ', '_')}.txt com sucesso!")

def balanco_mensal():
    import os

    mes = input("Digite o mês (em letras minúsculas, ex: abril): ")
    ano = input("Digite o ano (ex: 2025): ")
    nome_arquivo = f"sessoes_{mes}_{ano}.txt"

    if not os.path.exists(nome_arquivo):
        print("Arquivo de sessões não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    # Vamos procurar todas as linhas que começam com "→ Custo total dos materiais:"
    linhas = conteudo.split("\n")
    total_sessoes = 0
    total_gasto = 0
    total_ganho = 0

    for linha in linhas:
        if linha.startswith("→ Custo total dos materiais: R$"):
            valor = float(linha.split("R$")[1])
            total_gasto += valor
            total_sessoes += 1
        elif linha.startswith("Valor cobrado: R$"):
            valor = float(linha.split("R$")[1])
            total_ganho += valor

    print("\n--- BALANÇO MENSAL ---")
    print(f"Mês: {mes.capitalize()} de {ano}")
    print(f"Sessões registradas: {total_sessoes}")
    print(f"Total gasto com materiais: R${total_gasto:.2f}")
    print(f"Total recebido com tatuagens: R${total_ganho:.2f}")
    print(f"Lucro estimado: R${(total_ganho - total_gasto):.2f}")
# Teste da função de balanço mensal
resposta = input("Deseja visualizar o balanço mensal? (s/n): ")
if resposta.lower() == "s":
    balanco_mensal()
import os
from datetime import datetime

# Extrair mês e ano da data informada
data_convertida = datetime.strptime(data, "%d/%m/%Y")
nome_arquivo = f"sessoes_{data_convertida.strftime('%B_%Y')}.txt".lower()

# Criar o texto do relatório da sessão
relatorio = (
    f"\n--- RELATÓRIO DA SESSÃO ---\n"
    f"Cliente: {cliente}\n"
    f"Data: {data}\n"
    f"Estilo: {estilo}\n"
    f"Parte do corpo: {parte_corpo}\n"
    f"Referência: {referencia}\n"
    f"Tintas: {tintas}\n"
    f"Valor cobrado: R${valor}\n"
    f"Duração: {duracao}\n"
    f"O que deu certo: {acertos}\n"
    f"O que pode melhorar: {melhorias}\n"
    f"Dificuldades: {dificuldades}\n"
    f"Custo total dos materiais: R${custo_total:.2f}\n"
)

# Salvar o relatório no arquivo do mês
with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write(relatorio)
    arquivo.write("\n" + "-" * 40 + "\n")

print(f"Relatório salvo no arquivo: {nome_arquivo}")
def balanco_mensal():
    from datetime import datetime

    mes_input = input("Digite o mês (ex: abril): ").lower()
    ano_input = input("Digite o ano (ex: 2025): ")

    nome_arquivo = f"sessoes_{mes_input}_{ano_input}.txt"

    if not os.path.exists(nome_arquivo):
        print("Arquivo do mês não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    sessoes = conteudo.split("--- RELATÓRIO DA SESSÃO ---")
    total_sessoes = len([s for s in sessoes if s.strip() != ""])

    import re
    valores = re.findall(r"Valor cobrado: R\$(\d+(?:\.\d+)?)", conteudo)
    custos = re.findall(r"Custo total dos materiais: R\$(\d+(?:\.\d+)?)", conteudo)

    total_valores = sum(float(v) for v in valores)
    total_custos = sum(float(c) for c in custos)
    lucro = total_valores - total_custos

    print("\n--- BALANÇO DO MÊS ---")
    print(f"Sessões realizadas: {total_sessoes}")
    print(f"Total arrecadado: R${total_valores:.2f}")
    print(f"Total de custos: R${total_custos:.2f}")
    print(f"Lucro estimado: R${lucro:.2f}")
# Descomente se quiser gerar o balanço
# balanco_mensal()
