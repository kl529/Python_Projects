#네이버 API 얼굴인식 프로그램 그림파일 넣기
import os
import sys
import requests
import json
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
files = {'image': open('YOUR_FILE_NAME', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    # print (response.text)
    data = json.loads(response.text)
    faceCount = data['info']['faceCount']
    print("감지된 얼굴 수는 {}입니다.".format(faceCount))
else:
    print("Error Code:" + rescode)