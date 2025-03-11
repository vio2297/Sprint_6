import allure
import pytest
from locators.order_page_locators import TestOrderFormLocators
from data import Data


class TestPositiveOrderForm:

    @allure.title('Проверка позитивного сценария для заказа самоката через кнопку "Заказать" в заголовке страницы')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в заголовке страницы и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, date, comment', [Data.user_1])
    def test_positive_order_from_Order_button_header(self, driver, home_page, order_page, name, last_name, address, station, number,date, comment):
        home_page.click_order_button_header()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(date, comment)
        order_page.click_yes_on_confirm_order_form()
        assert order_page.is_order_complete_button_displayed()

    @allure.title('Проверка позитивного сценария для заказа самоката через кнопку Заказать в теле страницы')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле страницы и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, date, comment', [Data.user_2])
    def test_complete_order_form_order_button_body(self, driver, home_page, order_page, name, last_name, address, station, number,date, comment):
        home_page.scroll_to_order_button()
        home_page.click_order_button_body()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(date, comment)
        order_page.click_yes_on_confirm_order_form()
        assert order_page.is_order_complete_button_displayed()




