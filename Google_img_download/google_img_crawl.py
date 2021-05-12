#검색어를 입력하면 구글에서 이미지 검색값을 다운로드받음
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

name = input("검색어를 입력하세요 : ")
arguments = {"keywords":name,"limit":50,"print_urls":True,format : 'jpg'}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images