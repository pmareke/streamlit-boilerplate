import streamlit as st


class Text:
    def render(self, message: str) -> None:
        st.text(message)


if __name__ == "__main__":
    text = Text()
    text.render("any-text")
