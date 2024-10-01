import streamlit as st


class Title:
    def render(self, message: str) -> None:
        st.title(message)


if __name__ == "__main__":
    title = Title()
    title.render("Hello, world!")
