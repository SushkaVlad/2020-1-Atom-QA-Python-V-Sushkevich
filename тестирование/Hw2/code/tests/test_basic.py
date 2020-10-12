import pytest

from tests.base import BaseCase


class Test(BaseCase):
    @pytest.mark.UI
    def test_create_company(self, log_to_main_page):
        create_cm_page = log_to_main_page.go_to_create_company_page()
        create_cm_page.create_new_company("Тестовая кампания")
        self.main_page.click(self.main_page.locators.FILTER_OPTIONS)
        assert self.main_page.find(self.main_page.locators.NAME_OF_CREATED_COMPANY)

    @pytest.mark.UI
    def test_create_segment(self, log_to_main_page):
        sg_page = log_to_main_page.go_to_segments_page()
        name_of_segment = sg_page.create_segment("Тестовый сегмент")
        assert sg_page.find(sg_page.locators.NAME_OF_CREATED_SEGMENT)

    @pytest.mark.UI
    def test_delete_segment(self, log_to_main_page):
        sg_page = log_to_main_page.go_to_segments_page()
        sg_page.create_segment("Тестовый сегмент для удаления")
        sg_page.delete_segment()
        lst = self.driver.find_elements(*sg_page.locators.INPUT_SEGMENT_NAME)
        assert len(lst) == 0

    @pytest.mark.UI
    def test_correct_auth(self, correct_auth_data):
        self.login_page.click(self.login_page.locators.ENTER_BUTTON)
        self.login_page.fill_field(self.login_page.locators.INPUT_LOGIN, correct_auth_data['login'])
        self.login_page.fill_field(self.login_page.locators.INPUT_PASSWORD, correct_auth_data['password'])
        self.login_page.find(self.login_page.locators.GO_TO_MAIN_PAGE_BUTTON).click()
        assert self.main_page.find(self.main_page.locators.NAME_OF_USER).text == "СУШКЕВИЧ ВЛАДИСЛАВ"

    @pytest.mark.UI
    def test_incorrect_auth(self, incorrect_auth_data):
        self.login_page.click(self.login_page.locators.ENTER_BUTTON)
        self.login_page.fill_field(self.login_page.locators.INPUT_LOGIN, incorrect_auth_data['login'])
        self.login_page.fill_field(self.login_page.locators.INPUT_PASSWORD, incorrect_auth_data['password'])
        self.login_page.find(self.login_page.locators.GO_TO_MAIN_PAGE_BUTTON).click()
        assert self.auth_problem_page.find(self.auth_problem_page.locators.INVALID_DATA_MESSAGE).text == "Invalid " \
                                                                                                         "login or " \
                                                                                                         "password"
