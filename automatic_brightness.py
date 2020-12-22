import cv2
import numpy
import os

def brightening(file_img, tb):
    img = cv2.imread(file_img)
    cols, rows, _ = img.shape
    brightness = numpy.sum(img) / (255 * cols * rows)
    print(cols, rows)
    brightness = numpy.sum(img) / (255 * cols * rows)
    print(brightness)
    
    ratio = brightness / tb
    bright_img = cv2.convertScaleAbs(img, alpha = 1 / ratio, beta = 0)
    save_name = file_img
    os.remove(file_img)
    cv2.imwrite(save_name, bright_img)


paths=["target folder"]
target_brightness = 2.25

for path in paths:
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".jpg"):
                brightening(os.path.join(root, filename), target_brightness)