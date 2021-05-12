#1부터 50까지 누르는 프로그램을 봇처럼 해주는 프로그램
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

#전역변수
#현재 찾아야될 숫자
num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num += 1
            return

while num<=50:
    clickBtn()