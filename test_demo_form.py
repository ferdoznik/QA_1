import pytest
from selene.support.shared import browser
from selene import be, have, command


@pytest.fixture()
def set_browser_resolution():
    browser.config.window_height = 1080
    browser.config.window_width = 1700


@pytest.fixture()
def open_url():
    browser.open('https://demoqa.com/automation-practice-form')


def test_practice_form(set_browser_resolution, open_url):
    browser.element('#firstName').should(be.visible).type('Keanu')
    browser.element('#lastName').type('Reeves')
    browser.element('#userEmail').should(be.blank).type('ferdoznik@gmail.com')
    browser.element('//label[contains(text(), "Male")]').click()
    browser.element('#userNumber').should(be.blank).type('9053603200')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1964"]').click()
    browser.element('.react-datepicker__day--002').click()
    browser.element('#subjectsInput').type('Math')
    browser.element('#react-select-2-option-0').click()
    browser.element('//label[contains(text(), "Music")]').click()
    browser.element('#currentAddress').should(be.blank).type('Among mortal beings')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').should(be.visible).press_enter()
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Keanu Reeves'))
    browser.element('.table-responsive').should(have.text('ferdoznik@gmail.com'))
    browser.element('#closeLargeModal') \
        .perform(command.js.scroll_into_view).click()
    browser.element('#example-modal-sizes-title-lg') \
        .should(have.no.text('Thanks for submitting the form'))

