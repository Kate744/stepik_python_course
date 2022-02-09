from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


try:
	browser = webdriver.Chrome()
	link = "https://dispatch-qa.mavenmachines.com/dispatch"

	browser.get(link)
	login_email = "dicom@mavenmachines.com"
	login_password = "dicom"	

	email_field = browser.find_element_by_name("email")
	password_field = browser.find_element_by_name("password")
	sing_in_button = browser.find_element_by_css_selector("button.login-btn")

	email_field.send_keys(login_email)
	password_field.send_keys(login_password)
	sing_in_button.click()
	
	wait_until_dropdown_loaded = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class = terminal-name]")))

	drop_down_selector = browser.find_element_by_css_selector("div[class = terminal-name]")
	drop_down_selector.click()



finally:
	time.sleep(2)
	browser.quit()
