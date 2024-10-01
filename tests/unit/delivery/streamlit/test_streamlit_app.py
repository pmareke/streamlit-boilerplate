from streamlit.testing.v1 import AppTest


class TestStreamlitApp:
    def test_hello_world(self) -> None:
        at = AppTest.from_file("src/delivery/streamlit/app.py").run()

        assert at.title[0].value == "Hello, world!"
