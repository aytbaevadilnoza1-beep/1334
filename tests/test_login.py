import time

from conftest import driver_chrome
from pages.login_page import LoginPage
from pages.home_page import  HomePage



def test_login_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in")
    login_page = LoginPage(driver_chrome)
    login_page.enter_phone_number("998944507906")
    login_page.click_btn_next()
    login_page.enter_password("185379000")
    login_page.click_btn_submit()
    try:
        login_page.click_btn_sessions()
        time.sleep(2)
        login_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_chrome)
    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_exit_btn()
    home_page.click_confirm_exit()


# def test_login_edge(driver_edge):
#     driver_edge.get("https://my.proweb.uz/log-in")
#     login_page = LoginPage(driver_edge)
#     login_page.enter_phone_number("998944507906")
#     login_page.click_btn_next()
#     login_page.enter_password("185379000")
#     login_page.click_btn_submit()
#     try:
#         login_page.click_btn_sessions()
#         time.sleep(2)
#         login_page.click_btn_finish()
#     except:
#         pass







