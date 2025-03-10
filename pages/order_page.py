import allure
from locators.order_page_locators import TestOrderFormLocators
from pages.base_page import BasePage
class OrderFormPage(BasePage):

    @allure.step('Заполнить поле имя')
    def set_first_name(self, name):
        self.set_text_in_element(TestOrderFormLocators.NAME_INPUT, name)
        return self

    @allure.step('Заполнить поле Фамилия')
    def set_last_name(self, last_name):
        self.set_text_in_element(TestOrderFormLocators.SURNAME_INPUT, last_name)
        return self

    @allure.step('Заполнить поле Адрес')
    def set_address(self,address):
        self.set_text_in_element(TestOrderFormLocators.ADDRESS_INPUT, address)
        return self

    @allure.step('Выбрать станцию метро')
    def select_station(self):
        self.click_on_element(TestOrderFormLocators.SELECT_UNDERGROUND)

    @allure.step('Настроить поле Станция Метро')
    def set_underground(self, station):
        self.click_on_element(TestOrderFormLocators.UNDERGROUND_STATION)
        self.set_text_in_element(TestOrderFormLocators.UNDERGROUND_STATION, station)
        self.wait_visibility_of_element(TestOrderFormLocators.UNDERGROUND_STATION_LIST)
        self.select_station()
        return self

    @allure.step('Заполнить поле Телефон')
    def set_phone(self, number):
        self.set_text_in_element(TestOrderFormLocators.PHONE_INPUT, number)
        return self

    @allure.step('Нажать кнопку далее')
    def click_continue_button(self):
        self.click_on_element(TestOrderFormLocators.CONTINUE_BUTTON)

    @allure.step('Проверка отображения второй формы заказа')
    def check_second_form_title_displayed(self):
        self.check_displaying_of_element(TestOrderFormLocators.TITLE_ABOUT_RENT_FORM)

    @allure.step('Заполнить поле когда привезти самокат')
    def set_rental_date(self, date):
        self.set_text_in_element(TestOrderFormLocators.DELIVERY_DATE_INPUT, date)
        return self

    @allure.step('Выбираем период аренды самоката')
    def select_rental_period(self):
        self.click_on_element(TestOrderFormLocators.LISTED_RENTAL_PERIOD)

    @allure.step('Настраиваем период аренды самоката')
    def set_rental_duration(self):
        self.click_on_element(TestOrderFormLocators.RENTAL_DURATION)
        self.wait_visibility_of_element(TestOrderFormLocators.RENTAL_DURATION_LIST)
        self.select_rental_period()

    @allure.step('Выбираем цвет самоката')
    def set_color_field(self):
        self.click_on_element(TestOrderFormLocators.CHECKBOX_GREY)
        return self

    @allure.step('Оставляем комментарий')
    def set_comment_field(self, comment):
        self.set_text_in_element(TestOrderFormLocators.COMMENT_INPUT, comment)
        return self

    @allure.step('Нажимаем кнопку заказать')
    def click_order_button(self):
        self.click_on_element(TestOrderFormLocators.ORDER_BUTTON)
        self.wait_visibility_of_element(TestOrderFormLocators.CONFIRM_ORDER_FORM)

    @allure.step('Проверка отображения окна подтверждения, после нажатия кнопки далее ')
    def check_displaying_confirm_window(self):
        self.check_displaying_of_element(TestOrderFormLocators.CONFIRM_ORDER_FORM)

    @allure.step('Нажать кнопку да в окне подтверждения заказа')
    def click_yes_on_confirm_order_form(self):
        self.click_on_element(TestOrderFormLocators.YES_BUTTON_CONFIRM_ORDER)
        self.wait_visibility_of_element(TestOrderFormLocators.COMPLETE_ORDER_BUTTON)
        return self

    @allure.step('Заполнение первой формы заказа самоката и нажатие кнопки далее')
    def personal_information_input(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_underground(station)
        self.set_phone(number)
        self.click_continue_button()
        self.check_second_form_title_displayed()

    @allure.step('Заполнение второй формы заказа самоката и окна подтверждения')
    def rental_information_input(self, date, comment):
        self.set_rental_date(date)
        self.set_color_field()
        self.set_rental_duration()
        self.set_comment_field(comment)
        self.click_order_button()
        self.check_displaying_confirm_window()












