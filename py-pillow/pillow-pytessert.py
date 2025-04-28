import glob
import os

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'F:\tesseract-ocr\tesseract.exe'

catcha_files = glob.glob('captcha_*.png')
for catcha_file in catcha_files:
    # print(f'../train/{catcha_file}')
    img = cv2.imread(f'../py-pillow/{catcha_file}',cv2.IMREAD_GRAYSCALE)
    assert img is not None, f'../py-pillow/{catcha_file}'

    # 二值化，黑白图片
    _, binary = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))
    cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    # cv2.imshow("gray", cleaned)
    # cv2.waitKey(0)
    text = pytesseract.image_to_string(cleaned,config=r'--psm 10')
    # print(text)
    with open(os.path.join("captcha_deal.txt"), "a",encoding='utf-8') as f:
        f.write(f"{catcha_file} : {text}\n")





