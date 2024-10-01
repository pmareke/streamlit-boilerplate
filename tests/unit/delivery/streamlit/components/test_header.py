from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestHeaderComponent:
    def test_title(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/header.py")

        at = app.run()

        assert at.header[0].value == "any-header"
        expect(at.header[0].value).to(equal("any-header"))
