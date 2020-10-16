from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.bulletin_page import BulletinPage
import os
import time

link = "https://250.aurus-sp.app/sign-in"
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
# check create bulletin
    page = BulletinPage(browser, link)
    page.add_new_bulletin_with_attachment_for_everyone('attachment.txt')
    page.add_new_bulletin_only_for("SUP01")
    page.add_new_bulletin_only_for("SUP02")
    page.add_old_bulletin_with_attachment_for_everyone('attachment.txt')
    page.add_old_bulletin_only_for("SUP01")
    page.add_old_bulletin_only_for("SUP02")

def test_check_visibility_su(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to bulletin board
    page = MainPage(browser, link)
    page.go_to_bulletins_board()
# check view data
    page = BulletinPage(browser, link)
    page.wait_for_alert(browser)
    page.check_bulletins_current_aurus(3)
    page.go_to_past_bulletins()
    page.check_bulletins_past_aurus(3)

def test_check_visibility_sa(browser):
# log in as security admin
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("igfifth+sup01secadmin@gmail.com", "password!D2")
# go to bulletin board
    page = MainPage(browser, link)
    page.go_to_bulletins_board()
# check view data
    page = BulletinPage(browser, link)
    page.wait_for_alert(browser)
    page.check_bulletins_current_aurus(3)
    page.go_to_past_bulletins()
    page.check_bulletins_past_aurus(3)

def test_check_visibility_ba(browser):
# log in as business admin
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("igfifth+sup01businessadmin@gmail.com", "password!D1")
# go to bulletin board
    page = MainPage(browser, link)
    page.go_to_bulletins_board()
# check view data

    page = BulletinPage(browser, link)
    page.check_bulletins_sa()

def test_check_modifying_su(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to bullet list management
    page = MainPage(browser, link)
    page.go_to_bulletins_list()
# check modify data
    time.sleep(5)
    page = BulletinPage(browser, link)
    page.modify_bulletin()
