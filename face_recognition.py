
"""
1. first downlad the haarcascade frontalface defaultxml file
2. the file should be in the path of image files
"""
import cv2, glob
gimage = glob.glob("/home/srihari/Documents/*.jpg")
detect = cv2.CascadeClassifier('/home/srihari/Documents/haarcascade_frontalface_default.xml')
for timage in gimage:
    image = cv2.imread(timage)
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = detect.detectMultiScale(grayimg, 1.25, 3)
    for (x, y, w, h) in face:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0.255,0), 2)
        cv2.imshow("detect images", image)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        
