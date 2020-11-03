from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.users_page import UsersPage
from .swagger import methods
import os
import time

link = os.environ.get('spurl')

def test_create_user_as_su(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
#  go to users
    page = MainPage(browser, link)
    page.go_to_users()
# check Create user
    page = UsersPage(browser, link)
    page.add_user('test_mail@tst.tst', 'test_name', 'Data viewer', 'SUP01')
# check new user row
    page.check_user_row (browser, "test_mail@tst.tst", "test_name")

def test_modify_user_as_su (browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to users
    page = MainPage(browser, link)
    page.go_to_users()
# modify user
    page = UsersPage(browser, link)
    page.modify_user('test_mail@tst.tst', 'su')
# check modified user row
    page.check_user_row (browser, "test_mail@tst.tst", "Edited by su")

def test_create_user_as_ba (browser):
# log in as business administrator
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("ba@tst.tst", "password!D1")
# go to users
    page = MainPage(browser, link)
    page.go_to_users()
# create business administrator
    page = UsersPage(browser, link)
    page.add_user('ba@tst.tst', 'business admin', 'Business administrator', 'SUP01')
# check new user row
    page.check_user_row (browser, "ba@tst.tst", "business admin")
# sign out
    page = MainPage(browser, link)
    page.sign_out()



# check Own GSDB view data
# check Other GSDB view data
# check Own GSDB modify data
# check Other GSDB modify data