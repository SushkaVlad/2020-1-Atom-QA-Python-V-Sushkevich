from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.create_company_page import CreateCompanyPage

# MainPage в нашем случае это страница, на которую мы попадаем после авторизации (страница компаний)
from ui.pages.segments_page import SegmentsPage


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_create_company_page(self):
        el = self.driver.find_elements(*self.locators.CREATE_COMPANY_FIRST_TIME)
        if len(el) != 0:
            self.click(self.locators.CREATE_COMPANY_FIRST_TIME)
        else:
            self.click(self.locators.CREATE_COMPANY_NOT_FIRST_TIME)
        return CreateCompanyPage(self.driver)

    def go_to_segments_page(self):
        self.click(self.locators.GO_TO_SEGMENTS)
        return SegmentsPage(self.driver)


