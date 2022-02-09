from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"

	browser = webdriver.Chrome()
	browser.get(link)

	find_pic = browser.find_element_by_id("treasure")
	
	x_value = find_pic.get_attribute("valuex")
	

	y = calc(x_value)

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
