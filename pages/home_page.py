import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from data import Data

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step('Нажатие на логотип Яндекс и проверка открытия главной страницы Дзен')
    def click_yandex_logo_opens_dzen_page(self):
        self.wait_visibility_of_element(self.locators.LOGO_YANDEX)
        self.click_on_element(self.locators.LOGO_YANDEX)
        self.switch_to_next_tab()
        self.wait_visibility_of_element(self.locators.DZEN_PAGE_LOGO)
        self.wait_url_to_be(Data.DZEN_PAGE_URL)

    @allure.step('Нажатие на логотип Самокат и проверка открытия главной страницы Самоката')
    def click_samokat_logo_opens_main_samokat_page(self):
        self.click_on_element(self.locators.LOGO_SAMOKAT)
        self.wait_visibility_of_element(self.locators.LOGO_SAMOKAT)

    @allure.step('Нажатие кнопки заказать в заголовке страницы')
    def click_order_button_header(self):
        self.wait_visibility_of_element(self.locators.ORDER_BUTTON_HEADER)
        self.click_on_element(self.locators.ORDER_BUTTON_HEADER)

    @allure.step('Прокрутить страницу до кнопки заказать в теле страницы')
    def scroll_to_order_button(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BODY)
        self.wait_visibility_of_element(self.locators.ORDER_BUTTON_BODY)

    @allure.step('Нажать на кнопку заказать в теле страницы')
    def click_order_button_body(self):
        self.wait_visibility_of_element(self.locators.ORDER_BUTTON_BODY)
        self.click_on_element(self.locators.ORDER_BUTTON_BODY)

    @allure.step('Прокрутить страницу до отдела Вопросы о важном')
    def scroll_to_faq(self):
        self.scroll_to_element(self.locators.FAQ_8_BUTTON)
        self.wait_visibility_of_element(self.locators.FAQ_8_BUTTON)

    @allure.step('Нажатие на вопрос')
    def click_on_question(self, question_locator):
        self.wait_visibility_of_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step('Получение ответа на вопрос')
    def get_the_answer_text(self, answer_locator):
        self.wait_visibility_of_element(answer_locator)
        answer = self.get_text_on_element(answer_locator)
        return answer






