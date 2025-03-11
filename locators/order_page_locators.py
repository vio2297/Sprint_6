
from selenium.webdriver.common.by import By

class TestOrderFormLocators:
    # Для кого самокат
    # Поле Имя
    NAME_INPUT = By.XPATH, ".//input[@placeholder='* Имя']"
    # Поле Фамилия
    SURNAME_INPUT = By.XPATH, ".//input[@placeholder='* Фамилия']"
    # Поле Адрес
    ADDRESS_INPUT = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    # Поле станция метро
    UNDERGROUND_STATION = By.XPATH, ".//input[@placeholder='* Станция метро']"
    # Выбор станции
    SELECT_UNDERGROUND = (By.XPATH, ".//li[@class='select-search__row']")
    # Телефон
    PHONE_INPUT = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    CONTINUE_BUTTON = By.XPATH, ".//button[text()= 'Далее']"


    # Про аренду серый
    TITLE_ABOUT_RENT_FORM = By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']"
    # Когда привести самокат
    DELIVERY_DATE_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # Календарь
    CALENDAR_DELIVERY_DATE = By.XPATH, "//div[contains(@class, 'react-datepicker')]"
    # Срок аренды
    RENTAL_DURATION = By.XPATH, ".//div[text()='* Срок аренды']"
    RENTAL_DURATION_LIST = By.XPATH, "//div[contains(@class, 'Dropdown-menu') and @aria-expanded='true']"
    # Двое суток
    LISTED_RENTAL_PERIOD = By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']"
    # Цвет самоката
    CHOOSE_COLOUR = By.XPATH, "//div[text()='Цвет самоката']"
    # Цвет серый
    CHECKBOX_GREY = By.XPATH, "//input[@id='grey']"
    # Комментарий для курьера
    COMMENT_INPUT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # Кнопка Заказать
    ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"


    # Форма Хотите оформить заказ?
    CONFIRM_ORDER_FORM = By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]"
    # Кнопка Да
    YES_BUTTON_CONFIRM_ORDER = By.XPATH, "//button[text()='Да']"


    # Форма успешного заказа
    COMPLETE_ORDER_BUTTON = By.XPATH, ".//*[text()='Посмотреть статус']"