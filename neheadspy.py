# -*- coding: utf-8 -*-
import json
import time

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib3 import encode_multipart_formdata

from checkChrome import check_update_chromedriver, deffstr
from csdir import *
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://gswp.jszygs.com'
cookieurl = "https://gswp.jszygs.com/v6/rdmCode?d="
RdmCodeurl = "https://gswp.jszygs.com/v6/rdmCode?method=getRdmCode"
salturl = "https://gswp.jszygs.com/v6/rdmCode?method=getSalt"
loginurl = "https://gswp.jszygs.com/v6/j_bsp_security_check/"
homepage = "https://gswp.jszygs.com/portal/portal/appCenterInitCmd.cmd?method=queryPageInit&menuId=menuMap"
sytffx = "https://gswp.jszygs.com/imr/pc/supplyv3.cmd?method=getComSupplyAnalysisMainPageData&flag=2"
styffxpage = "https://gswp.jszygs.com/imr/pc/supplyv3.cmd?method=comSupplyAnalysisMainPage&_protocol=https"
cslists = "11320101,11320201"
pplist = "6901028301695"
date = "20220408"
isMaxCount = ""
searchMode = "company"
jd = 25

rowlength = 0
sf_xlist = []
cs_xlist = []
# 软九五
rjw_tfm_xlist = []
rjw_jhm_xlist = []
rjw_dzl_xlist = []
rjw_dzmx_xlist = []
rjw_ddmzl_xlist = []
rjw_dwdds_xlist = []
rjw_dddw_xlist = []
rjw_fdwqk_xlist = []
# 细九五
xjw_tfm_xlist = []
xjw_jhm_xlist = []
xjw_dzl_xlist = []
xjw_dzmx_xlist = []
xjw_ddmzl_xlist = []
xjw_dwdds_xlist = []
xjw_dddw_xlist = []
xjw_fdwqk_xlist = []
# 雨花石
yhs_tfm_xlist = []
yhs_jhm_xlist = []
yhs_dzl_xlist = []
yhs_dzmx_xlist = []
yhs_ddmzl_xlist = []
yhs_dwdds_xlist = []
yhs_dddw_xlist = []
yhs_fdwqk_xlist = []

# spydate=input("请输入所需要爬数据的日期（eg:20201201）：")

file_path = ".\\"

check_update_chromedriver(file_path)

s = Service("chromedriver.exe")
window = webdriver.Chrome(service=s)

window.get(url)
time.sleep(2)
# # 点击账号登录


