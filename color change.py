import cv2
import matplotlib.pyplot as plt
image=cv2.imread("pic.jpg")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("rgb_image")
plt.show()
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap="gray")
plt.title("gray scale image")
plt.show()
cropped_image=image[100:500,200:500]
cropped_rgb=cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()