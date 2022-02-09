from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))



try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	find_submit_button1 = browser.find_element_by_css_selector("button.btn-primary")
	find_submit_button1.click()
	
	
	
	new_window = browser.window_handles[1]
	old_window = browser.window_handles[0]

	browser.switch_to.window(new_window)

	x = browser.find_element_by_id("input_value")
	x_to_text = x.text
	y = calc(x_to_text)

	field_for_answer = browser.find_element_by_id("answer")
	field_for_answer.send_keys(y)

	find_submit_button2 = browser.find_element_by_css_selector("button.btn-primary")
	find_submit_button2.click()

	


finally:

	time.sleep(4)
	browser.quit()
