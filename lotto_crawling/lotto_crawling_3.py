from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from collections import Counter
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2'
driver.get(url)

num_list = []

for i in range(1, 1025):
    select = Select(driver.find_element(By.CSS_SELECTOR, "#dwrNoList"))
    select.select_by_visible_text(str(i))
    driver.find_element(By.CSS_SELECTOR, "#searchBtn").send_keys(Keys.ENTER)
    time.sleep(0.1)

    for j in range(1, 7):
        rotto_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(' + str(j) + ')').text
        num_list.append(rotto_num)

    bonus_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
    num_list.append(bonus_num)

frequent_num = Counter(num_list)
print(frequent_num)

frequent_num_dict = dict(frequent_num)
sorted_frequent_num = sorted(frequent_num_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_frequent_num)

driver.quit()