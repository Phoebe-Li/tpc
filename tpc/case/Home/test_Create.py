#_author:"Phoebe Li"
#date:2018/9/19
#_author:"Phoebe Li"
#date:2018/9/17

from selenium import webdriver

import time
import unittest


class TPC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(
            "http://tvuservice.tvunetworks.com/tvuuserservice/?url=http://tpc.tvunetworks.com:8080/tpc&serviceName=Tvu%20Pack%20Control")
        cls.driver.implicitly_wait(5)
        cls.driver.find_element_by_id("username").send_keys("phoebeli@tvunetworks.com")
        cls.driver.find_element_by_id("password").send_keys("123456")
        cls.driver.find_element_by_id("validationCode").send_keys("1234")
        cls.driver.find_element_by_id("sign-in").click()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        iframe = cls.driver.find_element_by_xpath("//iframe[contains(@src,'home')]")
        cls.driver.switch_to_frame(iframe)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def CreateT(self,TId,TName):
        create = self.driver.find_element_by_xpath("//*[contains(@value,'Create')]")
        create.click()
        self.driver.find_element_by_id("createTId").send_keys(TId)
        self.driver.find_element_by_id("createTName").send_keys(TName)
        self.driver.find_element_by_id("createTCardNo").send_keys("8")
        self.driver.find_element_by_xpath("//div[@id='createTdiv']/div[3]/input").click()
        time.sleep(3)

    def CreateTfailed(self,Tid,Tname):
        '''创建失败后再创建'''
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='errorDiv']/div[1]/div[2]").click()
        self.driver.find_element_by_id("createTId").clear()
        self.driver.find_element_by_id("createTId").send_keys(Tid)
        self.driver.find_element_by_id("createTName").clear()
        self.driver.find_element_by_id("createTName").send_keys(Tname)
        self.driver.find_element_by_xpath("//div[@id='createTdiv']/div[3]/input").click()

    def CreateR(self,RId,RName):
        create = self.driver.find_element_by_xpath("//*[contains(@value,'Create')]")
        create.click()
        select = self.driver.find_element_by_id("createType")
        select.find_element_by_xpath("//option[@value='R']").click()
        self.driver.find_element_by_xpath("//*[contains(@id, 'createRId')]").send_keys(RId)
        self.driver.find_element_by_id("createRName").send_keys(RName)
        self.driver.find_element_by_xpath("//div[@id='createRdiv']/div[5]/input").click()
        time.sleep(5)

    def CreateRfailed(self,Rid,Rname):
        '''创建失败后再创建'''
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='errorDiv']/div[1]/div[2]").click()
        self.driver.find_element_by_xpath("//*[contains(@id, 'createRId')]").clear()
        self.driver.find_element_by_xpath("//*[contains(@id, 'createRId')]").send_keys(Rid)
        self.driver.find_element_by_id("createRName").clear()
        self.driver.find_element_by_id("createRName").send_keys(Rname)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@id='createRdiv']/div[5]/input").click()

    def Search(self, keywords):
        self.driver.find_element_by_id("searchFilterValue").clear()
        self.driver.find_element_by_id("searchFilterValue").send_keys(keywords)
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[contains(@class,'se3')]").click()

    def FailedResult(self):
        '''判断是否提示created failed'''
        try:
            text = self.driver.find_element_by_xpath("//*[@id='errorMessageDiv']/ul/li/span").text
            print(text)
            return True
        except:
            return False

    def test_createT01(self):
        self.CreateT("abcde98765432203","phoebe-T203")
        self.Search("abcde98765432203")
        time.sleep(3)
        result = self.driver.find_element_by_xpath("//*[@id='tinfo_tab']/tbody/tr[2]/td[1]/div/a").text
        a = "abcde98765432203"
        self.assertEqual(result,a)
        time.sleep(3)

    def test_createT02(self):
        self.CreateT("abcde98765432203","phoebe-T203")
        time.sleep(2)
        self.CreateTfailed("abcde98765432204","phoebe-T204")
        time.sleep(2)
        self.Search("abcde98765432204")
        time.sleep(3)
        result = self.driver.find_element_by_xpath("//*[@id='tinfo_tab']/tbody/tr[2]/td[1]/div/a").text
        a = "abcde98765432204"
        self.assertEqual(result,a)
        time.sleep(3)


    def test_createR01(self):
        self.CreateR("abcde98765432103", "phoebe-103")
        self.Search("abcde98765432103")
        time.sleep(5)
        result = self.driver.find_element_by_xpath("//*[@id='rinfo_tab']/tbody/tr[2]/td[1]/div/a").text
        c = "abcde98765432103"
        self.assertEqual(result,c)
        time.sleep(3)

    def test_createR02(self):
        self.CreateR("abcde98765432103", "phoebe-103")
        time.sleep(2)
        self.CreateRfailed("abcde98765432105", "phoebe-105")
        time.sleep(2)
        self.Search("abcde98765432105")
        time.sleep(3)
        result = self.driver.find_element_by_xpath("//*[@id='rinfo_tab']/tbody/tr[2]/td[1]/div/a").text
        f = "abcde98765432105"
        self.assertEqual(result,f)
        time.sleep(3)



if __name__ == "__main__":
    unittest.main()


