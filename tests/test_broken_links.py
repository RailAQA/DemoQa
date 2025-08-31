import pytest
from url.url import URL
url = URL()


@pytest.mark.broken_links_page
def test_check_valid_image(broken_links_page):
    broken_links_page.open(url.Broken_Links_Page)
    broken_links_page.scroll_to_valid_image()
    valid_image_is_visible = broken_links_page.check_valid_image()
    assert valid_image_is_visible

@pytest.mark.xfail
@pytest.mark.broken_links_page
def test_check_broken_image(broken_links_page):
    broken_links_page.open(url.Broken_Links_Page)
    broken_links_page.scroll_to_broken_image()
    broken_image_is_not_visible = broken_links_page.check_broken_image()
    assert broken_image_is_not_visible

@pytest.mark.broken_links_page
def test_click_to_valid_link(broken_links_page):
    broken_links_page.open(url.Broken_Links_Page)
    broken_links_page.scroll_to_valid_link_button()
    broken_links_page.click_to_valid_link()
    opened_homepage = broken_links_page.opened_url_is(url.HomePage)
    assert opened_homepage

@pytest.mark.broken_links_page
def test_click_to_broken_link(broken_links_page):
    broken_links_page.open(url.Broken_Links_Page)
    broken_links_page.scroll_to_broken_link_button()
    broken_links_page.click_to_broken_link()
    opened_url_not_homepage = broken_links_page.opened_url_is_not(url.HomePage)
    assert opened_url_not_homepage