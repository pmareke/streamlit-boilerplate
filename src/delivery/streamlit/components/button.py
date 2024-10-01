import streamlit as st


class Button:
    def render(self, label: str) -> None:
        st.button(label)


if __name__ == "__main__":
    button = Button()
    button.render("any-button")
