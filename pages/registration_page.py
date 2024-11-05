from selene import browser, have

from resourses import CURRENT_DIR


class RegistrationPage:
    def __init__(self):
        pass

    def browser_open(self, url):
        browser.open(url)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def fill_first_name(self, fist_name):
        browser.element("#firstName").type(fist_name)
        return self

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)
        return self

    def fill_email(self, email):
        browser.element("#userEmail").type(email)
        return self

    def fill_gender_male(self):
        browser.element('//label[contains(text(), "Male")]').click()
        return self

    def fill_mobile_number(self, mobile_number):
        browser.element("#userNumber").set_value(mobile_number)
        return self

    def fill_birthday(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click().element(f'[value="{year}"]').click()
        browser.element(".react-datepicker__month-select").click().element(
            f'//option[contains(text(),"{month}")]').click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, subjects):
        browser.element("#subjectsInput").type(subjects).press_enter()
        return self

    def fill_hobbies(self):
        browser.element("//label[text()='Reading']").click()
        browser.element("//label[text()='Sports']").click()
        return self

    def upload_picture(self, file):
        """path /files"""
        browser.element("#uploadPicture").send_keys(f"{CURRENT_DIR}/files/{file}")
        return self

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def fill_state_and_city(self):
        # browser.driver.execute_script("window.scrollBy(0, 100);")
        browser.element("#state").click()
        browser.element(
            "//div[contains(@id, 'react-select-3-option-0') and text()='NCR']").click()
        browser.element("#react-select-4-input").type("Noida").press_enter()
        return self

    def click_submit_button(self):
        browser.element("#submit").click()
        return self

    def assert_value(self, name, email, gender_male, mobile_phone, date_of_birth, subjects, hobbies, picture_name,
                     address, state_and_city):
        browser.element("//tr[td[contains(text(), 'Student Name')]]").should(have.text(name))
        browser.element("//tr[td[contains(text(), 'Student Email')]]").should(have.text(email))
        browser.element("//tr[td[contains(text(), 'Gender')]]").should(have.text(gender_male))
        browser.element("//tr[td[contains(text(), 'Mobile')]]").should(have.text(mobile_phone))
        browser.element("//tr[td[contains(text(), 'Date of Birth')]]").should(have.text(date_of_birth))
        browser.element("//tr[td[contains(text(), 'Subjects')]]").should(have.text(subjects))
        browser.element("//tr[td[contains(text(), 'Hobbies')]]").should(have.text(hobbies))
        browser.element("//tr[td[contains(text(), 'Picture')]]").should(have.text(picture_name))
        browser.element("//tr[td[contains(text(), 'Address')]]").should(have.text(address))
        browser.element("//tr[td[contains(text(), 'State and City')]]").should(have.text(state_and_city))
        return self
