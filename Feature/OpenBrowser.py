from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

user = "jenil.desai25@gmail.com"
pwd = "jenildesai25"
# driverPath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.linkedin.com/login")
# assert "Facebook" in driver.title
elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
job_search_url = "https://www.linkedin.com/jobs/search/?keywords="

# driver.close()

