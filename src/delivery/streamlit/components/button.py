import streamlit as st


class Button:
    def render(self, label: str) -> bool:
        return st.button(label=label, type="primary")


if __name__ == "__main__":
    button = Button()
    button.render("any-button")
