def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

    resposta = requests.get(url)
    dados = resposta.json()

    lista = []

    for moeda, info in dados.items():

        bid = info.get("bid")
        ask = info.get("ask")
        high = info.get("high")
        low = info.get("low")
        pct = info.get("pctChange")

        # proteção contra dados inválidos
        if bid is None:
            continue

        lista.append({
            "Data Consulta": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Moeda": moeda,
            "Compra": float(bid),
            "Venda": float(ask) if ask else 0,
            "Máxima": float(high) if high else 0,
            "Mínima": float(low) if low else 0,
            "Variação (%)": float(pct) if pct else 0
        })

    return pd.DataFrame(lista)