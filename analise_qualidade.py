
import pandas as pd

# Carregar os dados dos testes
df = pd.read_csv("testes_software.csv")

# Indicadores gerais
total_testes = len(df)
aprovados = (df["resultado"] == "Aprovado").sum()
reprovados = (df["resultado"] == "Reprovado").sum()
total_defeitos = df["defeitos"].sum()
taxa_aprovacao = (aprovados / total_testes) * 100

# Resultados por módulo
resultados_modulo = df.groupby("modulo")["resultado"].value_counts().unstack(fill_value=0)

# Resultados por versão
resultados_versao = df.groupby("versao")["resultado"].value_counts().unstack(fill_value=0)

# Defeitos por módulo
defeitos_modulo = df.groupby("modulo")["defeitos"].sum().sort_values(ascending=False)

# Exibir resultados
print("===== ANALISE DE QUALIDADE DE SOFTWARE =====")
print(f"Total de testes: {total_testes}")
print(f"Testes aprovados: {aprovados}")
print(f"Testes reprovados: {reprovados}")
print(f"Taxa de aprovacao: {taxa_aprovacao:.2f}%")
print(f"Total de defeitos: {total_defeitos}")

print("\n===== RESULTADOS POR MODULO =====")
print(resultados_modulo)

print("\n===== RESULTADOS POR VERSAO =====")
print(resultados_versao)

print("\n===== DEFEITOS POR MODULO =====")
print(defeitos_modulo)



import matplotlib.pyplot as plt

# Grafico 1: testes aprovados e reprovados
plt.figure(figsize=(7, 5))
df["resultado"].value_counts().reindex(
    ["Aprovado", "Reprovado"], fill_value=0
).plot(kind="bar")
plt.title("Testes Aprovados x Reprovados")
plt.xlabel("Resultado")
plt.ylabel("Quantidade de testes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graficos/grafico_resultados.png")
plt.close()

# Grafico 2: defeitos por modulo
plt.figure(figsize=(7, 5))
defeitos_modulo.plot(kind="bar")
plt.title("Defeitos por Modulo")
plt.xlabel("Modulo")
plt.ylabel("Quantidade de defeitos")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graficos/grafico_defeitos_modulo.png")
plt.close()

# Grafico 3: resultados por versao
resultados_versao.plot(kind="bar", figsize=(8, 5))
plt.title("Resultados dos Testes por Versao")
plt.xlabel("Versao")
plt.ylabel("Quantidade de testes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("graficos/grafico_resultados_versao.png")
plt.close()

print("\nGraficos criados com sucesso na pasta graficos!")
