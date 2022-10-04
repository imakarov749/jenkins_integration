import allure
from selene import be, have
import os
from selene.support.conditions import be
from selene.support.shared import browser

from model.controls import dropdown, modal


@allure.step('Выполняем предусловия для теста')
def opened_and_configure_browser():
    browser.config.hold_browser_open = True
    browser.config.base_url = 'https://demoqa.com'
    browser.open('/automation-practice-form')
    browser.should(have.url('https://demoqa.com/automation-practice-form'))
    browser.element('.main-header').should(be.visible)
    browser.driver.set_window_size(1920, 1080)


@allure.step('Заполняем имя')
def set_first_name(name):
    browser.element('#firstName').should(be.blank).type(name)


@allure.step('Заполняем фамилию')
def set_last_name(last_name):
    browser.element('#lastName').should(be.blank).type(last_name)


@allure.step('Заполняем email')
def set_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


@allure.step('Выбираем гендер')
def choose_gender():
    browser.element("[for='gender-radio-1']").click()


@allure.step('Заполняем номер телефона')
def set_phone_number(phone_number):
    browser.element('#userNumber').should(be.blank).type(phone_number)


@allure.step('Выбираем дату рождения из календаря')
def choose_birth_date_from_calendar():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1912"]').click()
    browser.element('.react-datepicker__day--012').click()


# v2.можно ввести дату рождения вручную
# @allure.step('Вводим дату рождения вручную')
# def set_birth_from_controls(birth_for_type):
# birth_for_type = '12 Dec 1912' - больше не нужна, но я оставлю для второго варианта ввода даты рождения
# birth = browser.element('#dateOfBirthInput').click()
# birth.clear().set_value(birth_for_type).press_enter()
# birth.send_keys(Keys.CONTROL + 'a').type(birth_for_type).press_enter()
@allure.step('Выбираем хобби')
def choose_hobbies():
    browser.element("[for='hobbies-checkbox-1']").click()


@allure.step('Заполняем адресс')
def set_address(address_for_type):
    browser.element('#currentAddress').should(be.blank).type(address_for_type)


@allure.step('Заполняем предметы')
def set_subject(subject):
    browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()


@allure.step('Загружаем изображение')
def upload_image():
    file_path = os.path.abspath("../resources/photo_image.jpg")
    browser.element('#uploadPicture').send_keys(file_path)


@allure.step('Выбираем страну')
def choose_state(value):
    dropdown.select(browser.element('#state'), value)


@allure.step('Выбираем город')
def choose_city(value):
    dropdown.select(browser.element('#city'), value)


@allure.step('Нажимаем на кнопку подтверждения формы')
def click_submitting_button():
    browser.element('#submit').click()


@allure.step('Проверяем открытие pop-up финальной формы')
def check_open_submitting_window():
    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(
        have.text('Thanks for submitting the form'))


@allure.step('Закрываем финальную форму')
def close_submitting_window():
    browser.element('#closeLargeModal').click()


@allure.step('Проверяем точность заполнения полей в форме')
def check_fields_in_submitting_window(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
