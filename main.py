import streamlit as st
import time

def pomodoro_timer(minutes):
    """Runs a Pomodoro timer for the specified number of minutes."""
    timer_placeholder = st.empty()
    st.write(f"**Temporizador Pomodoro: {minutes} minutos**")
    for remaining in range(minutes * 60, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"**⏳ {mins:02d}:{secs:02d}**")
        time.sleep(1)
    #aplicar audio de alarme
    #st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    timer_placeholder.empty()  # Clear the timer display
    st.write("**Trabalho Concluído!**")

# Interface do Streamlit
st.title("Pomodoro App")

# Configuração do temporizador
pomodoro_minutes = st.slider("Escolha a duração do Pomodoro (minutos)", 1, 60, 25, 1)

# Botão para iniciar o Pomodoro
if st.button("Iniciar Pomodoro"):
    pomodoro_timer(pomodoro_minutes)
