import cv2
image=cv2.imread("blossom tree.jpg")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_image=cv2.resize(gray_image,(500,500))
cv2.imshow("resized_image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()