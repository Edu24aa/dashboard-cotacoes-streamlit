import requests
import pandas as pd
from datetime import datetime


def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
    except Exception as exc:
        print("Erro ao buscar cotações:", exc)
        return pd.DataFrame(
            columns=[
                "Data Consulta",
                "Moeda",
                "Compra",
                "Venda",
                "Máxima",
                "Mínima",
                "Variação (%)"
            ]
        )

    lista = []

    if isinstance(dados, dict):
        for moeda, info in dados.items():
            if not isinstance(info, dict):
                continue

            bid = info.get("bid")
            ask = info.get("ask")
            high = info.get("high")
            low = info.get("low")
            pct = info.get("pctChange")

            if bid is None:
                continue

            try:
                lista.append({
                    "Data Consulta": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "Moeda": moeda,
                    "Compra": float(bid),
                    "Venda": float(ask) if ask else 0,
                    "Máxima": float(high) if high else 0,
                    "Mínima": float(low) if low else 0,
                    "Variação (%)": float(pct) if pct else 0
                })
            except (ValueError, TypeError):
                continue

    return pd.DataFrame(
        lista,
        columns=[
            "Data Consulta",
            "Moeda",
            "Compra",
            "Venda",
            "Máxima",
            "Mínima",
            "Variação (%)"
        ]
    )
