import base64
import glob
import math

import streamlit as st
from st_clickable_images import clickable_images


def load_image(path):
    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"


def gallery(images):
    st.title("Gallery")
    if not images:
        st.warning("No images found")

    page = st.session_state.get("gallery-page", 1)
    if images:
        pages = math.ceil(len(images) / 9.0)

        if pages > 1:
            navigation = st.columns(spec=[0.1, 0.8, 0.1])

            with navigation[0]:
                previous = st.button(label="<")
                if previous:
                    page = st.session_state["gallery-page"] - 1

            with navigation[2]:
                next_ = st.button(label="\\>")
                if next_:
                    page = st.session_state["gallery-page"] + 1

            with navigation[1]:
                page = st.slider(
                    label="",
                    min_value=1,
                    max_value=pages,
                    value=max(1, min(page, pages)),
                    label_visibility="collapsed",
                    key="gallery-page",
                )

        min_image = max(0, page - 1)
        max_image = min(page + 9, len(images))
        selected_images = images[min_image:max_image]
        loaded_images = [load_image(path) for path in selected_images]
        clicked = clickable_images(
            loaded_images,
            titles=[f"Image #{str(i)}" for i in range(5)],
            div_style={
                "display": "flex",
                "justify-content": "center",
                "flex-wrap": "wrap",
            },
            img_style={
                "margin": "5px",
                "object-fit": "contain",
                "max-height": "200px",
                "max-width": "200px",
                "height": "auto",
                "width": "auto",
            },
            key="explorer",
        )

        st.markdown(
            f"Image #{clicked} clicked" if clicked > -1 else "No image clicked"
        )
        return clicked


workdir = st.session_state.get("config-workdir")
images = glob.glob(f"{workdir}/*.jpeg")
clicked = gallery(images)
