# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome("c:/Users/bfdev02/python/chromedriver.exe")
driver.get("https://www.tl-lincoln.net/accomodation/Ascsc1000InitAction.do")
#���O�C���܂ł̏���
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

####################�������炪���l�O�ɂ��鏈��

nichiji = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[2]/table/tbody/tr/td[1]/div/a/div')
nichiji.click()

WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])
print(len(driver.window_handles))

nettype = driver.find_element_by_xpath('//*[@id="gBodyPopup"]/div/div[2]/ul/li[3]/a')
nettype.click()
check = driver.find_element_by_xpath('//*[@id="checkBoxNetRoomTypeGroupGrp2_0"]')
check.click()
zansitu = driver.find_element_by_xpath('//*[@id="groupSsStatusFlgOff"]')
zansitu.click()
sousin0 = driver.find_element_by_xpath('//*[@id="sendBtn"]')
sousin0.click()

#�w�肵��driver�ɑ΂��čő��10�b�ԑ҂悤�ɐݒ肷��
wait = WebDriverWait(driver, 10)
#Alert���\�������܂őҋ@����悤�ݒ肷��
wait.until(expected_conditions.alert_is_present())
#3�b�ԑҋ@����iAlert���\������Ă��邱�Ƃ��m�F���邽�߁j
time.sleep(5)
#Alert��OK�{�^������������
Alert(driver).accept()

time.sleep(5)
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])

driver.close()





time.sleep(5)
#�����܂ł����l�O�ɂ��鏈���I�I�I�I�I�I

driver.switch_to.window(driver.window_handles[0])
yoku2syu = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[1]/div[1]/ul/li[6]/a/span')
yoku2syu.click()