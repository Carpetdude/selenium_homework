from selenium.webdriver.common.by import By

def test_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_btn is not None