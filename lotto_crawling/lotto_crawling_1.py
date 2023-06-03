from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_2'
driver.get(url)
rotto_num1 = driver.find_element(By.CSS_SELECTOR, '#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(1)').text
print(f"당첨번호1: {rotto_num1}")
driver.quit()