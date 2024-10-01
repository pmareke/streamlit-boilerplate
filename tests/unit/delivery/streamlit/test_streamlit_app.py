from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestStreamlitApp:
    def test_hello_world(self) -> None:
        def test_app() -> None:
            from src.delivery.streamlit.components.countries_list import CountriesList
            from src.delivery.streamlit.components.header import Header
            from src.delivery.streamlit.components.text import Text
            from src.infrastructure.countries.dummy_countries_client import (
                DummyCountriesClient,
            )

            header = Header()
            countries_client = DummyCountriesClient()
            countries_list = CountriesList(countries_client)
            text = Text()

            header.render("Countries")
            countries_list.render()
            text.render("Made by @pmareke")

        app = AppTest.from_function(test_app)

        at = app.run()
        at.button[0].click().run()

        expect(at.header[0].value).to(equal("Countries"))
        expect(at.button[0].label).to(equal("Load Countries"))
        expect(at.text[0].value).to(equal("Country: Argentina, Capital: Buenos Aires"))
        expect(at.text[1].value).to(equal("Made by @pmareke"))
