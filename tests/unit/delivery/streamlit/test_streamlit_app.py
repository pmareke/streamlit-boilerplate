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

        assert at.header[0].value == "Countries"
        assert at.button[0].label == "Load Countries"
        assert at.text[0].value == "Country: Argentina, Capital: Buenos Aires"
        assert at.text[1].value == "Made by @pmareke"
