import cv2
import numpy as np

def apply_filter(input_path, output_path, filter_name):
    img = cv2.imread(input_path)

    if filter_name == "grayscale":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter_name == "invert":
        img = cv2.bitwise_not(img)
    elif filter_name == "blur":
        img = cv2.GaussianBlur(img, (15, 15), 0)
    elif filter_name == "edges":
        img = cv2.Canny(img, 100, 200)

    cv2.imwrite(output_path, img)
