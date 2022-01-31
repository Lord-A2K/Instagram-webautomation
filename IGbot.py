from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()  
chrome_options.add_argument("--headless")  

class IGbot:
    def __init__(self, username, password):
        self.user = username
        self.password = password
        self.driver = webdriver.Chrome()

    def exit(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        
        usernameElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        usernameElement.clear()
        usernameElement.send_keys(self.user)
        
        passwordElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        passwordElement.clear()
        passwordElement.send_keys(self.password)
        
        loginElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]")
        loginElement.click()
        time.sleep(4)
        
        
        # optional
        
        # saveInfoNotNowElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        # saveInfoNotNowElement.click()
        # time.sleep(2)
        
        # notificationNotNowElement = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        # notificationNotNowElement.click()
    def gotoMain(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)

    def search(self, tag):
        driver = self.driver
        # method 1
        driver.get("https://www.instagram.com/explore/tags/" + tag + "/")
        time.sleep(4)
        postElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]")
        postElement.click()
        while 1:
            try:    
                firstComentElement = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div/div[3]/div[1]/ul/ul[1]/div/li/div/div[1]/div[2]/h3/div")
                print(firstComentElement.get_attribute("innerHTML").splitlines()[0])
                break
            except:
                continue
        # method 2
        # searchElement = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        # searchElement.clear()
        # searchElement.send_keys(tag)
        # time.sleep(4)

        # firstElement = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div")
        # firstElement.click()
        # postElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]")
        # print(postElement.is_displayed())
    def like(self, number):
        driver = self.driver
        for i in range(1, 4):
            for j in range(1, 4):
                postElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[%d]/div[%d]"%(i, j))
                postElement.click()
                time.sleep(2)

                likeElement = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                likeElement.click()
                time.sleep(2)

                xElement = driver.find_element_by_xpath("/html/body/div[4]/div[3]/button/div")
                xElement.click()
                time.sleep(1)

        number -= 9
        number = int(number / 3)
        for i in range(1, number + 1):
            for j in range(1, 4):
                postElement = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div/div[%d]/div[%d]"%(i, j))
                postElement.click()
                time.sleep(2)

                likeElement = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                likeElement.click()
                time.sleep(2)

                xElement = driver.find_element_by_xpath("/html/body/div[4]/div[3]/button/div")
                xElement.click()
                time.sleep(1)

def main():
    market = IGbot("barnamz_nevis", "barnamzchie")
    market.login()
    market.search("برنامه_نویسی")

if __name__ == "__main__":
    main()
