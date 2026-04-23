import streamlit as st

# Configuração básica
st.set_page_config(page_title="Minhas Tarefas", page_icon="📝")

st.title("📝 Gestão de Tarefas")

# 1. LINHA DE BUSCA E FILTRO (Usando Colunas)
# Criamos duas colunas: a primeira é 3x maior que a segunda
col1, col2 = st.columns([3, 1]) 

with col1:
    search = st.text_input("Buscar tarefa...", placeholder="Ex: Estudar Pandas")

with col2:
    filtro = st.selectbox("Status", ["Todas", "Pendente", "Concluída"])

st.markdown("---")

# 2. LISTAGEM DE TAREFAS (Usando Expanders)
st.subheader("Suas Atividades")

# Tarefa 1
with st.expander("📌 Tarefa 09: Configuração de Layout (Clique para ver)", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Disciplina:** Innovation Lab")
        st.write("**Prazo:** 20/02/2026")
    with col_b:
        st.checkbox("Marcar como Concluída", value=True, key="t1")
    st.info("Status: Layout concluído com sucesso.")

# Tarefa 2 (Exemplo de tarefa pendente)
with st.expander("📌 Tarefa 10: Conexão com API", expanded=False):
    st.write("**Disciplina:** Desenvolvimento Web")
    st.write("**Prazo:** 05/03/2026")
    st.checkbox("Marcar como Concluída", value=False, key="t2")
    st.warning("Aguardando instruções da próxima aula.")

# 3. BOTÃO PARA NOVA TAREFA
st.divider()
if st.button("➕ Adicionar Nova Tarefa"):
    st.toast("Funcionalidade em desenvolvimento!")