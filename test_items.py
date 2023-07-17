from selenium.webdriver.common.by import By

def test_user_can_see_purchase_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_btn is not None