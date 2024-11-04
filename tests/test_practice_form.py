import allure
from allure_commons.types import Severity
from selene import browser

from pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Форма регистрации")
@allure.story("Заполнение формы регистрации")
@allure.title("Отправка формы регистрации и проверка корректности отправленных значений")
@allure.link("https://github.com", name="github")
def test_practice_form(open_browser):
    registration = RegistrationPage()

    with allure.step('Открыть браузер и перейти на сайт'):
        browser.open("/automation-practice-form")

    """ WHEN """
    with allure.step('Ввести значение в поле first_name'):
        registration.fill_first_name("Алексей")

    with allure.step('Ввести значение в поле last_name'):
        registration.fill_last_name("Елисеев")

    with allure.step('Ввести значение в поле email'):
        registration.fill_email("qaguru@test.com")

    with allure.step('Указать значение поля gender'):
        registration.fill_gender_male()

    with allure.step('Ввести значение в поле mobile'):
        registration.fill_mobile_number("9999999999")

    with allure.step("Ввести значения поля birthday"):
        registration.fill_birthday("1992", "April", "04")

    with allure.step('Ввести значение в поле subjects'):
        registration.fill_subjects("English")

    with allure.step('Указать значение в поле hobbies'):
        registration.fill_hobbies()

    with allure.step('Загрузить изображение в в поле upload_picture'):
        registration.upload_picture("test_image.jpg")

    with allure.step('Ввести значение в поле Address'):
        registration.fill_current_address("Test Country, test city, test street, test house")

    with allure.step('Указать значение в поле state and city'):
        registration.fill_state_and_city()

    with allure.step('Нажать на кнопку Submit'):
        registration.click_submit_button()

    """ THEN """
    with allure.step("Проверить корректность отправленных значений"):
        registration.assert_value("Алексей Елисеев", "qaguru@test.com", "Male", "9999999999", "04 April,1992",
                                  "English",
                                  "Reading, Sports", "test_image.jpg",
                                  "Test Country, test city, test street, test house",
                                  "NCR Noida")
