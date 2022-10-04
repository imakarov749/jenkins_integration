import allure
from allure_commons.types import Severity

from model.pages import registration_form


# убрал фикстуры в этой версии теста, теперь браузер открывается и конфигурируется функцией

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'imakarov749')
@allure.feature('Регистрация пользователя в системе')
@allure.story('Я, как пользователь, хочу иметь возможность регистрации на сайте')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_fill_registration_form():
    # GIVEN

    registration_form.opened_and_configure_browser()

    # WHEN

    registration_form.set_first_name('Ivan')

    registration_form.set_last_name('Ivanov')

    registration_form.set_email('ivan.ivanov@kljh.com')

    registration_form.choose_gender()

    registration_form.set_phone_number('7123456789')

    registration_form.choose_birth_date_from_calendar()

    registration_form.choose_hobbies()

    registration_form.set_address('Moscow')

    registration_form.set_subject('Math')

    registration_form.upload_image()

    registration_form.choose_state('Uttar Pradesh')
    registration_form.choose_city('Lucknow')

    registration_form.click_submitting_button()
    registration_form.check_open_submitting_window()

    # THEN

    registration_form.check_fields_in_submitting_window(
        [
            ('Student Name', 'Ivan Ivanov'),
            ('Student Email', 'ivan.ivanov@kljh.com'),
            ('Gender', 'Male'),
            ('Mobile', '7123456789'),
            ('Date of Birth', '12 December,1912'),
            ('Subjects', 'Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'photo_image.jpg'),
            ('Address', 'Moscow'),
            ('State and City', 'Uttar Pradesh Lucknow')
        ]
    )

    registration_form.close_submitting_window()
