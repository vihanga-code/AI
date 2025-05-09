import cv2
import matplotlib as mlp

def filter_type(image,types):
    copy=image.copy()
    if types=="red_tint":
        copy[:,:,1]=0
        copy[:,:,0]=0
    elif types =="green_tint":
        copy[:,:,0]=0    
        copy[:,:,2]=0
    elif types=="blue_tint":
        copy[:,:,1]=0
        copy[:,:,2]=0
    elif types=="increase_red":
        copy[:,:,2]=cv2.add(copy[:,:,2],50)
    elif types=="decrease_blue":
        copy[:,:,0]=cv2.subtract(copy[:,:,0],50)
    return copy

image_path="images.jpg"
image=cv2.imread(image_path)
if image is None:
    print("error image not found")
else:
    
    original=image
    red_tint=filter_type(image,"red_tint")
    blue_tint=filter_type(image,"blue_tint")
    green_tint=filter_type(image,"green_tint")
    increase_red=filter_type(image,"increase_red")
    decrease_blue=filter_type(image,"decrease_blue")
    
    
    
    cv2.imshow("original",original)
    cv2.waitKey(5000)
    cv2.imshow("original",red_tint)
    cv2.waitKey(5000)
    cv2.imshow("original",blue_tint)
    cv2.waitKey(5000)
    cv2.imshow("original",green_tint)
    cv2.waitKey(5000)
    cv2.imshow("original",increase_red)
    cv2.waitKey(5000)
    cv2.imshow("original",decrease_blue)
    cv2.waitKey(5000)