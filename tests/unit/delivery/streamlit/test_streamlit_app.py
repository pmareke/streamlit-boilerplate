from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestStreamlitApp:
    def test_hello_world(self) -> None:
        def create_app() -> None:
            from src.delivery.streamlit.app import App

            app = App()
            app.render()

        app = AppTest.from_function(create_app)

        at = app.run()
        at.button[0].click().run()

        expect(at.header[0].value).to(equal("Countries"))
        expect(at.button[0].label).to(equal("Load Countries"))
        expect(at.text[0].value).to(equal("Country: Argentina, Capital: Buenos Aires"))
        expect(at.text[1].value).to(equal("Made by @pmareke"))
