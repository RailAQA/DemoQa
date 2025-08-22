from url.url import URL
import pytest
url = URL()

@pytest.mark.smoke
def test_click_to_buttons(buttons_page):
    buttons_page.open(url.Buttons_Page)
    buttons_page.click_button()
    text_result_is_correct = buttons_page.check_text_result()
    assert text_result_is_correct