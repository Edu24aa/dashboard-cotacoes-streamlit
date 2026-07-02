from funcoes import (
    buscar_cotacoes,
    gerar_excel,
    gerar_grafico,
    gerar_insights,
)


def main():
    df = buscar_cotacoes()
    insights = gerar_insights(df)

    gerar_excel(df, insights)
    gerar_grafico(df)

    print("\n✅ Processo concluído com sucesso!")


if __name__ == "__main__":
    main()