import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request


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
            temp = self.driver.find_element_by_id("username")
            temp.send_keys(self.linkedin_username)
            temp = self.driver.find_element_by_id("password")
            temp.send_keys(self.linkedin_password)
            temp.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10)
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
            time.sleep(5)
            WebDriverWait(self.driver, 10)
            linked_in_feature = self.driver.find_elements_by_class_name("search-s-facet__form")
            time.sleep(5)
            for data in linked_in_feature:
                if data.text == 'LinkedIn Features':
                    data.click()
                    WebDriverWait(self.driver, 20)
                    easy_apply_bool = False
                    i = 1
                    while not easy_apply_bool:
                        easy_apply = self.driver.find_element_by_xpath("//div[@id='ember79']/ul/li[{}]".format(i))
                        if 'Easy Apply' in easy_apply.text:
                            easy_apply_bool = True
                            easy_apply.click()
                            WebDriverWait(self.driver, 10)
                        i += 1
                    i = 1
                    apply_button_bool = False
                    while not apply_button_bool:
                        apply_button = self.driver.find_element_by_xpath(
                            "//div[@id='ember81']/div/button[{}]".format(i))
                        if 'Apply' in apply_button.text:
                            apply_button_bool = True
                            apply_button.click()
                            WebDriverWait(self.driver, 20)
                        i += 1
                    break

            print('successfull')
            # soup = BeautifulSoup(content, 'html.parser')

        except Exception as e:
            print(e)
