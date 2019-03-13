#_author:"Phoebe Li"
#date:2018/9/19
#_author:"Phoebe Li"
#date:2018/8/28
from selenium import webdriver

import time
import unittest

class TPC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://tvuservice.tvunetworks.com/tvuuserservice/?url=http://tpc.tvunetworks.com:8080/tpc&serviceName=Tvu%20Pack%20Control")
        cls.driver.implicitly_wait(30)
        cls.driver.find_element_by_id("username").send_keys("phoebeli@tvunetworks.com")
        cls.driver.find_element_by_id("password").send_keys("123456")
        cls.driver.find_element_by_id("validationCode").send_keys("1234")
        cls.driver.find_element_by_id("sign-in").click()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def change_pageset(self):
    #     iframe = self.driver.find_element_by_xpath("//iframe[contains(@src,'home')]")
    #     self.driver.switch_to_frame(iframe)
    #     select = self.driver.find_element_by_id("pageSize")
    #     select.find_element_by_xpath("//option[@value='10']").click()

    def search(self, keywords):
        '''这里写了一个搜索的方法'''
        iframe = self.driver.find_element_by_xpath("//iframe[contains(@src,'home')]")
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_id("searchFilterValue").send_keys(keywords)
        self.driver.find_element_by_xpath("//*[contains(@class,'se3')]").click()
    # def is_login_success(self):
    #     '''判断是否获取到登录账号名称'''
    #     try:
    #         text = self.driver.find_element_by_id("emailId").text
    #         print(text)
    #         return True
    #     except:
    #         return False
    def is_search_success(self):
        r = self.driver.find_elements_by_xpath("//table[@id='rinfo_tab']/tbody/tr/td[1]")
        t = self.driver.find_elements_by_xpath("//table[@id='tinfo_tab']/tbody/tr/td[1]")
        result = t + r
        list = []
        for i in result:
            list.append(i.text)
        print(list)
        return list

    def check_pairR(self):
        self.driver.find_element_by_xpath("//table[@id='tinfo_tab']/tbody/tr[2]/td[1]").click()
        Rlist = self.driver.find_elements_by_xpath("//table[@id='rightRList']/tbody/tr/td[1]")
        PairRlist = []
        for i in Rlist:
            PairRlist.append(i.text)
        print(PairRlist)
        return PairRlist

    def search_pairR(self):
        Rlist = self.driver.find_elements_by_xpath("//table[@id='rinfo_tab']/tbody/tr/td[1]")
        SearchPairR = []
        for i in Rlist:
            SearchPairR.append(i.text)
        return SearchPairR


    def is_search_successR(self):
        try:
            text = self.driver.find_element_by_xpath("//table[@id='rinfo_tab']/tbody/tr[3]/td[1]/div/a[1]").text
            print(text)
            return True
        except:
            return False
    # def test_search_ExistedRealR(self):
    #     self.search("0806")
    #     result = self.is_search_successR()
    #     self.assertTrue(result)

    # def test_search_PartofPID(self):
    #     self.search("0806")
    #     self.is_search_success()
    #     a = "0806"
    #     b = self.is_search_success()
    #     assert a in str(b)

    def test_search_WholeR(self):
        self.search("734dc413e1280806")
        self.is_search_success()
        a = "734dc413e1280806"
        b = self.is_search_success()
        assert a in str(b)

    # def test_search_ResultOnly(self):
    #     self.change_pageset()
    #     self.search("3ff1")
    #     a = self.search_pairR()
    #     b = self.check_pairR()
    #     self.assertCountEqual(a,b)




if __name__ == "__main__":
    unittest.main()