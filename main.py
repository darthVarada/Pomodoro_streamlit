import streamlit as st
import time

def pomodoro_timer(minutes: int) -> None:
    """
    Runs a Pomodoro timer for the specified number of minutes.

    Args:
        minutes (int): The duration of the Pomodoro timer in minutes.

    This function displays a countdown timer on the Streamlit interface for
    the specified number of minutes. After the timer reaches zero, a message
    is displayed indicating that the work session has ended.

    TODO:
        - Add audio alert when the timer reaches zero.
        - Add a reset button to reset the timer.
        - Add a stop button to stop the timer.
        - Add a restart button to restart the timer.
        - Add a settings button to configure the timer.
        - Add a pause/resume button to pause and resume the timer.
    """
    # Create an empty placeholder for the timer display
    timer_placeholder = st.empty()

    # Display the Pomodoro timer with its duration
    st.write(f"**Temporizador Pomodoro: {minutes} minutos**")

    # Run the countdown timer
    for remaining in range(minutes * 60, 0, -1):
        # Calculate the remaining minutes and seconds
        mins, secs = divmod(remaining, 60)

        # Display the remaining time
        timer_placeholder.markdown(f"**⏳ {mins:02d}:{secs:02d}**")

        # Pause the timer for 1 second
        time.sleep(1)

    # Clear the timer display
    timer_placeholder.empty()

    # Display a message indicating the end of the work session
    st.write("**Trabalho Concluído!**")

# Interface do Streamlit
st.title("Pomodoro App")

# Configuração do temporizador
pomodoro_minutes = st.slider("Escolha a duração do Pomodoro (minutos)", 1, 60, 25, 1)

# Botão para iniciar o Pomodoro
if st.button("Iniciar Pomodoro"):
    pomodoro_timer(pomodoro_minutes)
