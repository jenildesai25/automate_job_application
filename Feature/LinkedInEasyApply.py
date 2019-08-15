from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait


# user = "jenil.desai25@gmail.com"
# pwd = "jenildesai25"
# # driverPath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.linkedin.com/login")
# # assert "Facebook" in driver.title
# elem = driver.find_element_by_id("username")
# elem.send_keys(user)
# elem = driver.find_element_by_id("password")
# elem.send_keys(pwd)
# elem.send_keys(Keys.RETURN)
# job_search_url = "https://www.linkedin.com/jobs/search/?keywords="

# driver.close()

class LinkedInEasyApply:

    def __init__(self, email_address, email_password, linkedin_username, linkedin_password, desired_job_title, city,
                 state, phone_number, page_limit, resume_path):
        self.email_address = email_address
        self.email_password = email_password
        self.linkedin_username = linkedin_username
        self.linkedin_password = linkedin_password
        self.desired_job_title = desired_job_title
        self.city = city
        self.state = state
        self.phone_number = phone_number
        self.page_limit = page_limit
        self.resume_path = resume_path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        try:
            login_path = "https://www.linkedin.com/login"
            self.driver.get(login_path)
            # assert "Linkedin" in self.driver.title
            temp = self.driver.find_element_by_id("username")
            temp.send_keys(self.linkedin_username)
            temp = self.driver.find_element_by_id("password")
            temp.send_keys(self.linkedin_password)
            temp.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10)
            print('True')
            return True
        except Exception as e:
            print(e)

    def _generate_url_for_jobs(self):
        try:
            base_url = "https://www.linkedin.com/jobs/search/?keywords="
            job_title = self.desired_job_title.replace(" ", "%20") + "&location="
            state = self.state.replace(" ", "%20")

            if self.city:
                city = self.city.replace(" ", "%20") + "%2C%20"
                # url = base_url + job_title + city + state + "&start=30"
                url = base_url + job_title + city + state
            else:
                # url = base_url + job_title + state + "&start=30"
                url = base_url + job_title + state

            print(url)
            return url
        except Exception as e:
            print(e)

    def search_for_jobs(self):
        try:
            job_url = self._generate_url_for_jobs()
            self.driver.get(job_url)
            # TODO find all the jobs and go one by one.
            #  Find easy apply button and click on it, After than read all the data and look for another job.
            content = urllib.request.urlopen(job_url)
            print(content.read())
            WebDriverWait(self.driver, 10)
            linked_in_feature = self.driver.find_elements_by_class_name("search-s-facet__form")
            for data in linked_in_feature:
                if data.text == 'LinkedIn Features':
                    data.click()
                    # easy_apply_class = self.driver.find_element_by_class_name("ember-view")
            # search-s-facet-value
            # search-s-facet-value__name t-14 t-black--light t-normal
            #         easy_apply_class.click()
            # self.driver.find_element_by_class_name("ember83").click()

            print('successfull')
            # soup = BeautifulSoup(content, 'html.parser')

        except Exception as e:
            print(e)
