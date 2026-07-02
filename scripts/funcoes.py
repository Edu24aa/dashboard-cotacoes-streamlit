import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

    resposta = requests.get(url)
    dados = resposta.json()

    lista = []

    for moeda, info in dados.items():
        lista.append({
            "Data Consulta": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Moeda": moeda,
            "Compra": float(info["bid"]),
            "Venda": float(info["ask"]),
            "Máxima": float(info["high"]),
            "Mínima": float(info["low"]),
            "Variação (%)": float(info["pctChange"])
        })

    return pd.DataFrame(lista)


def gerar_insights(df):

    maior = df.loc[df["Compra"].idxmax()]
    menor = df.loc[df["Compra"].idxmin()]

    insights = pd.DataFrame({
        "Resumo": [
            f"Consulta realizada em {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            f"A maior cotação foi {maior['Moeda']}.",
            f"A menor cotação foi {menor['Moeda']}.",
            f"Foram analisadas {len(df)} moedas."
        ]
    })

    return insights


def gerar_excel(df, insights):

    with pd.ExcelWriter(
        "relatorios/cotacoes.xlsx",
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Cotações",
            index=False
        )

        insights.to_excel(
            writer,
            sheet_name="Insights",
            index=False
        )


def gerar_grafico(df):

    plt.figure(figsize=(8,5))

    plt.bar(df["Moeda"], df["Compra"])

    plt.title("Cotação de Compra")

    plt.xlabel("Moeda")

    plt.ylabel("Valor (R$)")

    plt.tight_layout()

    plt.savefig("imagens/grafico_cotacoes.png")

    plt.close()