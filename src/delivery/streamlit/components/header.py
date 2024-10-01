import streamlit as st


class Header:
    def render(self, message: str) -> None:
        st.header(message)


if __name__ == "__main__":
    header = Header()
    header.render("any-header")
