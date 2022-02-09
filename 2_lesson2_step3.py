from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



try:
	link = "http://suninjuly.github.io/selects1.html"
	link2 = "http://suninjuly.github.io/selects2.html"	
	browser = webdriver.Chrome()
	browser.get(link2)
	

	first_number = browser.find_element_by_id("num1")
	fir = first_number.text
	second_number = browser.find_element_by_id("num2")
	sec = second_number.text
	num1 = int(fir)
	print(num1)
	num2 = int(sec)
	print(num2)
	
	sum = num1 + num2
	sum_to_text = str(sum)

	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum_to_text)

	submit_button = browser.find_element_by_css_selector("button.btn-default")
	submit_button.click()





finally:

	time.sleep(5)
	browser.quit()











