import cv2
from matplotlib import pyplot as plt


def main():
    imgBGR = cv2.imread(
        "/home/uav/krshim-ros2_humble_tutorial/opencv_learning/data/lena.jpg", 1
    )
    b, g, r = cv2.split(imgBGR)
    imgRGB = cv2.merge((r, g, b))
    plt.axis("off")
    plt.imshow(imgRGB)
    # plt.imshow(r)
    plt.show()


if __name__ == "__main__":
    main()