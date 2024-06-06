# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://easysmarthub.ru/blog/')
#     link = driver.find_element(By.LINK_TEXT, 'Что такое базы данных?')
#     time.sleep(5)
#     link.click()
#     time.sleep(5)
#     link = driver.find_element(By.LINK_TEXT, 'Эрик Спичак')
#     link.click()
#     time.sleep(5)
    


# finally:
#     driver.quit()


# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_02/')
#     input = driver.find_elements(By.CSS_SELECTOR,'input')
#     for i in input:
#         i.send_keys('Text')
   
#     time.sleep(3)
   


# finally:
#     driver.quit()


# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     input = driver.find_elements(By.CSS_SELECTOR,'input')
#     for i in input:
#         i.send_keys('Text@mail.ru')
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     btn.click()
#     time.sleep(5)
#     wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
#     wel_text_block = wel_text.text


#     assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


# finally:
#     time.sleep(5)
#     driver.quit()


# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_03/')
#     #проверили обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#firstName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#lastName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#email')
#     input1.send_keys('text@mail.ru')


#     # проверяет не обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#phone')
#     input1.send_keys('1231231231')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#address')
#     input1.send_keys('text@mail.ru')
   
   
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     btn.click()
#     time.sleep(1)
#     wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
#     wel_text_block = wel_text.text


#     assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_04/')
#     #проверили обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#firstName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#lastName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#email')
#     input1.send_keys('text@mail.ru')


#     # проверяет не обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#phone')
#     input1.send_keys('1231231231')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#address')
#     input1.send_keys('text@mail.ru')
   
   
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     btn.click()
#     time.sleep(1)
#     wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
#     wel_text_block = wel_text.text


#     assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_04/')
#     #проверили обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#firstName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#lastName')
#     input1.send_keys('text')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#email')
#     input1.send_keys('text@mail.ru')


#     # проверяет не обязательные поля
#     input1 = driver.find_element(By.CSS_SELECTOR,'#phone')
#     input1.send_keys('1231231231')
#     input1 = driver.find_element(By.CSS_SELECTOR,'#address')
#     input1.send_keys('text@mail.ru')
   
   
#     btn = driver.find_element(By.CSS_SELECTOR, 'button')
#     btn.click()
#     time.sleep(1)
#     wel_text = driver.find_element(By.CSS_SELECTOR,'h2')
#     wel_text_block = wel_text.text


#     assert 'Поздравляю, вы прошли первый уровень.' == wel_text_block
   
   


# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/Qa_autotest_07/')
#     time.sleep(2)

#     nums = driver.find_element(By.CSS_SELECTOR,'#numberImage')
#     b = nums.get_attribute('data-b')
#     b = b.split('?')


#     anser = int(b[0] + b[1])


#     text = driver.find_element(By.CSS_SELECTOR,'#answer').send_keys(anser)
#     driver.find_element(By.CSS_SELECTOR,'#submitBtn').click()


# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/QA_autotests_11/')
#     time.sleep(2)
  
#     driver.find_element(By.CSS_SELECTOR,'#imageInput').send_keys(r'C:\Users\AttekPC\Desktop\4.jpg')
   

#     driver.find_element(By.CSS_SELECTOR,'[type ="submit"]').click()
   
   




# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_12/')
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, '#startTaskBtn').click()
#     driver.switch_to.alert.accept()
#     driver.switch_to.alert.send_keys('50')
#     driver.switch_to.alert.accept()
#     a = driver.switch_to.alert.text
#     assert 'Правильно, ответ 50.' == a

    



# finally:
#     time.sleep(5)
#     driver.quit()

# ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re

# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()

# try:
#     driver.get('https://erikdark.github.io/QA_autotests_13/')
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, '#openNewPageBtn').click()
#     driver.switch_to.window('viewport')
#     new_window = driver.window_handles[1]
#     driver.find_element(By.CSS_SELECTOR, '#displayTextBtn').click()
#     driver.switch_to.window('viewport')
#     new_window = driver.window_handles[2]
    



# finally:
#     time.sleep(5)
#     driver.quit()

# ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()




# try:
#     driver.get('https://erikdark.github.io/QA_autotests_13/')
#     time.sleep(1)


#     driver.find_element(By.CSS_SELECTOR,'#openNewPageBtn').click()
#     time.sleep(1)


#     new_tab = driver.window_handles[1]
#     driver.switch_to.window(new_tab)


#     driver.find_element(By.CSS_SELECTOR,'#displayTextBtn').click()


#     display_text = driver.find_element(By.CSS_SELECTOR,'#displayText').text


#     assert display_text == 'Я СДЕЛАЛ', 'текст не отображается или не верный текст'
#     print('Test compleate!')
   
   




# finally:
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

# import time
# #импортирую сам вебдрайвер
# from selenium import webdriver
# #импортирую класс By который ищет элемент на странице
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import re




# #иницилизирую драйвер браузера
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)




# try:
#     driver.get('https://erikdark.github.io/QA_autotests_14/')
       
#     btn = driver.find_element(By.ID,'verify').click()
#     message = driver.find_element(By.ID,'verify_message')
#     assert 'Verification successful!' in message.text
       
       

# finally:
#     print('OK')
#     time.sleep(5)
#     driver.quit()

# # ______________________________________________________________________________________________

import time
#импортирую сам вебдрайвер
from selenium import webdriver
#импортирую класс By который ищет элемент на странице
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC                # сокращенное название 
import re


#иницилизирую драйвер браузера
driver = webdriver.Chrome()
driver.implicitly_wait(5)


try:
    driver.get('https://erikdark.github.io/Qa_autotest_15/')
       
    btn = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'verify'))).click()
    message = driver.find_element(By.ID,'verify_message')


finally:
    print('OK')
    time.sleep(5)
    driver.quit()

# # ______________________________________________________________________________________________