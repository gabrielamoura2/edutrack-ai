import streamlit as st

st.set_page_config(page_title="EduTrack AI", layout="wide")

st.sidebar.title("Menu EduTrack")
opcao = st.sidebar.selectbox("Ir para:", ["Dashboard", "Disciplinas", "Tarefas"])

st.title("🎓 EduTrack AI")

if opcao == "Dashboard":
    st.subheader("Bem-vindo ao seu painel!")
    st.write("Configuração inicial concluída com sucesso.")
elif opcao == "Disciplinas":
    st.subheader("📚 Minhas Disciplinas")
elif opcao == "Tarefas":
    st.subheader("📝 Gestão de Tarefas")