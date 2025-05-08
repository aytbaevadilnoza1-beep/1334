from pages.login_page import LoginPage


def test_login_chrome(driver):
    driver.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver)
    login_page.enter_phone_number("998978879555")
    login_page.click_btn_next()
    login_page.enter_password("The0pend00r")
    login_page.click_btn_submit()
    # login_page.click_btn_sessions()
    # login_page.click_btn_finish()


def test_login_edge(driver_edge):
    driver_edge.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver_edge)
    login_page.enter_phone_number("998978879555")
    login_page.click_btn_next()
    login_page.enter_password("The0pend00r")
    login_page.click_btn_submit()
    # login_page.click_btn_sessions()
    # login_page.click_btn_finish()





