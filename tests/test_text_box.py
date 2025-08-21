import pytest
from url.url import URL
url = URL()
from time import sleep

@pytest.mark.text_box_page
def test_send_form(text_box_page):
    text_box_page.open(url.Text_Box)
    text_box_page.form_filling()
    result_is_visible = text_box_page.form_result_is_visible()
    assert result_is_visible, 'После отправки формы не отображается результат формы'

@pytest.mark.text_box_page
def test_results_sended_form(text_box_page):
    text_box_page.open(url.Text_Box)
    s = text_box_page.form_filling()
    text_box_page.scroll_to_result()
    sended_result = "Name:" + s[0] + "Email:"  + s[1] + "Current Address :" + s[2] + "Permananet Address :" + s[3]
    get_result = text_box_page.results_data()[0] + text_box_page.results_data()[1] + text_box_page.results_data()[2] + text_box_page.results_data()[3]
    print(get_result)
    print(sended_result)
    assert sended_result in get_result

@pytest.mark.text_box_page
def test_send_empty_form(text_box_page):
    text_box_page.open(url.Text_Box)
    text_box_page.scroll_to_send_button()
    text_box_page.send_empty_form()
    result_form_not_visible = text_box_page.form_result_not_visible()
    assert result_form_not_visible