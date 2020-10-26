from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    ENTER_BUTTON = (By.XPATH, '//div[contains(@class,"responseHead-module-button")]')
    INPUT_LOGIN = (By.XPATH, '// input[ @ name = "email"]')
    INPUT_PASSWORD = (By.XPATH, '// input[ @ name = "password"]')
    GO_TO_MAIN_PAGE_BUTTON = (By.XPATH, '// div[contains( @class , "authForm-module-button")]')


class AuthProblemPageLocators(object):
    INVALID_DATA_MESSAGE = (By.XPATH, '//div[contains( @class, "formMsg_text")]')


class BasePageLocators(object):
    GO_TO_SEGMENTS = (By.XPATH, '// a[ @ href = "/segments"]')
    USER_BUTTON = (By.XPATH, '// div[contains(@class, "right-module-rightButton")]')
    LOG_OUT = (By.XPATH, '//a[@href = "/logout"]')


class MainPageLocators(BasePageLocators):
    NAME_OF_USER = (By.XPATH, '//div[contains( @class, "userNameWrap")]')
    CREATE_COMPANY_FIRST_TIME = (By.XPATH, '//a[@href = "/campaign/new"]')
    CREATE_COMPANY_NOT_FIRST_TIME = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and text() = '
                                               '"Создать кампанию"]')
    FILTER_OPTIONS = (By.XPATH, '// span[contains(text(), "кампании") or contains(text(), "объявления")]')
    SELECT_FILTER = (By.XPATH, '//li[contains(@class, "optionsList-module") and text()="Активные кампании"]')
    NAME_OF_CREATED_COMPANY = (By.XPATH, '//a[contains(@class, "nameCell-module-campaignName") and text() = "Тестовая '
                                         'кампания"]')


class CreateCompanyPageLocators(BasePageLocators):
    AUDIO_ADVERT = (By.XPATH, '//div[contains(@class, "audiolistening")]')
    UPLOAD_AUDIO = (By.XPATH, '//input[contains(@class, "input__inp") and contains(@type,"file") ]')
    INPUT_COMPANY_NAME = (By.XPATH, '// div[contains( @class, "campaign-name")] / descendant::input')
    FINISH_CREATE_COMPANY_NAME = (By.XPATH, '//div[contains(@class, "button__text") and text()="Создать кампанию"]')


class SegmentsPageLocators(BasePageLocators):
    CREATE_SEGMENT_FIRST_TIME = (By.XPATH, '//a[@href = "/segments/segments_list/new/"]')
    CREATE_SEGMENT_NOT_FIRST_TIME = (By.XPATH, '//div[contains(@class, "button__text") and text()="Создать сегмент"]')
    SEGMENT_APPS_AND_GAMES = (By.XPATH, '//div[contains(@class,"adding-segments-item") and text()="Приложения и игры '
                                        'в соцсетях"]')
    PLAYED_AND_PAID = (By.XPATH, '//span[text()="Игравшие и платившие в платформе"]/ancestor::div[contains(@class, '
                                 '"adding-segments-source__header")]')
    CHECKBOX_PAID = (By.XPATH, '//input[@value="pay"]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(@class, "button__text") and text()="Добавить сегмент"]')
    INPUT_SEGMENT_NAME = (By.XPATH, '//div[contains(@class, "js-segment-name")]//input')
    CREATE_SEGMENT = (By.XPATH, '//div[contains(@class, "button__text") and text()="Создать сегмент"]')
    NAME_OF_CREATED_SEGMENT = (By.XPATH, '// a[text() = "Тестовый сегмент"]')
    NAME_OF_CREATED_SEGMENT_FOR_DELETE = (By.XPATH, '// a[text() = "Тестовый сегмент для удаления"]')
    TICK_TO_HIGHLIGHT = (By.XPATH, '// a[text() = "Тестовый сегмент для удаления"]/ancestor::div['
                                   '2]/preceding-sibling::div//input')
    ACTIONS_WITH_SEGMENT = (By.XPATH, '//div[contains(@class, "segmentsTable-module-selectItem")]')
    DELETE_SEGMENT = (By.XPATH, '//li[contains(@class, "optionsList-module-option" ) and text() = "Удалить"]')
