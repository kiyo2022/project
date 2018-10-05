from selenium import webdriver
driver = webdriver.Chrome("c:/Users/bfdev02/python/chromedriver.exe")
driver.get("https://www.tl-lincoln.net/accomodation/Ascsc1000InitAction.do")

lincoln_login_id = driver.find_element_by_id("txt_usrId")
lincoln_login_id.send_keys("M6458555")
lincoln_login_password = driver.find_element_by_id("password")
lincoln_login_password .send_keys("kirishima@09")
lincoln_login_btn = driver.find_element_by_id("doLogin")
lincoln_login_btn.click()
lincoln_login_btn2 = driver.find_element_by_id("doForceLogout")
lincoln_login_btn2.click()

zansitukanri_btn = driver.find_element_by_class_name("g_nav_list_btn3")
zansitukanri_btn.click()

zansitukanri_tbl = driver.find_element_by_name("raRMTypeInvRmrmCntDate4")
zansitukanri_ra = zansitukanri_tbl.get_attribute("value")
print(zansitukanri_ra)