import cv2
import numpy as np

def run():
    import cv2
    import numpy as np

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cam.read()
        if not ret:
            break # safety check to ensure we have a valid frame

        frame = cv2.resize(frame, (1920, 1080))

        cv2.imshow("Camera", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            exit()

if __name__ == "__main__":
    run()

