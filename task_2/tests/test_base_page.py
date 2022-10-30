import pytest
from helpers.base_helper import get_css_files
from page.base_page import BasePage
import os
from settings import PATH_FILES_SITE

css_files = get_css_files()


@pytest.mark.parametrize('iterate', range(len(css_files)))
def test_check_h2_headers_of_homepage(browser_session, rename_file, iterate):
    rename_file(css_files)
    base_page = BasePage()
    base_page.open_site()
    base_page.check_color_headings(
        file_name=css_files[iterate]
    )
