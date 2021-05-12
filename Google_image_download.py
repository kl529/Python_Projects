from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"아이유","limit":50,"print_urls":True,format : 'jpg'}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

//아이유 이미지 구글에서 다운로드 
//keyword를 바꾸고 limit는 사진 개수, format은 확장자명
