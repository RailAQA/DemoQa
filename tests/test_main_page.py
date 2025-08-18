import pytest
from url.url import URL
url = URL()


def test_open_main_page(main_page):
        main_page.open(url.HomePage)
        main_page_is_open = main_page.main_page_is_opened()
        assert main_page_is_open

def test_click_to_elements_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_elements_card()
        main_page.click_to_elements_card()
        opened_url_is_elements = main_page.opened_url_is(url.Elements_Page)
        assert opened_url_is_elements