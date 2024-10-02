import streamlit as st

from src.domain.component import Component


class Title(Component):
    def render(self, message: str) -> None:
        st.title(message)


if __name__ == "__main__":
    title = Title()
    title.render("any-title")
