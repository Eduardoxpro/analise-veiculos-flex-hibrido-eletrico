# Análise Comparativa de Veículos 2025 - Eduardo Rodrigues dos Santos
# Flex × Híbrido × Elétrico - Custo e Emissão
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração geral dos gráficos (fica bonito no GitHub)
plt.rcParams['font.size'] = 12
sns.set_style("whitegrid")

# Lê os dados
df = pd.read_csv("dados_veiculos.csv")

# Cálculo do custo por km
df["Custo_por_km_R$"] = (df["Preco_Combustivel_kWh"] / df["Consumo_Cidade"]).round(3)

# === GRÁFICO 1: CUSTO POR KM ===
plt.figure(figsize=(12, 8))
sns.barplot(data=df.sort_values("Custo_por_km_R$"),
            y="Modelo", x="Custo_por_km_R$", hue="Tipo", palette="Set2")
plt.title("Custo por km rodado - Salvador/BA - Novembro 2025", fontsize=18, pad=20)
plt.xlabel("Custo (R$ por km)", fontsize=14)
plt.ylabel("")
plt.legend(title="Tipo de motorização")
plt.tight_layout()
plt.savefig("custo_por_km.png", dpi=300, bbox_inches='tight')
plt.show()

# === GRÁFICO 2: EMISSÃO DE CO₂ (g/km) ===
plt.figure(figsize=(12, 8))
sns.barplot(data=df.sort_values("CO2_medio_g_km", ascending=False),
            y="Modelo", x="CO2_medio_g_km", hue="Tipo", palette="Reds_d")
plt.title("Emissão de CO₂ por km rodado (g/km) - 2025", fontsize=18, pad=20)
plt.xlabel("CO₂ emitido (gramas por km)", fontsize=14)
plt.ylabel("")
plt.legend(title="Tipo de motorização")
plt.tight_layout()
plt.savefig("emissao_co2_por_km.png", dpi=300, bbox_inches='tight')
plt.show()

# Salva resultado completo em Excel
df.to_excel("Resultado_Final_Veiculos_2025.xlsx", index=False)

# Exibe no terminal o ranking duplo
print("\n=== RANKING FINAL ===")
print(df[["Modelo", "Tipo", "Custo_por_km_R$", "CO2_medio_g_km"]]
      .sort_values("Custo_por_km_R$")
      .to_string(index=False))

print("\nProjeto concluído com sucesso!")
print("Imagens salvas: custo_por_km.png + emissao_co2_por_km.png")
print("Planilha salva: Resultado_Final_Veiculos_2025.xlsx")