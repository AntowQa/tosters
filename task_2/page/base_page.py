from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s
from selene import be, query

from settings import BASE_URL, DEFAULT_COLOR


class BasePage:
    def __init__(self):
        self.base_url = BASE_URL
        self.browser = browser
        self.h2_headings = ss('h2')

    def open_site(self):
        self.browser.open(self.base_url)
        self.h2_headings.matching(be.visible)

    def check_color_headings(self, file_name):
        headings = self.h2_headings
        colors_heads = [head.get(query.css_property('color')) for head in headings]
        assert set(colors_heads) != DEFAULT_COLOR, f'Возможно проблема в этом файле {file_name}'
