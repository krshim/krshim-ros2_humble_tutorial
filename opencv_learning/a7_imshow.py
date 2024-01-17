import cv2

def main():
    img = cv2.imread("/home/uav/krshim-ros2_humble_tutorial/opencv_learning/data/lena.jpg" , 1)
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()