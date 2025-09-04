import pytest
from url.url import URL
url = URL()

@pytest.mark.links_page
def test_click_following_link(links_page):
    links_page.open(url.Links_Page)
    links_page.scroll_to_following_links()
    links_page.click_to_following_link()
    result_is_correct = links_page.check_data_result()
    assert result_is_correct