try:
    account_login_button = window.find_element(By.ID, 'frm-ok')
    account_login_button.click()
    # 输入账号
    input_account = window.find_element(By.ID, 'j_username')
    input_account.send_keys('jhccx')
    # 输入密码
    input_password = window.find_element(By.ID, 'j_password')
    input_password.send_keys('Jhccx123456')
    # 点击登录按钮
    login_button = window.find_element(By.ID, 'frm-ok')
    login_button.click()

    # # 在新窗口打开商业投放分析页面
    # time.sleep(1)
    # js = "window.open('"+styffxpage+"')"
    # window.execute_script(js)
    #
    # cc = window.get_cookies()
    # # cookie = 'JSESSIONID=40BAD916482CE6A82081058641EDBE7C; skin=wuko; mtMenuStyle=fixed; j_username=jhccx; idp_ls=SkhDQ1g%3D; v6u="SkhDQ1gj6K6h5YiS5aSE5p+l6K+iIzAxMDAyOTM="; isAdmin=false; v6uba=SkhDQ1h8fDIwMzIwMDAxfHw2NzA4LDYw; b_t_s=t472658981981x; v6sysfont=reset; sso_token=DD2E4E5F9564602246708004E23D2263'
    # cookie = 'skin=wuko; mtMenuStyle=fixed; j_username=jhccx; idp_ls=SkhDQ1g%3D; v6u="SkhDQ1gj6K6h5YiS5aSE5p+l6K+iIzAxMDAyOTM="; isAdmin=false; v6uba=SkhDQ1h8fDIwMzIwMDAxfHw2NzA4LDYw; b_t_s=t472658981981x; v6sysfont=reset;'
    #
    # for c in window.get_cookies():
    #     if c.get('name') == 'JSESSIONID':
    #         cookie += c.get('name') + '=' + c.get('value')+';'
    #     if c.get('name') == 'sso_token':
    #         cookie += c.get('name') + '=' + c.get('value')+';'
    # aa = window.get_cookies()
    #
    # d = {"date": "20230102",
    #      "com_idSearch": "11320101",
    #      "pack_barSearch": "6901028111355,6901028062015",
    #      "icompanysMaxCount": "",
    #      "searchMode": "company"}
    # datajson = json.loads(str(d).replace("'", "\""))
    # header = {"Content-Type": "multipart/form-data; boundary=<calculated when request is sent>","Content-Length":"<calculated when request is sent>","Cookie" :cookie}
    # # r = requests.post('https://gswp.jszygs.com/imr/pc/supplyv3.cmd?method=getComSupplyAnalysisMainPageData&flag=2',
    # #                   data=datajson, cookies=cookie)
    # encode_data = encode_multipart_formdata(d)
    # data = encode_data[0]
    # header['Content-Type'] = encode_data[1]
    # res = requests.post(url='https://gswp.jszygs.com/imr/pc/supplyv3.cmd?method=getComSupplyAnalysisMainPageData&flag=2', headers=header, data=data)
    # print(json.loads(res.content.decode('utf-8')))


    # 在新窗口打开商业投放分析页面
    time.sleep(1)
    js = "window.open('"+styffxpage+"')"
    window.execute_script(js)
    ws = window.window_handles
    time.sleep(2)
    window.switch_to.window(ws[0])
    time.sleep(2)
    window.switch_to.window(ws[1])
    time.sleep(3)

    # 选中所有区域
    # window.find_element(By.ID,'treeSpan2').click()
    # time.sleep(5)
    # cslist = window.find_element(By.ID,'comTree2_1_check')
    # cslist.click()
    # time.sleep(5)
    # # 打开规格的tree
    # window.find_element(By.ID,'itemTreeSpan2').click()
    # time.sleep(1)
    # window.find_element(By.ID,'itemTree2_2_switch').click()
    # time.sleep(1)
    # window.find_element(By.ID,'itemTree2_16_switch').click()
    # time.sleep(1)
    # # 选中 三种烟
    # window.find_element(By.ID,'itemTree2_18').click()
    # window.find_element(By.ID,'itemTree2_19').click()
    # window.find_element(By.ID,'itemTree2_20').click()
    # window.find_element(By.ID,'itemTree2_23').click()
    # window.find_element(By.ID,'itemTreeSpan2').click()
    time.sleep(1)
    cs_value = "document.getElementsByName('com_idSearch2')[0].value='{}'" .format("11320101,11320201,11320301,11320401,11320501,11320601,11320701,11320801,11320901,11321001,11321101,11321201,11321301,11340101,11340201,11340301,11340401,11340501,11340601,11340701,11340801,11341001,11341101,11341201,11341301,11341501,11341601,11341701,11341801,11410101,11410201,11410301,11410401,11410501,11410601,11410701,11410801,11410809,11410901,11411001,11411101,11411201,11411301,11411401,11411501,11411601,11411701,11370101,11370201,11370301,11370401,11370501,11370601,11370701,11370801,11370901,11371001,11371101,11371201,11371301,11371401,11371501,11371601,11371701,11110001,11120101,11120102,11120103,11120104,11120105,11120106,11120107,11120108,11120109,11120110,11120111,11120112,11120113,11120201,11120202,11120203,11130101,11130201,11130301,11130401,11130501,11130601,11130701,11130801,11130901,11131001,11131101,11131201,11140101,11140201,11140301,11140401,11140501,11140601,11140701,11140801,11140901,11141001,11142301,11130715,11150101,11150201,11150301,11150401,11150501,11150601,11150701,11150709,11152201,11152502,11152601,11152801,11152901,11230101,11230201,11230301,11230401,11230501,11230601,11230701,11230801,11230901,11231001,11231003,11231101,11231201,11232704,11220101,11220201,11220301,11220401,11220501,11220601,11220701,11220801,11222401,11210101,11210301,11210401,11210501,11210601,11210701,11210801,11210901,11211001,11211101,11211201,11211301,11211401,11210201,11620101,11620201,11620301,11620401,11620501,11620601,11620701,11620801,11620901,11620902,11621001,11622401,11622601,11622901,11623001,11640101,11640201,11640301,11640307,11640401,11610101,11610201,11610301,11610401,11610413,11610501,11610601,11610701,11610801,11610901,11611001,11630101,11632101,11632201,11632301,11632501,11632601,11632701,11632801,11632802,11540100,11542101,11542201,11542301,11542401,11542501,11542601,11650101,11650201,11652101,11652201,11652301,11652701,11652801,11652901,11653101,11653201,11654001,11654201,11654301,11659001,11310101,11310103,11310104,11310105,11310106,11310107,11310108,11310109,11310110,11310111,11310112,11310113,11310114,11310115,11310116,11310118,11310119,11310120,11310201,22310101,22310102,11330101,11330201,11330301,11330401,11330501,11330601,11330701,11330801,11330901,11331001,11331101,11350101,11350201,11350301,11350401,11350501,11350601,11350701,11350801,11350901,11440101,11440201,11440401,11440501,11440601,11440701,11440801,11440901,11441201,11441301,11441401,11441501,11441601,11441701,11441801,11441901,11442001,11445101,11445201,11445301,11440302,11440303,11440304,11440305,11440306,11440307,11440311,11440312,11440313,11440314,11440315,11440316,11450101,11450201,11450301,11450401,11450501,11450603,11450701,11450801,11450901,11451001,11451101,11451201,11451301,11451401,11460101,11460201,11469005,11469011,11360101,11360201,11360301,11360401,11360501,11360601,11360701,11360801,11360901,11361001,11361101,11430101,11430201,11430301,11430401,11430501,11430601,11430701,11430801,11430901,11431001,11431101,11431201,11431301,11433101,11420101,11420201,11420301,11420501,11420601,11420701,11420801,11420901,11421001,11421101,11421201,11421301,11422801,11429001,11429002,11429003,11429004,11510101,11510301,11510401,11510501,11510601,11510701,11510801,11510901,11511001,11511101,11511301,11511401,11511501,11511601,11511701,11511801,11511901,11512001,11513201,11513301,11513401,11500001,11530101,11530301,11530401,11530501,11530601,11530701,11532301,11532501,11532601,11532701,11532801,11532901,11533101,11533301,11533401,11533501,11520102,11520201,11520301,11520401,11520501,11522201,11522301,11522401,11522601,11522701")
    window.execute_script(cs_value)
    gg_value = "document.getElementsByName('pack_barSearch2')[0].value='{}'" .format("6901028301695,6901028112987")
    window.execute_script(gg_value)
    date_value = "document.getElementById('date').value='{}'" .format("20230103")
    window.execute_script(date_value)
    # 全选
    window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[2]').click()
    # 反选
    window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[2]').click()

    #选中所需要的
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[18]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[19]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[20]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[21]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[24]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[25]').click()
    window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[26]').click()
    # window.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/div/div/label[27]').click()

    # 点击搜索并等待表格加载
    searchButton = window.find_element(By.ID,'search-btn').click()
    element=WebDriverWait(window, 20).until(lambda driver:driver.find_element(By.ID,"area-table_wrapper"))

    lists = window.find_element(By.XPATH,'//*[@id="area-table"]/tbody[1]/tr[1]/td[1]')
    table = window.find_element(By.TAG_NAME,'tbody')
    rows = table.find_elements(By.TAG_NAME,'tr')
    for row in rows:
        data = row.text
        my_list = data.split(' ')
        if len(my_list) >= 6:

            if my_list[4] != '-':
                gg1list = my_list[4].split(',')
                gg1d = gg1list[-1]
                gg1 = int(gg1d)
                if gg1 >= jd:
                    print(my_list[1] + "第一个规格不符合档位")
            if my_list[5] != '-':
                gg2list = my_list[5].split(',')
                gg2d = gg1list[-1]
                gg2 = int(gg2d)
                if gg2 >= jd:
                    print(my_list[1] + "第二个规格不符合档位")
        # gg3 = my_list[6]
        # gg4 = my_list[7]
        # if my_list[4] != '-':
        #     djlist = my_list[4].split(' ')
        #     leng = djlist - 1
        #     if djlist[leng] >= jd:
        #         print(my_list[2] + "软九五不符合")
        # if my_list[5] != '-':
        #     djlist = my_list[5].split(' ')
        #     if djlist[leng] >= jd:
        #         print(my_list[2] + "软九五不符合")
        print(data)
    # for index in range(1,len(rows)):
    #     # 省份
    #     sfxpath= '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[2]'
    #     # 城市
    #     csxpath= '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[3]'
    #     # 软九五
    #     rjwtfmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[5]'
    #     rjwjhmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[6]'
    #     rjwdzlxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[7]'
    #     rjwdzmxxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[8]'
    #     rjwddmzlxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[9]'
    #     rjwdwddsxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[10]'
    #     rjwdddwxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[11]'
    #     rjwfdwqkxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[12]'
    #     # 细九五
    #     xjwtfmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[13]'
    #     xjwjhmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[14]'
    #     xjwdzlxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[15]'
    #     xjwdzmxxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[16]'
    #     xjwddmzlxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[17]'
    #     xjwdwddsxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[18]'
    #     xjwdddwxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[19]'
    #     xjwfdwqkxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[20]'
    #     # 雨花石
    #     yhstfmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[21]'
    #     yhsjhmxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[22]'
    #     yhsdzlxpath   = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[23]'
    #     yhsdzmxxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[24]'
    #     yhsddmzlxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[25]'
    #     yhsdwddsxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[26]'
    #     yhsdddwxpath  = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[27]'
    #     yhsfdwqkxpath = '//*[@id="area-table"]/tbody[1]/tr['+str(index)+']/td[28]'
    #
    #     sf_xlist.append(sf[window.find_element(By.XPATH,sfxpath).text])
    #     cs_xlist.append(cs[window.find_element(By.XPATH,csxpath).text])
    #
    #     rjw_tfm_xlist.append(window.find_element(By.XPATH,rjwtfmxpath).text)
    #     rjw_jhm_xlist.append(window.find_element(By.XPATH,rjwjhmxpath).text)
    #     rjw_dzl_xlist.append(window.find_element(By.XPATH,rjwdzlxpath).text)
    #     rjw_dzmx_xlist.append(window.find_element(By.XPATH,rjwdzmxxpath).text)
    #     rjw_ddmzl_xlist.append(window.find_element(By.XPATH,rjwddmzlxpath).text)
    #     rjw_dwdds_xlist.append(window.find_element(By.XPATH,rjwdwddsxpath).text)
    #     rjw_dddw_xlist.append(window.find_element(By.XPATH,rjwdddwxpath).text)
    #     rjw_fdwqk_xlist.append(window.find_element(By.XPATH,rjwfdwqkxpath))
    #
    #     xjw_tfm_xlist.append(window.find_element(By.XPATH,xjwtfmxpath).text)
    #     xjw_jhm_xlist.append(window.find_element(By.XPATH,xjwjhmxpath).text)
    #     xjw_dzl_xlist.append(window.find_element(By.XPATH,xjwdzlxpath).text)
    #     xjw_dzmx_xlist.append(window.find_element(By.XPATH,xjwdzmxxpath).text)
    #     xjw_ddmzl_xlist.append(window.find_element(By.XPATH,xjwddmzlxpath).text)
    #     xjw_dwdds_xlist.append(window.find_element(By.XPATH,xjwdwddsxpath).text)
    #     xjw_dddw_xlist.append(window.find_element(By.XPATH,xjwdddwxpath).text)
    #     xjw_fdwqk_xlist.append(window.find_element(By.XPATH,xjwfdwqkxpath))
    #
    #     yhs_tfm_xlist.append(window.find_element(By.XPATH,yhstfmxpath).text)
    #     yhs_jhm_xlist.append(window.find_element(By.XPATH,yhsjhmxpath).text)
    #     yhs_dzl_xlist.append(window.find_element(By.XPATH,yhsdzlxpath).text)
    #     yhs_dzmx_xlist.append(window.find_element(By.XPATH,yhsdzmxxpath).text)
    #     yhs_ddmzl_xlist.append(window.find_element(By.XPATH,yhsddmzlxpath).text)
    #     yhs_dwdds_xlist.append(window.find_element(By.XPATH,yhsdwddsxpath).text)
    #     yhs_dddw_xlist.append(window.find_element(By.XPATH,yhsdddwxpath).text)
    #     yhs_fdwqk_xlist.append(window.find_element(By.XPATH,yhsfdwqkxpath).text)
    #
    #     print(len(rjw_tfm_xlist))
    # f=open(spydate+".csv","w")
    # for index in range(len(rjw_tfm_xlist)):
    #     f.write("6901028301695"+","+spydate+","+sf_xlist[index]+","+cs_xlist[index]+","+deffstr(str(rjw_tfm_xlist[index]))+","+deffstr(str(rjw_jhm_xlist[index]))+","+deffstr(str(rjw_dzl_xlist[index]))+","+deffstr(str(rjw_dzmx_xlist[index]))+","+deffstr(str(rjw_ddmzl_xlist[index]))+","+deffstr(str(rjw_dwdds_xlist[index]))+","+'"'+deffstr(str(rjw_dddw_xlist[index]))+'"'+'\n')
    # for index in range(len(xjw_tfm_xlist)):
    #     f.write("6901028112987"+","+spydate+","+sf_xlist[index]+","+cs_xlist[index]+","+deffstr(str(xjw_tfm_xlist[index]))+","+deffstr(str(xjw_jhm_xlist[index]))+","+deffstr(str(xjw_dzl_xlist[index]))+","+deffstr(str(xjw_dzmx_xlist[index]))+","+deffstr(str(xjw_ddmzl_xlist[index]))+","+deffstr(str(xjw_dwdds_xlist[index]))+","+'"'+deffstr(str(xjw_dddw_xlist[index]))+'"'+'\n')
    # for index in range(len(yhs_tfm_xlist)):
    #     f.write("6901028111546"+","+spydate+","+sf_xlist[index]+","+cs_xlist[index]+","+deffstr(str(yhs_tfm_xlist[index]))+","+deffstr(str(yhs_jhm_xlist[index]))+","+deffstr(str(yhs_dzl_xlist[index]))+","+deffstr(str(yhs_dzmx_xlist[index]))+","+deffstr(str(yhs_ddmzl_xlist[index]))+","+deffstr(str(yhs_dwdds_xlist[index]))+","+'"'+deffstr(str(yhs_dddw_xlist[index]))+'"'+'\n')
    # f.close()

except Exception as r:
    print(r)

ws = window.window_handles
time.sleep(2)
window.switch_to.window(ws[0])
exit_button = window.find_element(By.CLASS_NAME, 'logout')
exit_button.click()
window.quit()
