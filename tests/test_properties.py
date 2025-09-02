import pytest
from url.url import URL
url = URL()


@pytest.mark.properties_page
def test_check_color_button(properties_page):
    properties_page.open(url.Properties_Page)
    color_button_changing_red_color = properties_page.color_button_changing_color()
    assert color_button_changing_red_color

@pytest.mark.properties_page
def test_check_button_visability(properties_page):
    properties_page.open(url.Properties_Page)
    button_is_visible_after_5_sec = properties_page.new_button_visible()
    assert button_is_visible_after_5_sec