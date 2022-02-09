from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"

	browser = webdriver.Chrome()
	browser.get(link)

	x_value = browser.find_element_by_id("input_value")
	x = x_value.text

	y = calc(x)

	field_for_answer = browser.find_element_by_id("answer")
	
	enter_answer = field_for_answer.send_keys(y)

	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()


	radiobutton = browser.find_element_by_id("robotsRule")
	radiobutton.click()
	
	submit_button = browser.find_element_by_css_selector("button.btn-default")
	submit_button.click()

finally:

	time.sleep(4)

	browser.quit()







	

