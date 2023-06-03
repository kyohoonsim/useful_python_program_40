from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.youtube.com/watch?v=1Hu2sHhsSPI'
driver.get(url)

rotto_num1 = driver.find_element(By.CSS_SELECTOR, '#author-text > span').text
print(f"당첨번호1: {rotto_num1}")
driver.quit()

#comment7887786 > div > span.reply-linux



#author-text > span