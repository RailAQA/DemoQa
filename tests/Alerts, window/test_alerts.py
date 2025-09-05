import pytest
from url.url import URL
url = URL()

@pytest.mark.alerts_page
def test_alert_button(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_first_alert_button()
    alert_is_opened = alerts_page.checker_alert_is_opened()
    assert alert_is_opened

@pytest.mark.alerts_page
def test_timer_alert(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_timer_alert_button()
    alert_opened_after_5_sec = alerts_page.checker_alert_is_opened
    assert alert_opened_after_5_sec

@pytest.mark.alerts_page
def test_timer_alert(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_cofirm_button()
    alert_is_opened = alerts_page.checker_alert_is_opened()
    assert alert_is_opened

@pytest.mark.alerts_page
def test_timer_alert_close(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_cofirm_button() 
    alerts_page.random_acepting_alert()
    alert_is_closed = alerts_page.checker_alert_is_closed()
    resust_text_is_correct = alerts_page.check_result_confirming_alert()
    assert alert_is_closed
    assert resust_text_is_correct

@pytest.mark.smoke
def test_timer_alert_close(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_promt_button()
    alerts_page.send_text_to_alert()
    result_promt_is_correct = alerts_page.check_entered_promt()
    assert result_promt_is_correct