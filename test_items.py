from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_item_basket(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    assert button.is_enabled()
    assert EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))

