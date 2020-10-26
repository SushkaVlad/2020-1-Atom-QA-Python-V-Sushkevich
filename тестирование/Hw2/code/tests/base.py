import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.auth_problem_page import AuthProblemPage
from ui.pages.base_page import BasePage
from ui.pages.create_company_page import CreateCompanyPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.segments_page import SegmentsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.auth_problem_page: AuthProblemPage = request.getfixturevalue('auth_problem_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.create_company_page: CreateCompanyPage = request.getfixturevalue('create_company_page')
        self.segments_page: SegmentsPage = request.getfixturevalue('segments_page')
