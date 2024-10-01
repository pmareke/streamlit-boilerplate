from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestButtonComponent:
    def test_button(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/button.py")

        at = app.run()

        expect(at.button[0].label).to(equal("any-button"))
