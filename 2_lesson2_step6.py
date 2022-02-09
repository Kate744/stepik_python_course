from selenium import webdriver

import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/execute_script.html"
	browser.get(link)


	x = browser.find_element_by_id("input_value")
	x_to_text = x.text

	y = calc(x_to_text)
	browser.execute_script("window.scrollBy(0, 100);")

	find_field = browser.find_element_by_id("answer")
	enter_answer = find_field.send_keys(y)

	find_checkbox = browser.find_element_by_id("robotCheckbox")
	find_checkbox.click()


	find_radio = browser.find_element_by_id("robotsRule")
	find_radio.click()

	
	find_button = browser.find_element_by_css_selector("button.btn-primary")
	find_button.click()

finally:

	time.sleep(4)

	browser.quit()
