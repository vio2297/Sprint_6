import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Дождаться видимости элемента')
    def wait_visibility_of_element(self,locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Дождаться загрузки станицы')
    def wait_url_to_be(self,url):
        return WebDriverWait(self.driver, 25).until(expected_conditions.url_to_be(url))

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Переключиться на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.text

    @allure.step('Ввести значение в поле ввода')
    def set_text_in_element(self, locator, text):
        element = self.wait_visibility_of_element(locator)
        element.send_keys(text)


    @allure.step('Получаем адрес страницы')
    def get_current_url(self):
        return self.driver.current_url













