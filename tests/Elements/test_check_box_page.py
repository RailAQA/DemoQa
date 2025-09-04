from url.url import URL
import pytest
url = URL()


@pytest.mark.check_box_page
def test_open_list(check_box_page):
    check_box_page.open(url.Check_Box_Page)
    check_box_page.scroll_to_checkbox_block()
    check_box_page.open_list()
    list_is_opened = check_box_page.check_list_is_opened()
    assert list_is_opened

@pytest.mark.check_box_page
def test_check_box_click(check_box_page):
    check_box_page.open(url.Check_Box_Page)
    check_box_page.scroll_to_checkbox_block()
    check_box_page.open_list()
    check_box_page.click_to_check_box()
    text_is_correct = check_box_page.check_result()
    assert text_is_correct