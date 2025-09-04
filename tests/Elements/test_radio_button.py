import pytest
from url.url import URL
url = URL()

@pytest.mark.radio_button_page
def test_result_text(radio_button_page):
    radio_button_page.open(url.Radio_Button_Page)
    radio_button_page.scroll_to_radio_button()
    radio_button_page.click_to_radio_button()
    result_text_is_correct = radio_button_page.check_result_text()
    assert result_text_is_correct