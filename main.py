import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def set_browser_resolution():
    browser.config.window_height = 1090
    browser.config.window_width = 1700


def test_google_search(set_browser_resolution):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="rso"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_random_input_search(set_browser_resolution):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('askjdgqiuwehq').press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))
