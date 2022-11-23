#AUTHOR: GUSTAVO AZUAGA

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, time, re
import time
import os
from datetime import datetime

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_untitled_test_case(self):

        #Driver instance
        global driver, now
        now=datetime.now()
        driver = self.driver
        portal="https://techwithtim.net"
        print("\n"+str(now)+": Triggering selenium webdriver...")
        print("\n"+str(now)+": Opening portal: "+portal+"Please wait a moment...")
        driver.get(portal)

        def sections():

            #Sections
            section1="Tutorials"
            section2="Community"
            section3="ProgrammingExpert"
            section4="Python Programming"
            section5="Game Development With Python"
            section6="Python Neural Networks"
            sections_array = [section1, section2, section3, section4, section5, section6]
            #Portal
            portal="https://techwithtim.net"
            print("\n"+str(now)+": Displaying portal: "+portal)
            print("\n"+str(now)+": Waiting for 3 seconds...")
            driver.implicitly_wait(3)
            print("\n"+str(now)+": Navigating through some sections...")
            for section in sections_array:

                link=driver.find_element_by_link_text(section)
                link.click()
                print("\n"+str(now)+": Clicked on : "+section)
                print("\n"+str(now)+": Taking snapshot and saving to: ", os.getcwd()+" ...")
                replace_space=section.replace(" ", "_")
                driver.save_screenshot(str(now)+"_"+replace_space+"_snapshot.png")
                print("\n"+str(now)+": Waiting for 3 seconds...")
                print("\n"+str(now)+": Going back to previous page")
                driver.back()
                print("\n"+str(now)+": Waiting for 3 seconds...")
                driver.implicitly_wait(3)

            def re_run_test():

                re_test=input("\n"+str(now)+": Do you want to re-run the test? y/n: ")
                if re_test == "y":
                    driver.back()
                    print("\n"+str(now)+": Waiting for 3 seconds to get back and re-run test...")
                    driver.implicitly_wait(3)
                    return sections()
                if re_test == "n":
                    input("\n"+str(now)+": Terminating the driver session...")
                    driver.close()
                else:
                    print("\n"+str(now)+": Please input either 'y' or 'n'. ")
                    return re_run_test()
            re_run_test()

        sections()

if __name__ == "__main__":
    unittest.main()

