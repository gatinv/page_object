from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.bulletin_page import BulletinPage
from .swagger import methods
import requests
import os
import time

link = "https://200.aurus-sp.app/sign-in"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'send_me.txt') 

def test_create_bulletins(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to bullet list management
    page = MainPage(browser, link)
    page.go_to_bulletins_list()
# clean bulletins
    page = BulletinPage(browser, link)
    page.clean_up_bulletins_list(browser)

# get token
def test_run():
    user_id=methods.get_user_id('123@test.tst')
    methods.delete_user(user_id)

def test_run2():
    methods.create_user('123','123@test.tst','Supplier data viewer', 'SUP02')