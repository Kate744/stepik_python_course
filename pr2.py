#В коде используется webdriver-manager, позволяющий не заморачиваться с версиями драйвера, для его установке в терминале надо набрать: pip install webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By





try:


    link= "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)



    first_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    last_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    email_input = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    first_name_input.send_keys('Вася')
    last_name_input.send_keys('Пупкин')
    email_input.send_keys('vasya@mail.ru')
    submit_button.click()

    time.sleep(1)

    congrats_text = browser.find_element(By.TAG_NAME, 'h1').text
    
    assert congrats_text == 'Congratulations! You have successfully registered!'

    time.sleep(5)

finally:
    browser.quit()