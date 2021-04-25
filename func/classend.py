
import time
import cv2

import numpy as np
from func.orb import image_checker
from func.ss import screenshot
def end_clas_check():
    screenshot()
        
    img1 = cv2.imread('./images/screenshot.png')
    img2 = cv2.imread('./images/to_compare.png')
    value = image_checker(img1, img2)
    print(value)


