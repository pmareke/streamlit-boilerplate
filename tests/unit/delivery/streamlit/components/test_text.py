from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTextComponent:
    def test_text(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/text.py")

        at = app.run()

        expect(at.text[0].value).to(equal("any-text"))
