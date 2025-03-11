import allure
import pytest
from data import Data
from locators.home_page_locators import HomePageLocators


class TestHomePageSamokat:


    @allure.title('Проверка отдела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего текта при нажатии на вопрос')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (HomePageLocators.FAQ_1_BUTTON, HomePageLocators.ANSWER_FAQ_1, Data.expected_text['FAQ1']),
        (HomePageLocators.FAQ_2_BUTTON, HomePageLocators.ANSWER_FAQ_2, Data.expected_text['FAQ2']),
        (HomePageLocators.FAQ_3_BUTTON, HomePageLocators.ANSWER_FAQ_3, Data.expected_text['FAQ3']),
        (HomePageLocators.FAQ_4_BUTTON, HomePageLocators.ANSWER_FAQ_4, Data.expected_text['FAQ4']),
        (HomePageLocators.FAQ_5_BUTTON, HomePageLocators.ANSWER_FAQ_5, Data.expected_text['FAQ5']),
        (HomePageLocators.FAQ_6_BUTTON, HomePageLocators.ANSWER_FAQ_6, Data.expected_text['FAQ6']),
        (HomePageLocators.FAQ_7_BUTTON, HomePageLocators.ANSWER_FAQ_7, Data.expected_text['FAQ7']),
        (HomePageLocators.FAQ_8_BUTTON, HomePageLocators.ANSWER_FAQ_8, Data.expected_text['FAQ8'])
        ])

    def test_clicking_on_questions_gives_answer(self, driver, home_page, question_locator, answer_locator, expected_text):
        home_page.scroll_to_faq()
        home_page.click_on_question(question_locator)
        answer = home_page.get_the_answer_text(answer_locator)
        assert answer == expected_text, f"Ожидалось: {expected_text}, но получили: {answer}"


    @allure.title('Проверка нажатии на логотип Яндекс')
    @allure.description('Проверка, что при нажатии на логотип Яндекс, произойдет переход на главную страницу Дзен')
    def test_clicking_yandex_logo_opens_dzen_page(self, driver, home_page):
        home_page.click_yandex_logo_opens_dzen_page()
        assert home_page.get_current_url() == Data.DZEN_PAGE_URL

    @allure.title('Проверка нажатии на логотип Самокат')
    @allure.description('Проверка, что при нажатии на логотип Самокат, произойдет переход на главную страницу Самокат')
    def test_clicking_samokat_logo_opens_main_samokat_page(self, driver, home_page):
        home_page.click_order_button_header()
        home_page.click_samokat_logo_opens_main_samokat_page()
        assert home_page.get_current_url() == Data.MAIN_PAGE_URL

















