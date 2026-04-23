import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Configuração da página (deve ser a primeira linha de código Streamlit)
st.set_page_config(page_title="EduTrack - Dashboard", layout="wide")

# Título Principal
st.title("🐧 Dashboard Interativo: Palmer Penguins")
st.markdown("---")

# 2. Carregamento dos dados
df = sns.load_dataset("penguins").dropna()

# 3. Filtros na Barra Lateral
st.sidebar.header("Configurações da Análise")
especies = st.sidebar.multiselect(
    "Selecione as Espécies:", 
    options=df['species'].unique(), 
    default=df['species'].unique()
)

ilhas = st.sidebar.multiselect(
    "Selecione as Ilhas:", 
    options=df['island'].unique(), 
    default=df['island'].unique()
)

# Aplicando os filtros nos dados
df_filtrado = df[(df['species'].isin(especies)) & (df['island'].isin(ilhas))]

# 4. Métricas em Colunas (Destaque visual)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Pinguins", len(df_filtrado))
col2.metric("Massa Média (g)", f"{df_filtrado['body_mass_g'].mean():.1f}")
col3.metric("Bico Médio (mm)", f"{df_filtrado['bill_length_mm'].mean():.1f}")
col4.metric("Nadadeira Média (mm)", f"{df_filtrado['flipper_length_mm'].mean():.1f}")

st.markdown("---")

# 5. Organização por Abas
tab_graficos, tab_dados = st.tabs(["📊 Gráficos de Análise", "📂 Dados Brutos"])

with tab_graficos:
    # Criando duas colunas para os gráficos ficarem lado a lado
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("Relação Bico vs. Massa")
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=df_filtrado, x="bill_length_mm", y="body_mass_g", hue="species", ax=ax1)
        st.pyplot(fig1)
        
    with c2:
        st.subheader("Distribuição por Espécie")
        fig2, ax2 = plt.subplots()
        sns.countplot(data=df_filtrado, x="species", palette="viridis", ax=ax2)
        st.pyplot(fig2)

with tab_dados:
    st.subheader("Tabela de Dados Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

st.sidebar.info("Use o menu acima para navegar entre Disciplinas e Tarefas!")