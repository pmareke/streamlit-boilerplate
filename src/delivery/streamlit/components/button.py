import streamlit as st

from src.domain.component import Component


class Button(Component):
    def render(self, label: str) -> bool:
        return st.button(label=label, type="primary")


if __name__ == "__main__":
    button = Button()
    button.render("any-button")
