import streamlit as st


class Title:
    def render(self) -> None:
        st.title("Hello, world!")


if __name__ == "__main__":
    title = Title()
    title.render()
