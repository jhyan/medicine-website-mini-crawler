from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

FILE_NAME = 'medicalNews.txt'
URL = 'https://www.cmde.org.cn/CL0004/'
DRIVER_PATH = "/Users/jiahan/PycharmProjects/medicine_crawler/chromedriver"

class Crawler(object):

    def __init__(self, url):
        '''
        Some websites are banning selenium by checking a variable window.navigator.webdriver.
        In order to walk around that, we exclude the automation switch in the driver.
        More details in https://juejin.im/post/5c62b6d5f265da2dab17ae3c.
        '''
        self.url = url
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.driver = Chrome(options = self.option, executable_path = DRIVER_PATH)

    def save_pagesource(self):
        self.driver.get(self.url)
        with open(FILE_NAME, 'w') as fp:
            fp.write(self.driver.page_source.encode('utf-8', 'ignore'))
        print "finish writing"

    def quit(self):
        self.driver.quit()

if __name__ == '__main__':
    crawler = Crawler(URL)
    crawler.save_pagesource()
    crawler.quit()


### backup codes
## wait methods
# self.driver.implicitly_wait(10)
# WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "ListColumnClass5")))
# print self.driver.find_element(By.CLASS_NAME, 'ListColumnClass5')

## other imports
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC