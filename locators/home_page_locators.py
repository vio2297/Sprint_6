from selenium.webdriver.common.by import By


class HomePageLocators:

    # Навигация по странице
    ORDER_BUTTON_HEADER = By.XPATH, ".//button[text() = 'Заказать']" # Кнопка заказать в хедере
    ORDER_BUTTON_BODY = By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]" # Кнопка Заказать в теле страницы
    FAQ = By.XPATH, ".//div[text()= 'Вопросы о важном']" # Вопросы о важном
    LOGO_SAMOKAT = By.XPATH, "//a[@href='/' and contains(@class, 'Header_LogoScooter')]" # Логотип Самокат
    LOGO_YANDEX = By.XPATH, "//a[@href='//yandex.ru' and contains(@class, 'Header_LogoYandex')]" # Логотип Яндекс
    DZEN_PAGE_LOGO = By.XPATH, "//*[@id='dzen-header']" # Логотип Дзена

    #FAQ
    #1
    FAQ_1_BUTTON = By.XPATH, ".//div[@id='accordion__heading-0'] "
    ANSWER_FAQ_1 = By.XPATH, ".//div[@id='accordion__panel-0']"
    #2
    FAQ_2_BUTTON = By.XPATH, ".//div[@id='accordion__heading-1'] "
    ANSWER_FAQ_2 = By.XPATH, ".//div[@id='accordion__panel-1']"
    # 3
    FAQ_3_BUTTON = By.XPATH, ".//div[@id='accordion__heading-2'] "
    ANSWER_FAQ_3 = By.XPATH, ".//div[@id='accordion__panel-2']"
    # 4
    FAQ_4_BUTTON = By.XPATH, ".//div[@id='accordion__heading-3'] "
    ANSWER_FAQ_4 = By.XPATH, ".//div[@id='accordion__panel-3']"
    # 5
    FAQ_5_BUTTON = By.XPATH, ".//div[@id='accordion__heading-4'] "
    ANSWER_FAQ_5 = By.XPATH, ".//div[@id='accordion__panel-4']"
    # 6
    FAQ_6_BUTTON = By.XPATH, ".//div[@id='accordion__heading-5'] "
    ANSWER_FAQ_6 = By.XPATH, ".//div[@id='accordion__panel-5']"
    # 7
    FAQ_7_BUTTON = By.XPATH, ".//div[@id='accordion__heading-6'] "
    ANSWER_FAQ_7 = By.XPATH, ".//div[@id='accordion__panel-6']"
    # 8
    FAQ_8_BUTTON = By.XPATH, ".//div[@id='accordion__heading-7'] "
    ANSWER_FAQ_8 = By.XPATH, ".//div[@id='accordion__panel-7']"



