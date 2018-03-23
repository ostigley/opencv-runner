# https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#   help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#   help="type of preprocessing to be done")
# args = vars(ap.parse_args())

# # load the example image and convert it to grayscale
image = cv2.imread('./results/circle0.jpg')
# gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

# # check to see if we should apply thresholding to preprocess the
# # image
# if args["preprocess"] == "thresh":
# gray = cv2.threshold(image, 0, 255,1)[1]

# # make a check to see if median blurring should be done to remove
# # noise
# elif args["preprocess"] == "blur":
gray = cv2.medianBlur(image, 3)
cv2.imwrite('circle0_thresh.jpg', gray)

# # write the grayscale image to disk as a temporary file so we can
# # apply OCR to it
# filename = "{}.png".format(os.getpid())


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
# image = Image.open('./results/circle0.jpg')
# text = pytesseract.image_to_string(image)
# print(text)







