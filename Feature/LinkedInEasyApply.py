import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
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
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disbale-extensions")
        self.driver = webdriver.Chrome(chrome_options=self.options, executable_path=ChromeDriverManager().install())

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
            container = []
            for data in linked_in_feature:
                if data.text == 'LinkedIn Features':
                    data.click()
                    WebDriverWait(self.driver, 20)
                    easy_apply_bool = False
                    i = 1
                    # self.driver.find_element_by_xpath("//div[@id='ember423']/header").click()
                    while not easy_apply_bool:
                        easy_apply = self.driver.find_element_by_xpath("//div[@id='ember79']/ul/li[{}]".format(i))
                        if 'Easy Apply' in easy_apply.text:
                            easy_apply_bool = True
                            easy_apply.click()
                        i += 1
                    WebDriverWait(self.driver, 20)

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
            time.sleep(5)
            # TODO now iterate through nums of loops you get from user input and apply on each and every job you see.
            print(int(self.page_limit))
            try:
                for page in self.page_limit:
                    print('page no.{}'.format(page))
                    pane = self.driver.find_element_by_class_name("jobs-search-results")
                    # ul_tag_data = self.driver.find_element_by_xpath(
                    #     "//div//ul[@class='jobs-search-results__list artdeco-list']")
                    all_li = pane.find_elements_by_tag_name("li")
                    # all_ul_li = ul_tag_data.find_elements_by_tag_name("li")
                    for li in all_li:
                        try:
                            # get link to apply
                            link = li.find_element_by_class_name("job-card-search__link-wrapper")
                            tag = link.get_attribute('href')
                            # Obtain Basic Job Info
                            job_title = li.find_element_by_class_name("job-card-search__title").text
                            location = li.find_element_by_class_name("job-card-search__location").text
                            # location = location.splitlines()[1]

                            company = li.find_element_by_class_name("job-card-search__company-name").text
                            easy_bool = True

                            # If not found then set easy bool to false
                            try:
                                easy_apply = li.find_element_by_class_name("job-card-search__easy-apply")
                            except Exception as e:
                                easy_bool = False

                            # If true apply to job
                            if easy_bool:
                                if tag:
                                    self.apply_to_job(tag)
                                    status = True
                                else:
                                    status = False
                            else:
                                status = False

                            l = []
                            # generate dictionary for reporting
                            values = [company, job_title, location, easy_bool, status]
                            for v in values:
                                l.append(v)
                            container.append(l)
                        # print('successful')
                        except Exception as e:
                            print(e)
                            pass
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def apply_to_job(self, url):
        # Get main window
        current_window = self.driver.current_window_handle
        self.driver.execute_script('window.open(arguments[0]);', url)

        # Go to app window
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)

        # Set init status
        status = False
        # TODO still need to implement code if there are more pages and needs to configure.

        # Look for easy apply button
        try:
            # self.driver.execute_script("window.scrollTo(0,0)")
            easy_apply_button = self.driver.find_element_by_xpath(
                "//div[@class='jobs-top-card__actions']/div/div/button")
            easy_apply_button.click()

            try:
                self.answer_form_1()
                status = True
            except Exception as e:
                status = False

        except Exception as e:
            print("You have already applied to this job!")
            time.sleep(3)

        # Execute required operations to switch back
        self.driver.close()
        self.driver.switch_to.window(current_window)

        [self.driver.close() for window in self.driver.window_handles if window != current_window]

        return status

    def answer_form_1(self):
        try:
            # Here we need to account for different application windows
            time.sleep(1)
            try:
                # req_info = self.driver.find_element_by_id('ember687')
                phone_input = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.ID, 'apply-form-phone-input')))
                phone_input.clear()
                phone_input.send_keys(self.phone_number)
                time.sleep(1)
            except Exception as e:
                print(str(e))

            try:
                resume_button = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'jobs-apply-form__file-upload-label')))
                resume_button.send_keys(self.resume_path)
                time.sleep(1)
            except Exception as e:
                print(str(e))

            try:
                form_submit_btn = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'jobs-apply-form__submit-button')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(3)

        except:
            print("Primary Form Invalid. Switching to secondary....")
            self.answer_form_2()

    def answer_form_2(self):
        try:
            try:
                text_fields = self.driver.find_elements_by_class_name("ember-text-field")
                time.sleep(1)
                text_fields[0].send_keys(self.phone_number)
                time.sleep(2)
            except Exception as e:
                print(str(e))

            try:
                work_auth_check = self.driver.find_element_by_class_name("ember586-answer")
                work_auth_check.click()
                time.sleep(2)
            except Exception as e:
                print(str(e))

            try:
                work_auth_check_two = self.driver.find_element_by_class_name("ember592-answer")
                work_auth_check_two.click()
                time.sleep(2)
            except Exception as e:
                print(str(e))

                # self.driver.execute_script("window.scrollTo(0, Y)")
            try:
                form_submit_btn = WebDriverWait(self.driver, 3).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'jobs-apply-form__submit-button')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(10)
        except:
            print("Primary Form Invalid. Switching to auxillary....")
            self.answer_form_3()

    def answer_form_3(self):
        try:
            try:
                form_submit_btn = WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'continue-btn')))
                form_submit_btn.click()
            except Exception as e:
                print(str(e))

            print("Successfully applied to job!")
            time.sleep(10)

        except Exception as e:
            print('No forms valid...')
            print(str(e))
