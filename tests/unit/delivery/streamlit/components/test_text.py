from streamlit.testing.v1 import AppTest


class TestTextComponent:
    def test_text(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/text.py")

        at = app.run()

        assert at.text[0].value == "any-text"
