
import easyocr 
import cv2 


reader = easyocr.Reader(['en'])
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))



dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)


contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_NONE)

im2 = img.copy()


file = open("recognized.txt", "w+")
file.write("")
file.close()
    

text = reader.readtext('image.jpg')
for (bbox, text, confidence) in text:
    file.write(text + '\n')
    

file.close()
