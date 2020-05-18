import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_check_for_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    check = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.text == check.text, 'Different values'
