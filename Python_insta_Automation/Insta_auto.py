from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
from time import sleep
from selenium.webdriver.common.by import By
from creds import username, password


class insta_auto:

    links=[]
    
    comments = [
        'Amazing'   ,   'Awesome!'  ,   'Nice :)'   ,   'SuperB !!' ,   'Sukhibhava !!'
    ]
    def __init__(self, username, password):
        # self.login(u_n,pw)
        # self.like_commenter_feed()
        # self.liking_commenting_Hashtags('technology')
        # sleep(100)
        # self.driver.close()
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com/")
        self.username = username
        self.password = password

        sleep(5)

    def _accept_cookies(self):
        """Accepts cookies up opening the webpage"""
        COOKIE_XPATH = (By.XPATH, "//button[text()='Allow all cookies']")
        l = self.driver.find_element(*COOKIE_XPATH)
        l.click()
        sleep(3)

    def _enter_username(self):
        """Enter the username"""
        USERNAME_XPATH = (By.XPATH, "//input[@name='username']")
        l = self.driver.find_element(*USERNAME_XPATH)
        l.send_keys(self.username)
        l.click()
        sleep(1)

    def _enter_password(self):
        """Enter the password"""
        PASSWORD_XPATH = (By.XPATH, "//input[@name='password']")
        l = self.driver.find_element(*PASSWORD_XPATH)
        l.send_keys(self.password)
        l.click()
        sleep(1)

    def _submit_login(self):
        """Submit login button"""
        LOGIN_XPATH = (By.XPATH, "//button[@type='submit']")
        l = self.driver.find_element(*LOGIN_XPATH)
        l.click()

    def accept_alerts(self, value="No"):
        """Not accepting alerts after logging in
        By Default, it will say no.
        """
        if value == "Yes":
            CONDITION_XPATH = (By.XPATH, "//button[text()='Turn On']")
        else:
            CONDITION_XPATH = (By.XPATH, "//button[text()='Not Now']")

        l = self.driver.find_element(*CONDITION_XPATH)
        l.click()


    def login(self):
        """Logging into Instagram"""

        # Accepting cookies
        self._accept_cookies()


        # Enter Username
        self._enter_username()

        # Enter Password
        self._enter_password()


        # Click Submit Button
        self._submit_login()

        # Wait for 10 seconds
        sleep(10)


    def like_post(self, post_link):
        """Like the post"""
        self.driver.get(post_link)
        LIKE_XPATH = (By.XPATH, "//div[@class='x78zum5']//div[@class='x1ypdohk']//div[@role='button']")
        l = self.driver.find_element(*LIKE_XPATH)
        l.click()
        sleep(1)

    
    def liking_commenting_Hashtags(self,Hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(Hashtag))
        links=self.driver.find_elements_by_tag_name('a')

        def conditions(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(conditions,links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)
            buttons=self.driver.find_elements_by_xpath("//button[@class='wpO6b  ']")
            buttons[1].click()
            sleep(3)
            try:
                buttons[2].click()
                sleep(3)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(choice(self.comments))
                sleep(3)
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(5)
                try:
                    self.driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
                    sleep(3)
                except:
                    continue
            except:
                continue

    def like_commenter_feed(self):
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        sleep(1)
        html.send_keys(Keys.HOME)
        sleep(3)
        links=self.driver.find_elements_by_xpath("//*[@aria-label='Like']//following::a[@class='zV_Nj']")
        def conditions(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(conditions,links))

        for i in range(3):
            link = valid_links[i].get_attribute('href')
            print(link)
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)
            buttons=self.driver.find_elements_by_xpath("//button[@class='wpO6b  ']")
            buttons[1].click()
            sleep(3)
            try:
                buttons[2].click()
                sleep(3)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(choice(self.comments))
                sleep(3)
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(5)
                try:
                    self.driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
                    sleep(3)
                except:
                    continue
            except:
                continue

        self.links=[]

                





if __name__=='__main__':

    Ins_auto = insta_auto(username, password)
    # Login
    Ins_auto.login()
    # Deny any alerts
    Ins_auto.accept_alerts("No")
    # Like the post
    Ins_auto.like_post("https://www.instagram.com/p/C9ZtTF0txeK/")

