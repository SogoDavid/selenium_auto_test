import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
