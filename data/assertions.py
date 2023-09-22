from playwright.sync_api import Page
from data.environment import host
from playwright.sync_api import expect
from pages.base import Base


class Assertions(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def check_URL(self, uri, msg):
        expect(self.page).to_have_url(f"{host.get_base_url()}{uri}", timeout=10000), msg


    def check_equals(self, actual, expected, msg):
        assert actual == expected, msg


    def check_is_less_then(self, first, second, msg):
        assert first < second, msg


    def check_presence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_visible(visible=True, timeout=12000), msg


    def check_absence(self, locator, msg):
        loc = self.page.locator(locator)
        expect(loc).to_be_hidden(timeout=700), msg


    def button_is_disabled(self, locator: str) -> bool:
        button = self.page.query_selector(locator)
        return button.is_disabled()


    def check_url_content(self, uri,msg):
        assert f"{uri}" in self.page.url, msg


    def check_box_activated(self, locator, msg): #проверка что чек бокс поставлен
        loc = self.page.locator(locator)
        expect(loc).to_be_checked(), msg


    def element_disabled(self, locator, msg): #веб элемент отключен
        loc = self.page.locator(locator)
        expect(loc).to_be_disabled(), msg


    def to_be_editable(self, locator, msg): #возможно редактировать
        loc = self.page.locator(locator)
        expect(loc).to_be_editable(), msg


    def to_be_empty(self, locator, msg): #web element пустой
        loc = self.page.locator(locator)
        expect(loc).to_be_empty(), msg


    def contain_text(self, locator, text: str, msg): #элемент содержит текст
        loc = self.page.locator(locator)
        expect(loc).to_contain_text(text), msg


    def have_text(self, locator, text: str, msg): #локатор имеет текст
        loc = self.page.locator(locator)
        expect(loc).to_have_text(text), msg


    def select_have_values(self, locator, options: list, msg): #Select имеет опции для выбора (опция передается аргументом к проверке)
        loc = self.page.locator(locator)
        loc.select_option(options)
        expect(loc).to_have_values(options), msg