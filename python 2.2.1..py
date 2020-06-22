import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    x1 = browser.find_element_by_id("num1")
    x = x1.text
    x_final1 = int(x)
    x2 = browser.find_element_by_id("num2")
    x_2 = x2.text
    x_final2 = int(x_2)

    y = str(x_final1 + x_final2)


    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y)

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()



