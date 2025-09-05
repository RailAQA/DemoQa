import pytest
from url.url import URL
url = URL()


class TestWindowPage:


    @pytest.mark.smoke
    def test_new_tab(self, window_page):
        window_page.open(url.Window_Page)
        window_page.click_to_tab_button()
        opened_new_tab = window_page.check_new_tab()
        assert opened_new_tab