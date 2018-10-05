
zansitukanri = driver.find_element_by_xpath("//input[@name='raRmTypeInvRmrmCntDate4']")[2]
zansitukanri.send_keys("4")

zansitukanri = driver.find_element_by_xpath('//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[5]/div/input')
zan_value = zansitukanri.get_attribute("value")
if int(zan_value) == 2:
    print("YES")
else:
    print("NO")

raRmTypeInvRmrmCntDate1

https://www.seleniumhq.org/