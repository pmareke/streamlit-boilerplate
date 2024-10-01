from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestCountriesListComponent:
    def test_countries_list(self) -> None:
        app = AppTest.from_file("src/delivery/streamlit/components/countries_list.py")

        at = app.run()
        at.button[0].click().run()

        expect(at.text[0].value).to(equal("Country: Argentina, Capital: Buenos Aires"))
