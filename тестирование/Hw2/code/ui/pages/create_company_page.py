from ui.locators.basic_locators import CreateCompanyPageLocators
from ui.pages.base_page import BasePage


class CreateCompanyPage(BasePage):
    locators = CreateCompanyPageLocators()

    def create_new_company(self, name_for_company):
        self.click(self.locators.AUDIO_ADVERT)
        self.fill_field(self.locators.INPUT_COMPANY_NAME, 'Тестовая кампания')
        music_upload = self.find(self.locators.UPLOAD_AUDIO)
        music_upload.send_keys(r"C:\Users\USER\Desktop\информатика\Python\тестирование\Hw2\code\sources\music1.mp3")
        self.click(self.locators.FINISH_CREATE_COMPANY_NAME)
