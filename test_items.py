from selenium.webdriver.common.by import By

link = r' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_btn_exists(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, f"Button wasn't found!"

