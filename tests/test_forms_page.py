from url.url import URL
import pytest
url = URL()


@pytest.mark.forms_page
def test_forms_field(forms_page):
    forms_page.open(URL.Practice_Form_Page)
    e = forms_page.zapolnenie_formi()
    entered_result = e[0] + " " + e[1] + e[2] + e[3] + e[4]
    g = forms_page.data_in_opened_window_form()
    get_result = g[0] + g[1] + g[3] + g[8]
    assert entered_result in get_result