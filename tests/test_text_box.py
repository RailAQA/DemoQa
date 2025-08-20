import pytest
from url.url import URL
url = URL()


@pytest.mark.text_box_page
def test_send_form(text_box_page):
    text_box_page.open(url.Text_Box)
    text_box_page.form_filling()
    result_is_visible = text_box_page.form_result_is_visible()
    assert result_is_visible, 'После отправки формы не отображается результат формы'

#def test_results_sended_form(text_box_page):
 #   text_box_page.open(url.Text_Box)
  #  text_box_page.form_filling()

    