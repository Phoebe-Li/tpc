#_author:"Phoebe Li"
#date:2018/9/19
#_author:"Phoebe Li"
#date:2018/9/6
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

    def Click(self, keywords):
        self.driver.find_element_by_id("searchFilterValue").clear()
        self.driver.find_element_by_id("searchFilterValue").send_keys(keywords)
        self.driver.find_element_by_xpath("//*[contains(@class,'se3')]").click()

    def AddRforT(self,keywords):
        self.driver.find_element_by_xpath("//table[@id='tinfo_tab']/tbody/tr[2]/td[1]/div/a").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='filterRValue']").send_keys(keywords)
        time.sleep(5)
        self.driver.find_element_by_xpath("//form[@id='pairTInfoForm']/div[2]/input").click()
        self.driver.find_element_by_xpath("//*[@id='leftRList']/tbody/tr[1]/td[1]").click()
        self.driver.find_element_by_id("tCopy").click()
        self.driver.find_element_by_id("savePairTButton").click()

    def AddTforR(self,Tkeywords):
        self.driver.find_element_by_xpath("//table[@id='rinfo_tab']/tbody/tr[2]/td[1]/div/a").click()
        self.driver.find_element_by_xpath("//*[@id='filterTValue']").send_keys(Tkeywords)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(
            "//input[@id='filterTValue']/parent::div/following-sibling::div/input[@class='button']").click()
        self.driver.find_element_by_xpath("//*[@id='leftTList']/tbody/tr[1]/td[1]").click()
        self.driver.find_element_by_id("rCopy").click()
        self.driver.find_element_by_id("savePairRButton").click()

    def CheckTResults(self):
        Rlist = self.driver.find_elements_by_xpath("//table[@id='rightRList']/tbody/tr/td[1]")
        PairRlist = []
        for i in Rlist:
            PairRlist.append(i.text)
        print(PairRlist)
        return PairRlist

    def CheckRResults(self):
        TList = self.driver.find_elements_by_xpath("//table[@id='rightTList']/tbody/tr/td[1]")
        PairTList = []
        for i in TList:
            PairTList.append(i.text)
        print(PairTList)
        return PairTList

    def test_AddPairfort(self):
        time.sleep(2)
        self.Click("3ff1")
        self.AddRforT("ea0d0e0c0bd199")
        b = self.CheckTResults()
        a = "ea0d0e0c0bd199"
        print("1111")
        assert a in str(b)

    def test_AddPairforR(self):
        self.Click("0806")
        self.AddTforR("bb1f4e7d3bd508")
        c = self.CheckRResults()
        d = "bb1f4e7d3bd508"
        print("2222")
        assert d in str(c)


if __name__ == "__main__":
    unittest.main()
