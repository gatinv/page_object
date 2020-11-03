from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.bulletin_page import BulletinPage
from .pages.asn_page import ASNPage
from .swagger import methods
import datetime
from datetime import timedelta
import requests
import os
import time

link = "https://250.aurus-sp.app/sign-in"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'send_me.txt') 

# prepare data
def test_country():
    methods.create_country ('RUS','Russian Federation')
    methods.create_country ('USA','United States of America')
    methods.create_country ('DEU','Germany')
    methods.create_country ('HUN','Hungary')

def test_supplier():
    methods.create_consolidated_supplier ('SUP01','Foreign Cosolidated Supplier','false','RUAEP','Gatin','CONS1','every day','10','productionPlanner','Gatin','igfifth@gmail.com','+7 909 313 64 36','en','NY','NY','USA','NY','America/New_York')
    methods.create_direct_supplier ('SUP02','Foreign Direct Supplier','false','RUAEP','Gatin','every day','10','productionPlanner','Gatin','igfifth@gmail.com','+7 909 313 64 36','en','Budapest','Budapest','HUN','Budapest','Europe/Budapest')
    methods.create_direct_supplier ('SUP03','Local Direct Supplier','true','RUAEP','Gatin','every day','10','productionPlanner','Gatin','igfifth@gmail.com','+7 909 313 64 36','en','Moscow','Moscow','RUS','Moscow','Europe/Moscow')
    methods.create_consolidator ('CONS1','Consolidator','false','RUAEP','Gatin','every day','10','2','productionPlanner','Gatin','igfifth@gmail.com','+7 909 313 64 36','en','Berlin','Berlin','DEU','Berlin','Europe/Berlin')

def test_part():
    methods.create_part ('p11','Деталь1 Поставщик1','Part1 SUP01','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p12','Деталь2 Поставщик1','Part2 SUP01','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p13','Деталь3 Поставщик1','Part3 SUP01','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p21','Деталь1 Поставщик2','Part1 SUP02','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p22','Деталь2 Поставщик2','Part2 SUP02','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p23','Деталь3 Поставщик2','Part3 SUP02','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p31','Деталь1 Поставщик3','Part1 SUP03','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p32','Деталь2 Поставщик3','Part2 SUP03','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')
    methods.create_part ('p33','Деталь3 Поставщик3','Part3 SUP03','шт.','15','RUAEP','2020-01-01','1','100','10','2020-01-01','pack-001','100')

def test_partSupplier():
    methods.create_partSupplier('p11','SUP01','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p12','SUP01','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p13','SUP01','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p21','SUP02','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p22','SUP02','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p23','SUP02','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p31','SUP03','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p32','SUP03','RUAEP','asn-001','135','2020-08-01','10','1','1')
    methods.create_partSupplier('p33','SUP03','RUAEP','asn-001','135','2020-08-01','10','1','1')

def test_orders():
    startDay=datetime.date.today()-timedelta(days=100)
    endDay=datetime.date.today()
    print(f'Creating ordersfrom {startDay} to {endDay}')
    methods.create_orders(startDay,endDay,'RUAEP','SUP01','p11','p12','p13')
    methods.create_orders(startDay,endDay,'RUAEP','SUP02','p21','p22','p23')
    methods.create_orders(startDay,endDay,'RUAEP','SUP03','p31','p32','p33')

def test_create_asn(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to asn list
    page = MainPage(browser, link)
    page.go_to_ASN()    
    page = ASNPage(browser,link)
    page.createASN('SCAC1','RUAEP','CONTAINER1','test','11/03/2020','BOL001','FREIGHT001','995','1000','CONTRACT1','part001','100','1000','шт.','10','GBR','10','','','BIGBOX001','1000')
 
def test_create_bulletins(browser):
# log in as super user
    page = LoginPage(browser, link)
    page.open()
    page.choose_english_as_default_language()
    page.login_as("superuser@test.tst", "password!D1")
# go to bullet list management
    page = MainPage(browser, link)
    page.go_to_bulletins_list()
    page.go_to_bulletins_list()
    page.go_to_bulletins_list()
# clean bulletins
    page = BulletinPage(browser, link)
    page.clean_up_bulletins_list(browser)

# get token
def test_run():
    methods.delete_user('123@test.tst')

def test_run3():
    methods.create_user('123','123@test.tst','Supplier data viewer', 'SUP02')

def test_del_country ():
    country_id=methods.get_country_id('GBR')
    methods.delete_country(country_id)

def test_del_supplier ():
    methods.delete_supplier('CONS1')
    
def test_del_part ():
    methods.delete_part('p11')

def test_del_partSupplier ():
    methods.delete_partSupplier('p11')