from ui.locators.basic_locators import CreateCompanyPageLocators
from ui.pages.base_page import BasePage
import pathlib

class CreateCompanyPage(BasePage):
    locators = CreateCompanyPageLocators()

    def create_new_company(self, name_for_company):
        self.click(self.locators.AUDIO_ADVERT)
        self.fill_field(self.locators.INPUT_COMPANY_NAME, 'Тестовая кампания')
        music_upload = self.find(self.locators.UPLOAD_AUDIO)
        curr_dir = pathlib.Path(__file__).parent
        mp3_path = curr_dir.parent.parent / 'sources' / 'music1.mp3'
        music_upload.send_keys(str(mp3_path))
        self.click(self.locators.FINISH_CREATE_COMPANY_NAME)
