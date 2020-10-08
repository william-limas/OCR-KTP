import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/98115b5c-dc58-46f4-9b8f-054491882dad/LabelFile/'

data = {'file': open('C:/Users/sapuser/Desktop/Test Utk Deploy/Image Dir/temp/13.jpeg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('EQURalOb9fgUo83e0KhrNtxW-HHjTLyl', ''), files=data)

# if "l" in response.text:
#     response.text = response.text.replace('l','1')
 
print(response.text)

# import cv2
# import numpy as np
# import pytesseract as pts

# # Image preprocessing
# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# def remove_noise(image):
#     return cv2.medianBlur(image, 5)

# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# def dilate(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.dilate(image, kernel=kernel, iterations=1)

# def erode(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.erode(image, kernel=kernel, iterations=1)

# def opening(image):
#     kernel = np.ones((5, 5), np.uint8)
#     return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel=kernel)

# def canny(image):
#     return cv2.Canny(image, 100, 200)

# def deskew(image):
#     coords = np.column_stack(np.where(image > 0))
#     angle = cv2.minAreaRect(coords)[-1]
#     if angle < -45:
#         angle = -(90 + angle)
#     else:
#         angle = -angle
#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#     return rotated

# def match_template(image, template):
#     return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# import os.path
# import matplotlib.pyplot as plt
# import os
# from PIL import Image

# path = 'C:/Users/sapuser/Desktop/Test Utk Deploy/Image Dir'

# def check_dir():
#     # threading.Timer(5.0, check_dir).start() # called every minute
#     if len(os.listdir(path) ) == 0:
#         print("Directory is empty")
#     else:
#         files = []
#         for file in os.listdir(path):
#             if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".PNG") or file.endswith(".JPG") or file.endswith(".JPEG"):
#                 files.append(os.path.join(path,file))
#         global newest
#         newest=max(files , key = os.path.getmtime)
#         if "\\" in newest:
#             newest = newest.replace("\\", "/")
#         print(newest)   
#         img = Image.open(newest)
#         img_np = np.asarray(img)
#         plt.imshow(img_np)
#         plt.draw()
#         plt.pause(4) # pause how many seconds
#         plt.close()
        
# check_dir()

# # Feed the image
# img = cv2.imread(newest)
# gray = get_grayscale(img)
# # dilated = dilate(img)
# # no_noise = remove_noise(img)
# # erode_img = erode(img)
# # canny_img = canny(img)
# # open_img = opening(img)

# # gray_canny = canny(gray)
# # gray_erode = erode(gray)
# # gray_dilated = dilate(gray)
# # gray_no_noise = remove_noise(gray)
# # gray_open = opening(gray)

# # gray_canny_erode = erode(gray_canny)
# # gray_canny_dilated = dilate(gray_canny)
# # gray_canny_no_noise = remove_noise(gray_canny)
# # gray_canny_open = opening(gray_canny)

# # gray_erode_dilated = dilate(gray_erode)
# # gray_erode_no_noise = remove_noise(gray_erode)
# # gray_erode_open = opening(gray_erode)

# # gray_dilated_no_noise = remove_noise(gray_dilated)
# # gray_dilated_open = opening(gray_dilated)

# # gray_no_noise_open = opening(gray_no_noise)

# # Template Path
# template = cv2.imread('C:\\Users\\sapuser\\Desktop\\KTP Data\\ocra_template.png')
# # match_template(gray_canny, template)

# # Adding custom options
# custom_config = r'--oem 1 --psm 6 -l ind'
# pts.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# result = pts.image_to_string(gray, config=custom_config)

# def convert(s):
#     new = ""
#     for x in s:
#         new += x
#     return new

# import re

# if "NIK" in result:
#   nik_char = result.split()
#   nik_str = convert(nik_char)
#   if "D" in result:
#     nik_str = nik_str.replace('D', '0')
#   if "?" in result:
#     nik_str = nik_str.replace('?', '7')
#   if "b" in result:
#     nik_str = nik_str.replace('b', '6')
#   if "L" in result:
#     nik_str = nik_str.replace('L','1')
#   if "g" in result:
#     nik_str = nik_str.replace('g','9')
#   nik_str = re.sub(r'\\s',"",nik_str)
#   nik_str = nik_str[nik_str.find("NIK")+4:nik_str.find("NIK")+24]
#   nik_str = re.sub(r'[^0-9]',"",nik_str)
  
# # print(result)
    
# nik_else = re.sub(r'[^0-9]',"",result)
# nik_else = nik_else[0:16]
# Name_only = re.sub(r'[^A-z]\\s',"",result)
# Name_only = Name_only[Name_only.find("Nama")+5:Name_only.find("Tempat")]
# Name_only = re.sub(r'[^a-zA-Z0-9]+',' ',Name_only)

# # print(nik_pos_start+)
# if "NIK" in result:
#     print("NIK : " + nik_str)
# else:
#     print("NIK : " + nik_else)

# print("Nama : " + Name_only)

# # Show the image
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()