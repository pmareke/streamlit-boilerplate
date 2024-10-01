from streamlit.testing.v1 import AppTest


class TestCountriesListComponent:
    def test_countries_list(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/countries_list.py")

        at = app.run()
        at.button[0].click().run()

        assert at.text[0].value == "Country: Argentina, Capital: Buenos Aires"
