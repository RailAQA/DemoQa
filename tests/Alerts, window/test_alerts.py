import pytest
from url.url import URL
url = URL()

@pytest.mark.smoke
def test_alert_button(alerts_page):
    alerts_page.open(url.Alerts_Page)
    alerts_page.click_to_first_alert_button()
    alert_is_opened = alerts_page.checker_alert_is_opened()
    assert alert_is_opened