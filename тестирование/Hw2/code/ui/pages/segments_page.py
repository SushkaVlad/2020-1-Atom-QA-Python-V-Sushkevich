from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):
    locators = SegmentsPageLocators()

    def go_to_create_segment(self):
        el = self.find(self.locators.CREATE_SEGMENT_FIRST_TIME)
        if el.is_displayed():
            el.click()
        else:
            self.click(self.locators.CREATE_SEGMENT_NOT_FIRST_TIME)

    def create_segment(self, name_of_segment = None):
        self.go_to_create_segment()
        self.click(self.locators.SEGMENT_APPS_AND_GAMES)
        self.click(self.locators.PLAYED_AND_PAID)
        self.click(self.locators.CHECKBOX_PAID)
        self.click(self.locators.ADD_SEGMENT)
        auto_name = self.find(self.locators.INPUT_SEGMENT_NAME).get_attribute("value")
        if name_of_segment:
            self.fill_field(self.locators.INPUT_SEGMENT_NAME, name_of_segment)
        self.click(self.locators.CREATE_SEGMENT)
        return auto_name

    def delete_segment(self):
        self.click(self.locators.TICK_TO_HIGHLIGHT)
        self.click(self.locators.ACTIONS_WITH_SEGMENT)
        self.click(self.locators.DELETE_SEGMENT)
