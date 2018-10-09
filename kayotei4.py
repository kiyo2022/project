# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome("c:/Users/bfdev02/python/chromedriver.exe")
driver.get("https://www.tl-lincoln.net/accomodation/Ascsc1000InitAction.do")
#ログインまでの処理
lincoln_login_id = driver.find_element_by_id("txt_usrId")
lincoln_login_id.send_keys("M6458555")
lincoln_login_password = driver.find_element_by_id("password")
lincoln_login_password .send_keys("kirishima@09")
lincoln_login_btn = driver.find_element_by_id("doLogin")
lincoln_login_btn.click()
cur_url = driver.current_url
if cur_url == "https://www.tl-lincoln.net/accomodation/Ascsc1000LogInAction.do":
	lincoln_login_btn2 = driver.find_element_by_id("doForceLogout")
	lincoln_login_btn2.click()

zansitukanri_btn = driver.find_element_by_class_name("g_nav_list_btn3")
zansitukanri_btn.click()

yoku2syu = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[1]/div[1]/ul/li[6]/a/span')
yoku2syu.click()




sousin = driver.find_element_by_xpath('//*[@id="sendBtn"]')
sousin.click()
#指定したdriverに対して最大で10秒間待つように設定する
wait = WebDriverWait(driver, 10)
#Alertが表示されるまで待機するよう設定する
wait.until(expected_conditions.alert_is_present())
#5秒間待機する（Alertが表示されていることを確認するため）
time.sleep(5)
#AlertのOKボタンを押下する
Alert(driver).accept()
time.sleep(5)
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])
driver.close()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])