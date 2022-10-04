from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

user = "donny.rivera@jumpplus.com"
pwd = "R1v3r413"



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://gsx2.apple.com/settings/permissions")
time.sleep(2)

driver.switch_to.frame("aid-auth-widget-iFrame")
time.sleep(3)
username = driver.find_element(By.ID, "account_name_text_field")
username.send_keys(user)
username.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element(By.ID, "password_text_field")
password.send_keys(pwd)
password.send_keys(Keys.ENTER)
time.sleep(4)
driver.get("https://gsx2.apple.com/settings/permissions")
time.sleep(3)

table_id = driver.find_element(By.ID, "tab-stl")
table_id.click()
time.sleep(3)

csv_row = []

for i in range(1,17):
    row_id = driver.find_element(By.ID, f"shipToLocationsTable_row{i}")
    td_id0 = driver.find_element(By.ID, f"simple-table_col{0}_row{i}")
    content0 = td_id0.find_element(By.TAG_NAME, "span")
    td_id1 = driver.find_element(By.ID, f"simple-table_col{1}_row{i}")
    content1 = td_id1.find_element(By.TAG_NAME, "span")
    td_id2 = driver.find_element(By.ID, f"simple-table_col{2}_row{i}")
    content2 = td_id2.find_element(By.TAG_NAME, "span")
    csv_row.append(content0.text)
    csv_row.append(content1.text)
    csv_row.append(content2.text)

f = open('mydata.txt', 'w')
writer = csv.writer(f)

writer.writerow(csv_row)
f.close()


time.sleep(5)






