from streamlit.testing.v1 import AppTest


class TestButtonComponent:
    def test_button(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/button.py")

        at = app.run()

        assert at.button[0].label == "any-button"
