# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.Chrome("c:/Users/Ycafe4/python/chromedriver.exe")
driver.get("https://www.tl-lincoln.net/accomodation/Ascsc1000InitAction.do")
#OCÜÅÌ
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

############ÖtF[Y1######################
def kansi():
	#lðæŸ
	def getvalue(xpath, xpath2):
	    kaisya = driver.find_element_by_xpath(xpath)
	    v = kaisya.get_attribute("value")
	    if v == '':
	        kaisya3 = driver.find_element_by_xpath(xpath2)
	        v = kaisya3.text
	    try:
	        v = int(v)
	        print(v)
	        return v
	    except:
	        v = 0
	        print(v)
	        return v
	#lðÏX
	def sendkey(xpath ,v):
	    kaisya2 = driver.find_element_by_xpath(xpath)
	    kaisya2.clear()
	    kaisya2.send_keys(v)
	    
	###########»è
	def henkou(aa ,bb ,bsyamei, cc , csyamei, dd ,dsyamei ,ee ,esyamei ,ff ,fsyamei ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
	    def hantei13(aa , bb ,bsyamei):
	        def hantei12(aa , cc ,csyamei):
	            def hantei11(aa , dd ,dsyamei):
	                def hantei10(aa , ee ,esyamei):
	                    def hantei9(aa , ff ,fsyamei):
	                        def hantei8(aa , gg ,gsyamei):
	                            def hantei7(aa , hh ,hsyamei):
	                                def hantei6(aa , ii ,isyamei):
	                                    def hantei5(aa , jj ,jsyamei):
	                                        def hantei4(aa , kk ,ksyamei):
	                                            def hantei3(aa , ll ,lsyamei):
	                                                def hantei2(aa ,mm ,msyamei):
	                                                    def hantei1(aa ,nn ,nsyamei):
	                                                        if nn + aa >= 0:
	                                                            nn += aa
	                                                            sendkey(nsyamei, nn)
	                                                        elif nn > 0 and nn + aa < 0:
	                                                            sendkey(nsyamei, 0)
	                                                            aa += nn
	                                                        else:
	                                                            print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
	                                                    if mm + aa >= 0:
	                                                        mm += aa
	                                                        sendkey(msyamei, mm)
	                                                    elif mm > 0 and mm + aa < 0:
	                                                        sendkey(msyamei, 0)
	                                                        aa += mm
	                                                        hantei1(aa ,nn ,nsyamei)
	                                                    else:
	                                                        hantei1(aa ,nn ,nsyamei)
	                                            if ll + aa >= 0:
	                                                ll += aa
	                                                sendkey(lsyamei, ll)
	                                            elif ll > 0 and ll + aa < 0:
	                                                sendkey(lsyamei, 0)
	                                                aa += ll
	                                                hantei2(aa ,mm ,msyamei)
	                                            else:
	                                                hantei2(aa ,mm ,msyamei)
	                                        if kk + aa >= 0:
	                                            kk += aa
	                                            sendkey(ksyamei, kk)
	                                        elif kk > 0 and kk + aa < 0:
	                                            sendkey(ksyamei, 0)
	                                            aa += kk
	                                            hantei3(aa ,ll ,lsyamei)
	                                        else:
	                                            hantei3(aa ,ll ,lsyamei)
	                                    if jj + aa >= 0:
	                                        jj += aa
	                                        sendkey(jsyamei, jj)
	                                    elif jj > 0 and jj + aa < 0:
	                                        sendkey(jsyamei, 0)
	                                        aa += jj
	                                        hantei4(aa ,kk ,ksyamei)
	                                    else:
	                                        hantei4(aa ,kk ,ksyamei)
	                                if ii + aa >= 0:
	                                    ii += aa
	                                    sendkey(isyamei, ii)
	                                elif ii > 0 and ii + aa < 0:
	                                    sendkey(isyamei, 0)
	                                    aa += ii
	                                    hantei5(aa ,jj ,jsyamei)
	                                else:
	                                    hantei5(aa ,jj ,jsyamei)
	                            if hh + aa >= 0:
	                                hh += aa
	                                sendkey(hsyamei, hh)
	                            elif hh > 0 and hh + aa < 0:
	                                sendkey(hsyamei, 0)
	                                aa += hh
	                                hantei6(aa ,ii ,isyamei)
	                            else:
	                                hantei6(aa ,ii ,isyamei)
	                        if gg + aa >= 0:
	                            gg += aa
	                            sendkey(gsyamei, gg)
	                        elif gg > 0 and gg + aa < 0:
	                            sendkey(gsyamei, 0)
	                            aa += gg
	                            hantei7(aa ,hh ,hsyamei)
	                        else:
	                            hantei7(aa ,hh ,hsyamei)
	                    if ff + aa >= 0:
	                        ff += aa
	                        sendkey(fsyamei, ff)
	                    elif ff > 0 and ff + aa < 0:
	                        sendkey(fsyamei, 0)
	                        aa += ff
	                        hantei8(aa ,gg ,gsyamei)
	                    else:
	                        hantei8(aa ,gg ,gsyamei)
	                if ee + aa >= 0:
	                    ee += aa
	                    sendkey(esyamei, ee)
	                elif ee > 0 and ee + aa < 0:
	                    sendkey(esyamei, 0)
	                    aa += ee
	                    hantei9(aa ,ff ,fsyamei)
	                else:
	                    hantei9(aa ,ff ,fsyamei)
	            if dd + aa >= 0:
	                dd += aa
	                sendkey(dsyamei, dd)
	            elif dd > 0 and dd + aa < 0:
	                sendkey(dsyamei, 0)
	                aa += dd
	                hantei10(aa ,ee ,esyamei)
	            else:
	                hantei10(aa ,ee ,esyamei)
	        if cc + aa >= 0:
	            cc += aa
	            sendkey(csyamei, cc)
	        elif cc > 0 and cc + aa < 0:
	            sendkey(csyamei, 0)
	            aa += cc
	            hantei11(aa ,dd ,dsyamei)
	        else:
	            hantei11(aa ,dd ,dsyamei)
	    if bb + aa >= 0:
	        bb += aa
	        sendkey(bsyamei, bb)
	    elif bb > 0 and bb + aa < 0:
	        sendkey(bsyamei, 0)
	        aa += bb
	        hantei12(aa ,cc ,csyamei)
	    else:
	        hantei12(aa ,cc ,csyamei)
	        
	x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
	for z in x:
	    #aº15ô 
	    #JTB02  
	    jtb = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb2 = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    c = getvalue(jtb, jtb2)
	    #ßEú{c[Xg 
	    kinki = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div/input'
	    kinki2 = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div'
	    d = getvalue(kinki, kinki2)
	    #ú{·s 
	    nihon = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div/input'
	    nihon2 = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div'
	    e = getvalue(nihon, nihon2)
	    #gbvcA[ 
	    top = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div/input'
	    top2 = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div'
	    f = getvalue(top, top2)
	    #ANA 
	    ANA = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div/input'
	    ANA2 = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div'
	    g = getvalue(ANA, ANA2)
	    #JRãB51 
	    JR51 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR512 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div'
	    h = getvalue(JR51, JR512)
	    #JRãB52 
	    JR52 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR522 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div'
	    i = getvalue(JR52, JR522)
	    #aº15ôilbgj
	    wasitunet = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    wasitunet2 = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div'
	    a = getvalue(wasitunet, wasitunet2)

	    #aº15ôiAbvO[h)
	    upgrade = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    upgrade2 = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div'
	    j = getvalue(upgrade,upgrade2)

	    #aº15ôi1ú3®Àèj
	    gentei = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    gentei2 = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div'
	    b = getvalue(gentei, gentei2)

	    #ÁÊº(06) 
	    jyuntoku = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    jyuntoku2 = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div'
	    k = getvalue(jyuntoku, jyuntoku2)

	    #ÁÊº(05)
	    #JTB01 
	    jtb01 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb012 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    m = getvalue(jtb01, jtb012)
	    #ÁÊº(05lbg) 
	    toku05 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku052 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div'
	    l = getvalue(toku05, toku052)
	    #ÁÊº(01lbg) 
	    toku01 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku012 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div'
	    n = getvalue(toku01, toku012)
	    print ("tuginohihe")

	    #a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if a < 0:
	        henkou(a, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
            
	    if b < 0:
	        henkou(b, a, wasitunet, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if c < 0:
	        henkou(c, a, wasitunet, b, gentei, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if d < 0:
	        henkou(d, a, wasitunet, b, gentei, c, jtb, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if e < 0:
	        henkou(e, a, wasitunet, b, gentei, c, jtb, d, kinki, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if f < 0:
	        henkou(f, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if g < 0:
	        henkou(g, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if h < 0:
	        henkou(h, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if i < 0:
	        henkou(i, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if j < 0:
	        henkou(j, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if k < 0:
	        henkou(k, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, l, toku05, m, jtb01, n, toku01)
	    if l < 0:
	        henkou(l, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, m, jtb01, n, toku01)
	    if m < 0:
	        henkou(m, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if n < 0:
	        henkou(n, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01)

##############ÖtF[YI¹###################
kansi()
yoku2syu = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[1]/div[1]/ul/li[6]/a/span')
yoku2syu.click()
#######################ÖtF[Y2#########################
def kansi2():
	#lðæŸ
	def getvalue(xpath, xpath2):
	    kaisya = driver.find_element_by_xpath(xpath)
	    v = kaisya.get_attribute("value")
	    if v == '':
	        kaisya3 = driver.find_element_by_xpath(xpath2)
	        v = kaisya3.text
	    try:
	        v = int(v)
	        print(v)
	        return v
	    except:
	        v = 0
	        print(v)
	        return v
	#lðÏX
	def sendkey(xpath ,v):
	    kaisya2 = driver.find_element_by_xpath(xpath)
	    kaisya2.clear()
	    kaisya2.send_keys(v)
	    
	###########»è1###################
	def henkou(aa ,bb ,bsyamei, cc , csyamei, dd ,dsyamei ,ee ,esyamei ,ff ,fsyamei ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
	    def hantei13(aa , bb ,bsyamei):
	        def hantei12(aa , cc ,csyamei):
	            def hantei11(aa , dd ,dsyamei):
	                def hantei10(aa , ee ,esyamei):
	                    def hantei9(aa , ff ,fsyamei):
	                        def hantei8(aa , gg ,gsyamei):
	                            def hantei7(aa , hh ,hsyamei):
	                                def hantei6(aa , ii ,isyamei):
	                                    def hantei5(aa , jj ,jsyamei):
	                                        def hantei4(aa , kk ,ksyamei):
	                                            def hantei3(aa , ll ,lsyamei):
	                                                def hantei2(aa ,mm ,msyamei):
	                                                    def hantei1(aa ,nn ,nsyamei):
	                                                        if nn + aa >= 0:
	                                                            nn += aa
	                                                            sendkey(nsyamei, nn)
	                                                        elif nn > 0 and nn + aa < 0:
	                                                            sendkey(nsyamei, 0)
	                                                            aa += nn
	                                                        else:
	                                                            print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
	                                                    if mm + aa >= 0:
	                                                        mm += aa
	                                                        sendkey(msyamei, mm)
	                                                    elif mm > 0 and mm + aa < 0:
	                                                        sendkey(msyamei, 0)
	                                                        aa += mm
	                                                        hantei1(aa ,nn ,nsyamei)
	                                                    else:
	                                                        hantei1(aa ,nn ,nsyamei)
	                                            if ll + aa >= 0:
	                                                ll += aa
	                                                sendkey(lsyamei, ll)
	                                            elif ll > 0 and ll + aa < 0:
	                                                sendkey(lsyamei, 0)
	                                                aa += ll
	                                                hantei2(aa ,mm ,msyamei)
	                                            else:
	                                                hantei2(aa ,mm ,msyamei)
	                                        if kk + aa >= 0:
	                                            kk += aa
	                                            sendkey(ksyamei, kk)
	                                        elif kk > 0 and kk + aa < 0:
	                                            sendkey(ksyamei, 0)
	                                            aa += kk
	                                            hantei3(aa ,ll ,lsyamei)
	                                        else:
	                                            hantei3(aa ,ll ,lsyamei)
	                                    if jj + aa >= 0:
	                                        jj += aa
	                                        sendkey(jsyamei, jj)
	                                    elif jj > 0 and jj + aa < 0:
	                                        sendkey(jsyamei, 0)
	                                        aa += jj
	                                        hantei4(aa ,kk ,ksyamei)
	                                    else:
	                                        hantei4(aa ,kk ,ksyamei)
	                                if ii + aa >= 0:
	                                    ii += aa
	                                    sendkey(isyamei, ii)
	                                elif ii > 0 and ii + aa < 0:
	                                    sendkey(isyamei, 0)
	                                    aa += ii
	                                    hantei5(aa ,jj ,jsyamei)
	                                else:
	                                    hantei5(aa ,jj ,jsyamei)
	                            if hh + aa >= 0:
	                                hh += aa
	                                sendkey(hsyamei, hh)
	                            elif hh > 0 and hh + aa < 0:
	                                sendkey(hsyamei, 0)
	                                aa += hh
	                                hantei6(aa ,ii ,isyamei)
	                            else:
	                                hantei6(aa ,ii ,isyamei)
	                        if gg + aa >= 0:
	                            gg += aa
	                            sendkey(gsyamei, gg)
	                        elif gg > 0 and gg + aa < 0:
	                            sendkey(gsyamei, 0)
	                            aa += gg
	                            hantei7(aa ,hh ,hsyamei)
	                        else:
	                            hantei7(aa ,hh ,hsyamei)
	                    if ff + aa >= 0:
	                        ff += aa
	                        sendkey(fsyamei, ff)
	                    elif ff > 0 and ff + aa < 0:
	                        sendkey(fsyamei, 0)
	                        aa += ff
	                        hantei8(aa ,gg ,gsyamei)
	                    else:
	                        hantei8(aa ,gg ,gsyamei)
	                if ee + aa >= 0:
	                    ee += aa
	                    sendkey(esyamei, ee)
	                elif ee > 0 and ee + aa < 0:
	                    sendkey(esyamei, 0)
	                    aa += ee
	                    hantei9(aa ,ff ,fsyamei)
	                else:
	                    hantei9(aa ,ff ,fsyamei)
	            if dd + aa >= 0:
	                dd += aa
	                sendkey(dsyamei, dd)
	            elif dd > 0 and dd + aa < 0:
	                sendkey(dsyamei, 0)
	                aa += dd
	                hantei10(aa ,ee ,esyamei)
	            else:
	                hantei10(aa ,ee ,esyamei)
	        if cc + aa >= 0:
	            cc += aa
	            sendkey(csyamei, cc)
	        elif cc > 0 and cc + aa < 0:
	            sendkey(csyamei, 0)
	            aa += cc
	            hantei11(aa ,dd ,dsyamei)
	        else:
	            hantei11(aa ,dd ,dsyamei)
	    if bb + aa >= 0:
	        bb += aa
	        sendkey(bsyamei, bb)
	    elif bb > 0 and bb + aa < 0:
	        sendkey(bsyamei, 0)
	        aa += bb
	        hantei12(aa ,cc ,csyamei)
	    else:
	        hantei12(aa ,cc ,csyamei)
	###########»è2###################
	def henkou2(aa ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
		def hantei8(aa , gg ,gsyamei):
			def hantei7(aa , hh ,hsyamei):
				def hantei6(aa , ii ,isyamei):
					def hantei5(aa , jj ,jsyamei):
						def hantei4(aa , kk ,ksyamei):
							def hantei3(aa , ll ,lsyamei):
								def hantei2(aa ,mm ,msyamei):
									def hantei1(aa ,nn ,nsyamei):
										if nn + aa >= 0:
											nn += aa
											sendkey(nsyamei, nn)
										elif nn > 0 and nn + aa < 0:
											sendkey(nsyamei, 0)
											aa += nn
										else:
											print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
								if mm + aa >= 0:
									mm += aa
									sendkey(msyamei, mm)
								elif mm > 0 and mm + aa < 0:
									sendkey(msyamei, 0)
									aa += mm
									hantei1(aa ,nn ,nsyamei)
								else:
									hantei1(aa ,nn ,nsyamei)
							if ll + aa >= 0:
								ll += aa
								sendkey(lsyamei, ll)
							elif ll > 0 and ll + aa < 0:
								sendkey(lsyamei, 0)
								aa += ll
								hantei2(aa ,mm ,msyamei)
							else:
								hantei2(aa ,mm ,msyamei)
						if kk + aa >= 0:
							kk += aa
							sendkey(ksyamei, kk)
						elif kk > 0 and kk + aa < 0:
							sendkey(ksyamei, 0)
							aa += kk
							hantei3(aa ,ll ,lsyamei)
						else:
							hantei3(aa ,ll ,lsyamei)
					if jj + aa >= 0:
						jj += aa
						sendkey(jsyamei, jj)
					elif jj > 0 and jj + aa < 0:
						sendkey(jsyamei, 0)
						aa += jj
						hantei4(aa ,kk ,ksyamei)
					else:
						hantei4(aa ,kk ,ksyamei)
				if ii + aa >= 0:
					ii += aa
					sendkey(isyamei, ii)
				elif ii > 0 and ii + aa < 0:
					sendkey(isyamei, 0)
					aa += ii
					hantei5(aa ,jj ,jsyamei)
				else:
					hantei5(aa ,jj ,jsyamei)
			if hh + aa >= 0:
				hh += aa
				sendkey(hsyamei, hh)
			elif hh > 0 and hh + aa < 0:
				sendkey(hsyamei, 0)
				aa += hh
				hantei6(aa ,ii ,isyamei)
			else:
				hantei6(aa ,ii ,isyamei)
		if gg + aa >= 0:
			gg += aa
			sendkey(gsyamei, gg)
		elif gg > 0 and gg + aa < 0:
			sendkey(gsyamei, 0)
			aa += gg
			hantei7(aa ,hh ,hsyamei)
		else:
			hantei7(aa ,hh ,hsyamei)
	###########»è3###################
	def henkou3(aa ,ff ,fsyamei ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
		def hantei9(aa , ff ,fsyamei):
			def hantei8(aa , gg ,gsyamei):
				def hantei7(aa , hh ,hsyamei):
					def hantei6(aa , ii ,isyamei):
						def hantei5(aa , jj ,jsyamei):
							def hantei4(aa , kk ,ksyamei):
								def hantei3(aa , ll ,lsyamei):
									def hantei2(aa ,mm ,msyamei):
										def hantei1(aa ,nn ,nsyamei):
											if nn + aa >= 0:
												nn += aa
												sendkey(nsyamei, nn)
											elif nn > 0 and nn + aa < 0:
												sendkey(nsyamei, 0)
												aa += nn
											else:
												print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
									if mm + aa >= 0:
										mm += aa
										sendkey(msyamei, mm)
									elif mm > 0 and mm + aa < 0:
										sendkey(msyamei, 0)
										aa += mm
										hantei1(aa ,nn ,nsyamei)
									else:
										hantei1(aa ,nn ,nsyamei)
								if ll + aa >= 0:
									ll += aa
									sendkey(lsyamei, ll)
								elif ll > 0 and ll + aa < 0:
									sendkey(lsyamei, 0)
									aa += ll
									hantei2(aa ,mm ,msyamei)
								else:
									hantei2(aa ,mm ,msyamei)
							if kk + aa >= 0:
								kk += aa
								sendkey(ksyamei, kk)
							elif kk > 0 and kk + aa < 0:
								sendkey(ksyamei, 0)
								aa += kk
								hantei3(aa ,ll ,lsyamei)
							else:
								hantei3(aa ,ll ,lsyamei)
						if jj + aa >= 0:
							jj += aa
							sendkey(jsyamei, jj)
						elif jj > 0 and jj + aa < 0:
							sendkey(jsyamei, 0)
							aa += jj
							hantei4(aa ,kk ,ksyamei)
						else:
							hantei4(aa ,kk ,ksyamei)
					if ii + aa >= 0:
						ii += aa
						sendkey(isyamei, ii)
					elif ii > 0 and ii + aa < 0:
						sendkey(isyamei, 0)
						aa += ii
						hantei5(aa ,jj ,jsyamei)
					else:
						hantei5(aa ,jj ,jsyamei)
				if hh + aa >= 0:
					hh += aa
					sendkey(hsyamei, hh)
				elif hh > 0 and hh + aa < 0:
					sendkey(hsyamei, 0)
					aa += hh
					hantei6(aa ,ii ,isyamei)
				else:
					hantei6(aa ,ii ,isyamei)
			if gg + aa >= 0:
				gg += aa
				sendkey(gsyamei, gg)
			elif gg > 0 and gg + aa < 0:
				sendkey(gsyamei, 0)
				aa += gg
				hantei7(aa ,hh ,hsyamei)
			else:
				hantei7(aa ,hh ,hsyamei)
		if ff + aa >= 0:
			ff += aa
			sendkey(fsyamei, ff)
		elif ff > 0 and ff + aa < 0:
			sendkey(fsyamei, 0)
			aa += ff
			hantei8(aa ,gg ,gsyamei)
		else:
			hantei8(aa ,gg ,gsyamei)


	x = ['1', '2', '3', '4']
	for z in x:
	    #aº15ô 
	    #JTB02  
	    jtb = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb2 = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    c = getvalue(jtb, jtb2)
	    #ßEú{c[Xg 
	    kinki = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div/input'
	    kinki2 = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div'
	    d = getvalue(kinki, kinki2)
	    #ú{·s 
	    nihon = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div/input'
	    nihon2 = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div'
	    e = getvalue(nihon, nihon2)
	    #gbvcA[ 
	    top = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div/input'
	    top2 = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div'
	    f = getvalue(top, top2)
	    #ANA 
	    ANA = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div/input'
	    ANA2 = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div'
	    g = getvalue(ANA, ANA2)
	    #JRãB51 
	    JR51 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR512 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div'
	    h = getvalue(JR51, JR512)
	    #JRãB52 
	    JR52 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR522 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div'
	    i = getvalue(JR52, JR522)
	    #aº15ôilbgj
	    wasitunet = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    wasitunet2 = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div'
	    a = getvalue(wasitunet, wasitunet2)

	    #aº15ôiAbvO[h)
	    upgrade = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    upgrade2 = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div'
	    j = getvalue(upgrade,upgrade2)

	    #aº15ôi1ú3®Àèj
	    gentei = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    gentei2 = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div'
	    b = getvalue(gentei, gentei2)

	    #ÁÊº(06) 
	    jyuntoku = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    jyuntoku2 = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div'
	    k = getvalue(jyuntoku, jyuntoku2)

	    #ÁÊº(05)
	    #JTB01 
	    jtb01 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb012 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    m = getvalue(jtb01, jtb012)
	    #ÁÊº(05lbg) 
	    toku05 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku052 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div'
	    l = getvalue(toku05, toku052)
	    #ÁÊº(01lbg) 
	    toku01 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku012 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div'
	    n = getvalue(toku01, toku012)
	    print ("tuginohihe")

	    #a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if a < 0:
	        henkou(a, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
            
	    if b < 0:
	        henkou(b, a, wasitunet, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if c < 0:
	        henkou(c, a, wasitunet, b, gentei, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if d < 0:
	        henkou(d, a, wasitunet, b, gentei, c, jtb, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if e < 0:
	        henkou(e, a, wasitunet, b, gentei, c, jtb, d, kinki, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if f < 0:
	        henkou(f, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if g < 0:
	        henkou(g, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if h < 0:
	        henkou(h, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if i < 0:
	        henkou(i, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if j < 0:
	        henkou(j, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if k < 0:
	        henkou(k, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, l, toku05, m, jtb01, n, toku01)
	    if l < 0:
	        henkou(l, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, m, jtb01, n, toku01)
	    if m < 0:
	        henkou(m, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if n < 0:
	        henkou(n, a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01)
	x = ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
	for z in x:
	    #aº15ô 
	    #JTB02  
	    jtb = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb2 = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    c = getvalue(jtb, jtb2)
	    #ßEú{c[Xg 
	    kinki = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div/input'
	    kinki2 = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div'
	    d = getvalue(kinki, kinki2)
	    #ú{·s 
	    nihon = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div/input'
	    nihon2 = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div'
	    e = getvalue(nihon, nihon2)
	    #gbvcA[ 
	    top = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div/input'
	    top2 = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div'
	    f = getvalue(top, top2)
	    #ANA 
	    ANA = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div/input'
	    ANA2 = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div'
	    g = getvalue(ANA, ANA2)
	    #JRãB51 
	    JR51 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR512 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div'
	    h = getvalue(JR51, JR512)
	    #JRãB52 
	    JR52 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR522 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div'
	    i = getvalue(JR52, JR522)
	    #aº15ôilbgj
	    wasitunet = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    wasitunet2 = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div'
	    a = getvalue(wasitunet, wasitunet2)

	    #aº15ôiAbvO[h)
	    upgrade = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    upgrade2 = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div'
	    j = getvalue(upgrade,upgrade2)

	    #aº15ôi1ú3®Àèj
	    gentei = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    gentei2 = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div'
	    b = getvalue(gentei, gentei2)

	    #ÁÊº(06) 
	    jyuntoku = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    jyuntoku2 = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div'
	    k = getvalue(jyuntoku, jyuntoku2)

	    #ÁÊº(05)
	    #JTB01 
	    jtb01 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb012 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    m = getvalue(jtb01, jtb012)
	    #ÁÊº(05lbg) 
	    toku05 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku052 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div'
	    l = getvalue(toku05, toku052)
	    #ÁÊº(01lbg) 
	    toku01 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku012 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div'
	    n = getvalue(toku01, toku012)
	    print ("tuginohihe")

	    #a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if a < 0:
	        henkou2(a, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
            
	    if b < 0:
	        henkou2(b, a, wasitunet, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if c < 0:
	        henkou3(c, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if d < 0:
	        henkou3(d, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if e < 0:
	        henkou3(e, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if f < 0:
	        henkou3(f, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if g < 0:
	        henkou2(g, a, wasitunet, b, gentei, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if h < 0:
	        henkou2(h, a, wasitunet, b, gentei, g, ANA, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if i < 0:
	        henkou2(i, a, wasitunet, b, gentei, g, ANA, h, JR51, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if j < 0:
	        henkou2(j, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, k, jyuntoku, l, toku05, n, toku01)
	    if k < 0:
	        henkou2(k, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, l, toku05, n, toku01)
	    if l < 0:
	        henkou2(l, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, n, toku01)
	    if m < 0:
	        henkou3(m, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if n < 0:
	        henkou2(n, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05)
##############ÖtF[YI¹###################
kansi2()
yoku2syu = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[1]/div[1]/ul/li[6]/a/span')
yoku2syu.click()
################################ÖtF[Y3#################################
def kansi3():
	#lðæŸ
	def getvalue(xpath, xpath2):
	    kaisya = driver.find_element_by_xpath(xpath)
	    v = kaisya.get_attribute("value")
	    if v == '':
	        kaisya3 = driver.find_element_by_xpath(xpath2)
	        v = kaisya3.text
	    try:
	        v = int(v)
	        print(v)
	        return v
	    except:
	        v = 0
	        print(v)
	        return v
	#lðÏX
	def sendkey(xpath ,v):
	    kaisya2 = driver.find_element_by_xpath(xpath)
	    kaisya2.clear()
	    kaisya2.send_keys(v)
	    
	###########»è2###################
	def henkou2(aa ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
		def hantei8(aa , gg ,gsyamei):
			def hantei7(aa , hh ,hsyamei):
				def hantei6(aa , ii ,isyamei):
					def hantei5(aa , jj ,jsyamei):
						def hantei4(aa , kk ,ksyamei):
							def hantei3(aa , ll ,lsyamei):
								def hantei2(aa ,mm ,msyamei):
									def hantei1(aa ,nn ,nsyamei):
										if nn + aa >= 0:
											nn += aa
											sendkey(nsyamei, nn)
										elif nn > 0 and nn + aa < 0:
											sendkey(nsyamei, 0)
											aa += nn
										else:
											print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
								if mm + aa >= 0:
									mm += aa
									sendkey(msyamei, mm)
								elif mm > 0 and mm + aa < 0:
									sendkey(msyamei, 0)
									aa += mm
									hantei1(aa ,nn ,nsyamei)
								else:
									hantei1(aa ,nn ,nsyamei)
							if ll + aa >= 0:
								ll += aa
								sendkey(lsyamei, ll)
							elif ll > 0 and ll + aa < 0:
								sendkey(lsyamei, 0)
								aa += ll
								hantei2(aa ,mm ,msyamei)
							else:
								hantei2(aa ,mm ,msyamei)
						if kk + aa >= 0:
							kk += aa
							sendkey(ksyamei, kk)
						elif kk > 0 and kk + aa < 0:
							sendkey(ksyamei, 0)
							aa += kk
							hantei3(aa ,ll ,lsyamei)
						else:
							hantei3(aa ,ll ,lsyamei)
					if jj + aa >= 0:
						jj += aa
						sendkey(jsyamei, jj)
					elif jj > 0 and jj + aa < 0:
						sendkey(jsyamei, 0)
						aa += jj
						hantei4(aa ,kk ,ksyamei)
					else:
						hantei4(aa ,kk ,ksyamei)
				if ii + aa >= 0:
					ii += aa
					sendkey(isyamei, ii)
				elif ii > 0 and ii + aa < 0:
					sendkey(isyamei, 0)
					aa += ii
					hantei5(aa ,jj ,jsyamei)
				else:
					hantei5(aa ,jj ,jsyamei)
			if hh + aa >= 0:
				hh += aa
				sendkey(hsyamei, hh)
			elif hh > 0 and hh + aa < 0:
				sendkey(hsyamei, 0)
				aa += hh
				hantei6(aa ,ii ,isyamei)
			else:
				hantei6(aa ,ii ,isyamei)
		if gg + aa >= 0:
			gg += aa
			sendkey(gsyamei, gg)
		elif gg > 0 and gg + aa < 0:
			sendkey(gsyamei, 0)
			aa += gg
			hantei7(aa ,hh ,hsyamei)
		else:
			hantei7(aa ,hh ,hsyamei)
	###########»è3###################
	def henkou3(aa ,ff ,fsyamei ,gg ,gsyamei ,hh , hsyamei, ii ,isyamei, jj ,jsyamei ,kk ,ksyamei ,ll ,lsyamei ,mm ,msyamei ,nn ,nsyamei ):
		def hantei9(aa , ff ,fsyamei):
			def hantei8(aa , gg ,gsyamei):
				def hantei7(aa , hh ,hsyamei):
					def hantei6(aa , ii ,isyamei):
						def hantei5(aa , jj ,jsyamei):
							def hantei4(aa , kk ,ksyamei):
								def hantei3(aa , ll ,lsyamei):
									def hantei2(aa ,mm ,msyamei):
										def hantei1(aa ,nn ,nsyamei):
											if nn + aa >= 0:
												nn += aa
												sendkey(nsyamei, nn)
											elif nn > 0 and nn + aa < 0:
												sendkey(nsyamei, 0)
												aa += nn
											else:
												print("mainasu syori dekimasen!!!!!!!!!!!!!!!!!!!!")
									if mm + aa >= 0:
										mm += aa
										sendkey(msyamei, mm)
									elif mm > 0 and mm + aa < 0:
										sendkey(msyamei, 0)
										aa += mm
										hantei1(aa ,nn ,nsyamei)
									else:
										hantei1(aa ,nn ,nsyamei)
								if ll + aa >= 0:
									ll += aa
									sendkey(lsyamei, ll)
								elif ll > 0 and ll + aa < 0:
									sendkey(lsyamei, 0)
									aa += ll
									hantei2(aa ,mm ,msyamei)
								else:
									hantei2(aa ,mm ,msyamei)
							if kk + aa >= 0:
								kk += aa
								sendkey(ksyamei, kk)
							elif kk > 0 and kk + aa < 0:
								sendkey(ksyamei, 0)
								aa += kk
								hantei3(aa ,ll ,lsyamei)
							else:
								hantei3(aa ,ll ,lsyamei)
						if jj + aa >= 0:
							jj += aa
							sendkey(jsyamei, jj)
						elif jj > 0 and jj + aa < 0:
							sendkey(jsyamei, 0)
							aa += jj
							hantei4(aa ,kk ,ksyamei)
						else:
							hantei4(aa ,kk ,ksyamei)
					if ii + aa >= 0:
						ii += aa
						sendkey(isyamei, ii)
					elif ii > 0 and ii + aa < 0:
						sendkey(isyamei, 0)
						aa += ii
						hantei5(aa ,jj ,jsyamei)
					else:
						hantei5(aa ,jj ,jsyamei)
				if hh + aa >= 0:
					hh += aa
					sendkey(hsyamei, hh)
				elif hh > 0 and hh + aa < 0:
					sendkey(hsyamei, 0)
					aa += hh
					hantei6(aa ,ii ,isyamei)
				else:
					hantei6(aa ,ii ,isyamei)
			if gg + aa >= 0:
				gg += aa
				sendkey(gsyamei, gg)
			elif gg > 0 and gg + aa < 0:
				sendkey(gsyamei, 0)
				aa += gg
				hantei7(aa ,hh ,hsyamei)
			else:
				hantei7(aa ,hh ,hsyamei)
		if ff + aa >= 0:
			ff += aa
			sendkey(fsyamei, ff)
		elif ff > 0 and ff + aa < 0:
			sendkey(fsyamei, 0)
			aa += ff
			hantei8(aa ,gg ,gsyamei)
		else:
			hantei8(aa ,gg ,gsyamei)
	        
	x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
	for z in x:
	    #aº15ô 
	    #JTB02  
	    jtb = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb2 = '//*[@id="rmType_1"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    c = getvalue(jtb, jtb2)
	    #ßEú{c[Xg 
	    kinki = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div/input'
	    kinki2 = '//*[@id="rmType_1"]/table[2]/tbody/tr[1]/td[' + z + ']/div'
	    d = getvalue(kinki, kinki2)
	    #ú{·s 
	    nihon = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div/input'
	    nihon2 = '//*[@id="rmType_1"]/table[3]/tbody/tr[1]/td[' + z + ']/div'
	    e = getvalue(nihon, nihon2)
	    #gbvcA[ 
	    top = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div/input'
	    top2 = '//*[@id="rmType_1"]/table[4]/tbody/tr[1]/td[' + z + ']/div'
	    f = getvalue(top, top2)
	    #ANA 
	    ANA = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div/input'
	    ANA2 = '//*[@id="rmType_1"]/table[5]/tbody/tr[1]/td[' + z + ']/div'
	    g = getvalue(ANA, ANA2)
	    #JRãB51 
	    JR51 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR512 = '//*[@id="rmType_1"]/table[6]/tbody/tr[1]/td[' + z + ']/div'
	    h = getvalue(JR51, JR512)
	    #JRãB52 
	    JR52 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div/input'
	    JR522 = '//*[@id="rmType_1"]/table[7]/tbody/tr[1]/td[' + z + ']/div'
	    i = getvalue(JR52, JR522)
	    #aº15ôilbgj
	    wasitunet = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    wasitunet2 = '//*[@id="netRmTypeGroup_9"]/tbody/tr[1]/td[' + z + ']/div'
	    a = getvalue(wasitunet, wasitunet2)

	    #aº15ôiAbvO[h)
	    upgrade = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    upgrade2 = '//*[@id="netRmTypeGroup_12"]/tbody/tr[1]/td[' + z + ']/div'
	    j = getvalue(upgrade,upgrade2)

	    #aº15ôi1ú3®Àèj
	    gentei = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    gentei2 = '//*[@id="netRmTypeGroup_13"]/tbody/tr[1]/td[' + z + ']/div'
	    b = getvalue(gentei, gentei2)

	    #ÁÊº(06) 
	    jyuntoku = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    jyuntoku2 = '//*[@id="netRmTypeGroup_2"]/tbody/tr[1]/td[' + z + ']/div'
	    k = getvalue(jyuntoku, jyuntoku2)

	    #ÁÊº(05)
	    #JTB01 
	    jtb01 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div/input'
	    jtb012 = '//*[@id="rmType_3"]/table[1]/tbody/tr[1]/td[' + z + ']/div'
	    m = getvalue(jtb01, jtb012)
	    #ÁÊº(05lbg) 
	    toku05 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku052 = '//*[@id="netRmTypeGroup_3"]/tbody/tr[1]/td[' + z + ']/div'
	    l = getvalue(toku05, toku052)
	    #ÁÊº(01lbg) 
	    toku01 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div/input[1]'
	    toku012 = '//*[@id="netRmTypeGroup_4"]/tbody/tr[1]/td[' + z + ']/div'
	    n = getvalue(toku01, toku012)
	    print ("tuginohihe")

	    #a, wasitunet, b, gentei, c, jtb, d, kinki, e, nihon, f, top, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, m, jtb01, n, toku01)
	    if a < 0:
	        henkou2(a, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
            
	    if b < 0:
	        henkou2(b, a, wasitunet, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if c < 0:
	        henkou3(c, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if d < 0:
	        henkou3(d, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if e < 0:
	        henkou3(e, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if f < 0:
	        henkou3(f, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if g < 0:
	        henkou2(g, a, wasitunet, b, gentei, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if h < 0:
	        henkou2(h, a, wasitunet, b, gentei, g, ANA, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if i < 0:
	        henkou2(i, a, wasitunet, b, gentei, g, ANA, h, JR51, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if j < 0:
	        henkou2(j, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, k, jyuntoku, l, toku05, n, toku01)
	    if k < 0:
	        henkou2(k, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, l, toku05, n, toku01)
	    if l < 0:
	        henkou2(l, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, n, toku01)
	    if m < 0:
	        henkou3(m, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05, n, toku01)
	    if n < 0:
	        henkou2(n, a, wasitunet, b, gentei, g, ANA, h, JR51, i, JR52, j, upgrade, k, jyuntoku, l, toku05)
##############ÖtF[YI¹###################
for zz in range(5):
	kansi3()
	yoku2syu = driver.find_element_by_xpath('//*[@id="dataHeaderInner"]/div[1]/div[1]/ul/li[6]/a/span')
	yoku2syu.click()
