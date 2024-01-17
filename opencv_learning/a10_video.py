import cv2

def main():
    cap = cv2. VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord("q"):
                con = False


if __name__ == "__main__":
    main()