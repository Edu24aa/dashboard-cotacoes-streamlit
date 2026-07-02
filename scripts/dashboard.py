import streamlit as st
from funcoes import buscar_cotacoes

# ==========================
# CONFIGURAÇÃO DA PÁGINA
# ==========================

st.set_page_config(
    page_title="Dashboard de Cotações",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Dashboard de Cotações em Tempo Real")

st.write("Consulta automática utilizando API pública.")

# ==========================
# BUSCA DOS DADOS
# ==========================

df = buscar_cotacoes()

# ==========================
# CARDS
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💵 Dólar",
        f"R$ {df.iloc[0]['Compra']:.2f}"
    )

with col2:
    st.metric(
        "💶 Euro",
        f"R$ {df.iloc[1]['Compra']:.2f}"
    )

with col3:
    st.metric(
        "₿ Bitcoin",
        f"R$ {df.iloc[2]['Compra']:,.2f}"
    )

st.divider()

# ==========================
# TABELA
# ==========================

st.subheader("Tabela de Cotações")

st.dataframe(
    df,
    use_container_width=True
)

# ==========================
# GRÁFICO
# ==========================

st.subheader("Comparativo das Cotações")

st.bar_chart(
    df.set_index("Moeda")["Compra"]
)