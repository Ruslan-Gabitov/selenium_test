from typing import Type
from utilities.logger import Logger
from pages.main_page import MainPage, locators
import allure


@allure.description("TestApplicationForm (Функциональное тестирование кнопки \"Написать\")")
class TestButtonGoToTelegram:

    def test_click_button_go_to_telegram(self, browser: Type[MainPage]):
        Logger.add_start_step(method="test_click_link_become_customer_header")
        browser.move_to_clickable_element(locators=locators.button_go_to_telegram).click()
        browser.switch_to_window(1)
        browser.save_screenshot(path=r"TestButtonGoToTelegram")
        assert browser.current_url() == "https://t.me/irlix_it"
        browser.close()
        browser.switch_to_window(0)
        browser.refresh()
        Logger.add_end_step(method="test_click_link_become_customer_header", url=browser.current_url())