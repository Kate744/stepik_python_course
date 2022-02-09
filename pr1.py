import time

from selenium import webdriver

# в списке link ссылки до и после верстки
link = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]

try:
    # опрашиваем список ссылок
    for i in link:
        browser = webdriver.Chrome()
        browser.get(i)

        # заполняем обязательные поля
        input1 = browser.find_element_by_css_selector(".first:required")
        input1.send_keys("Mishel")
        input2 = browser.find_element_by_css_selector(".second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("Abrakadabra")
        time.sleep(3)

        # 3 секунд оценить заполнение обязательных полей

        # жмем кнопку зарегистрироваться
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        wtext = browser.find_element_by_tag_name("h1")

        # переменная w_text_m текст из элемента w_text
        wtextm = wtext.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта если нет то сообщение
        # "не удачная регистрация"
        assert "Congratulations! You have successfully registered!" == wtextm


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
