from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))




try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	price_needed = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))	

	button = browser.find_element_by_id("book")
	button.click()

	x = browser.find_element_by_id("input_value")
	x_to_text = x.text
	y = calc(x_to_text)

	field_for_answer = browser.find_element_by_id("answer")
	field_for_answer.send_keys(y)

	find_submit_button2 = browser.find_element_by_id("solve")
	find_submit_button2.click()





finally:
	time.sleep(4)
	browser.quit()

