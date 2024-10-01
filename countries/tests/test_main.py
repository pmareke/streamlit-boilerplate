from streamlit.testing.v1 import AppTest


def test_hello_world():
    at = AppTest.from_file("main.py").run()

    assert at.title[0].value == "Hello, world!"
