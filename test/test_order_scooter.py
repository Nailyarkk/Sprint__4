import pytest
from selenium import webdriver
from pages.fill_form_first_page import FillFormFirst
from pages.fill_form_second_page import FillFormSecond
from pages.order_scooter_button_main_page import OrderScooterButton
from pages.success_page import CheckSuccessOrder
from pages.click_logo_yandex import CheckLogoYandex
from pages.click_logo_scooter import CheckLogoScooter
from constants import *
import allure
class TestOrderScooter:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
    @pytest.mark.parametrize("button_order", [
        OrderScooterButton.button_order1,
        OrderScooterButton.button_order2
    ])
    @allure.description(
        'Заказ самоката. Проверяем весь флоу позитивного сценария')
    def test_order_scooter(self, button_order):
        self.driver.get(url)
        main_page = OrderScooterButton(self.driver)
        main_page.click_button(button_order)

        form_page1 = FillFormFirst(self.driver)
        form_page1.fill_form_and_click_button()

        form_page2 = FillFormSecond(self.driver)
        form_page2.fill_form_order()

        check_page = CheckSuccessOrder(self.driver)
        check_page.confirm_order()
        assert check_page.text == success_text

        order_page_logo_scooter = CheckLogoScooter(self.driver)
        order_page_logo_scooter.check_click_logo_scooter()

        order_page_logo_scooter = CheckLogoYandex(self.driver)
        order_page_logo_scooter.check_click_logo_yandex()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
