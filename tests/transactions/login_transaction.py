from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage


class LoginTransaction(AbstractTransaction):

    def do(self, url, user, password):
        page = LoginPage(self._driver)
        page.login(user, password)

        return self._driver.current_url
