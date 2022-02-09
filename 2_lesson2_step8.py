from selenium import webdriver

import time
import os


try:
	link = "http://suninjuly.github.io/file_input.html"
	
	browser = webdriver.Chrome()
	browser.get(link)
	
	field_first_name = browser.find_element_by_name("firstname")
	type_answer1 = field_first_name.send_keys("Ivan")

	field_last_name = browser.find_element_by_name("lastname")
	type_answer2 = field_last_name.send_keys("Ivanov")

	field_email = browser.find_element_by_name("email")
	type_answer3 = field_email.send_keys("Ivan@")


	field_file_button = browser.find_element_by_id("file")
	

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, "1.txt")

	
	type_answer4 = field_file_button.send_keys(file_path)


	submit_button = browser.find_element_by_css_selector("button.btn-primary")
	submit_button.click()


finally:

	time.sleep(4)
	browser.quit()


