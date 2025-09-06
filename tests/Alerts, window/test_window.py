import pytest
from url.url import URL
url = URL()


class TestWindowPage:


    @pytest.mark.window_page
    def test_new_tab(self, window_page):
        window_page.open(url.Window_Page)
        window_page.click_to_tab_button()
        opened_new_tab = window_page.check_new_tab()
        assert opened_new_tab

    @pytest.mark.window_page
    def test_new_window(self, window_page):
        window_page.open(url.Window_Page)
        window_page.click_to_window_button()
        opened_new_window = window_page.check_new_window()
        assert opened_new_window