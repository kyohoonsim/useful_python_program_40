from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2'
driver.get(url)

for i in range(1, 7):
    rotto_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(' + str(i) + ')').text
    print(f"당첨번호{i}: {rotto_num}")

bonus_num = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span').text
print(f"보너스번호: {bonus_num}")

driver.quit()