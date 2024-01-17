import cv2

def main():
    img = cv2.imread("/home/uav/krshim-ros2_humble_tutorial/opencv_learning/data/lena.jpg" , 1)
    
    cv2.imwrite("/home/uav/krshim-ros2_humble_tutorial/opencv_learning/output/lena_copy.png", img)
 
 


if __name__ == "__main__":
    main()  