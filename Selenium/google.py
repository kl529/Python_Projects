from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome() //크롬을 사용
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") //이미지를 찾을 검색창이 있는 페이지를 넣기
elem = driver.find_element_by_name("q") //검색창
elem.send_keys("조코딩") //검색창에 검색할 것 입력
elem.send_keys(Keys.RETURN) // 검색하기 버튼 클릭

//여기서부터는 검색이후에 스크롤 내리는 코드
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() //검색결과 더보기 클릭하는 코드
        except:
            break
    last_height = new_height
//이까지 스크롤 내리는 코드

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") //이미지 찾기
count = 1
for image in images: //이미지들 
    try:
        image.click() //이미지 클릭
        time.sleep(2) //2초 쉬고
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src") //클릭한 이미지의 url 저장
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") //url을 통해 이미지 저장
        count = count +1
    except:
        pass

//https://www.youtube.com/watch?v=1b7pXC1-IbE 조코딩 영상