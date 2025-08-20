import pytest
from url.url import URL
url = URL()


@pytest.mark.main_page
def test_open_main_page(main_page):
        main_page.open(url.HomePage)
        main_page_is_open = main_page.main_page_is_opened()
        assert main_page_is_open

@pytest.mark.main_page
def test_click_to_elements_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_elements_card()
        main_page.click_to_elements_card()
        opened_url_is_elements = main_page.opened_url_is(url.Elements_Page)
        assert opened_url_is_elements

@pytest.mark.main_page
def test_click_to_forms_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_forms_card()
        main_page.click_to_forms_card()
        opened_url_is_forms = main_page.opened_url_is(url.Forms_Page)
        assert opened_url_is_forms

@pytest.mark.main_page
def test_click_to_alerts_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_alerts_card()
        main_page.click_to_alerts_card()
        opened_url_is_alerts = main_page.opened_url_is(url.Alerts_Page)
        assert opened_url_is_alerts

@pytest.mark.main_page
def test_click_to_widgets_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_widgets_card()
        main_page.click_to_widgets_card()
        opened_url_is_widgets = main_page.opened_url_is(url.Widgets_Page)
        assert opened_url_is_widgets

@pytest.mark.main_page
def test_click_to_interactions_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_interactions_card()
        main_page.click_to_interactions_card()
        opened_url_is_interactions = main_page.opened_url_is(url.Interactions_Page)
        assert opened_url_is_interactions

@pytest.mark.main_page
def test_click_to_books_card(main_page):
        main_page.open(url.HomePage)
        main_page.scroll_to_books_card()
        main_page.click_to_books_card()
        opened_url_is_books = main_page.opened_url_is(url.Book_Page)
        assert opened_url_is_books