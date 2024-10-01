from streamlit.testing.v1 import AppTest


class TestStreamlitApp:
    def test_hello_world(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/app.py")

        at = app.run()

        assert at.header[0].value == "Countries"
        assert at.button[0].label == "Load one country"
        assert at.text[0].value == "Made by @pmareke"
