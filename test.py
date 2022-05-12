from selenium import webdriver
from selenium.webdriver.common.by import By

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()

browser.get('http://localhost:3000/')

nav=browser.find_element(by=By.NAME, value='portfolio')
nav.click()

button=browser.find_element(by=By.NAME, value='profile')
button.click()

nav=browser.find_element(by=By.NAME, value='service')
nav.click()

# create
title=browser.find_element(by=By.ID, value='1')
title.send_keys('Пирсинг')

price=browser.find_element(by=By.ID, value='2')
price.send_keys('500')

button=browser.find_element(by=By.ID, value='3')
button.click()

# update
id_course=browser.find_element(by=By.ID, value='4')
id_course.send_keys('1')

title=browser.find_element(by=By.ID, value='6')
title.send_keys('Пирсинг')

price=browser.find_element(by=By.ID, value='7')
price.send_keys('650')

button=browser.find_element(by=By.ID, value='8')
button.click()

# delete
id_course=browser.find_element(by=By.ID, value='4')
id_course.send_keys('2')

button=browser.find_element(by=By.ID, value='5')
button.click()

# find
id_course=browser.find_element(by=By.ID, value='9')
id_course.send_keys('1')

button=browser.find_element(by=By.ID, value='10')
button.click()

# Закрываем браузер
browser.close()