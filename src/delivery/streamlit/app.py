from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.text import Text

header = Header()
button = Button()
text = Text()

header.render("Countries")
button.render("Load one country")
text.render("Made by @pmareke")
