import streamlit as st


# For permanent state!
def keep(key):
    def callback():
        st.session_state[key] = st.session_state[f"_{key}"]

    return callback


# WARN: this has access to all your disk drive, careful
st.title("Configuraton")
workdir = st.text_input(
    label="workdir",
    value=st.session_state.get("config-workdir"),
    placeholder="workdir",
    label_visibility="collapsed",
    key="_config-workdir",
    on_change=keep("config-workdir"),
)
