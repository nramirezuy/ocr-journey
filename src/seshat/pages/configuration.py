import os
import tomllib

import streamlit as st


def load_config():
    HOME = os.getenv("HOME")
    with open(f"{HOME}/.config/seshat/config.toml", "rb") as file:
        return tomllib.load(file)


def disabled_text_input(name, value):
    st.text_input(
        label=name,
        disabled=True,
        value=value,
        placeholder=name,
    )
    st.session_state[f"config-{name}"] = value


st.title("Configuraton")

config = load_config()
profile = st.selectbox("Choose a profile", config["profiles"].keys())


for name in ("workdir", ):
    disabled_text_input(name, config["profiles"][profile][name])
