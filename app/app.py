import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Configurar conexão com o banco de dados
DB_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Configurar a página
st.set_page_config(
    page_title="Dashboard de Commodities",
    page_icon="📈",
    layout="wide"
)

# Título do dashboard
st.title("📊 Dashboard de Commodities")

# Função para carregar os dados
@st.cache_data
def load_data():
    engine = create_engine(DB_URI)
    query = """
    SELECT "Close", ticker
    FROM public.commodities
    ORDER BY "Close" DESC
    """
    df = pd.read_sql(query, engine)
    return df

# Carregar os dados
try:
    df = load_data()
    
    # Sidebar com filtros
    st.sidebar.header("Filtros")
    
    # Filtro de commodity
    selected_commodity = st.sidebar.multiselect(
        "Selecione as Commodities:",
        options=df['ticker'].unique(),
        default=df['ticker'].unique()
    )
    
    # Filtrar dados
    filtered_df = df[df['ticker'].isin(selected_commodity)]
    
    # Layout em duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de linha para preços
        fig_line = px.line(
            filtered_df,
            y='Close',
            color='ticker',
            title='Evolução dos Preços das Commodities'
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
    with col2:
        # Gráfico de variação percentual
        df_pct = filtered_df.pivot(columns='ticker', values='Close').pct_change()
        fig_pct = px.box(
            df_pct.melt(),
            x='ticker',
            y='value',
            title='Distribuição da Variação Diária (%)'
        )
        st.plotly_chart(fig_pct, use_container_width=True)
    
    # Métricas principais
    st.header("Métricas Principais")
    metric_cols = st.columns(len(selected_commodity))
    
    for i, commodity in enumerate(selected_commodity):
        commodity_data = filtered_df[filtered_df['ticker'] == commodity]
        last_price = commodity_data['Close'].iloc[0]
        price_change = (commodity_data['Close'].iloc[0] - commodity_data['Close'].iloc[-1]) / commodity_data['Close'].iloc[-1] * 100
        
        with metric_cols[i]:
            st.metric(
                label=f"{commodity}",
                value=f"${last_price:.2f}",
                delta=f"{price_change:.2f}%"
            )
    
    # Tabela de dados
    st.header("Dados Detalhados")
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Erro ao carregar os dados: {str(e)}")
    st.info("Verifique se o banco de dados está acessível e se as credenciais estão corretas.")

# Footer
st.markdown("---")
st.markdown("Desenvolvido com ❤️ usando Streamlit")
