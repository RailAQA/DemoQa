from url.url import URL
import pytest
url = URL()

@pytest.mark.upload_page
def test_download_file(upload_page):
    upload_page.open(url.Upload_page)
    upload_page.scroll_to_downlodad_button()
    upload_page.click_to_download_button()
    file_is_downloaded = upload_page.check_file_is_saved()
    assert file_is_downloaded

@pytest.mark.upload_page
def test_upload_file(upload_page):
    upload_page.open(url.Upload_page)
    upload_page.scroll_to_upload_file_button()
    upload_page.upload_file()
    check_file_is_uploaded = upload_page.check_file_is_uploaded()
    assert check_file_is_uploaded
   
