from streamlit.testing.v1 import AppTest


class TestTitleComponent:
    def test_title(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/title.py")

        at = app.run()

        assert at.title[0].value == "any-title"
