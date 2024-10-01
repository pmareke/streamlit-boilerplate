import streamlit as st


class Image:
    def render(self, url: str, width: int) -> None:
        st.image(image=url, width=width)


if __name__ == "__main__":
    image = Image()
    image.render(url="https://docs.streamlit.io/logo.svg", width=200)
