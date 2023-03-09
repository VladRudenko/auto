from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


service_obj = Service('C:\chromedriver.exe')
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.get('https://qastartup.net/')

list_of_curses = driver.find_element(By.CSS_SELECTOR, 'a[class*=tn-atom]')
list_of_curses.click()

chose_course_qa_base = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*=t851__btn]')))
chose_course_qa_base.click()

take_part = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class*=tn-atom]')))
take_part.click()

for i in range(2):
        format_course = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[class*=t615__btn-text]')))
        format_course[i].click()

        field_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(("xpath", '//*[@id="form278351236"]/div[2]/div[1]/div/input')))
        field_name.send_keys('Руденко Влад')

        field_email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(("xpath", '//*[@id="form278351236"]/div[2]/div[2]/div/input')))
        field_email.send_keys('j0019285@gmail.com')

        field_number = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(("xpath", '//*[@id="form278351236"]/div[2]/div[3]/div/div[1]/input[1]')))
        field_number.send_keys('09898476535')
        
        eixt_window_of_registration = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "svg[class*=t-popup__close-icon]")))
        eixt_window_of_registration.click()

driver.quit()