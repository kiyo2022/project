from selenium import webdriver
driver = webdriver.Chrome("c:/Users/bfdev02/python/chromedriver.exe")
driver.get("https://www.tl-lincoln.net/accomodation/Ascsc1000InitAction.do")

zansitukanri = driver.find_element_by_xpath("//input[@name='raRmTypeInvRmrmCntDate4']")[2]
zansitukanri.send_keys("4")