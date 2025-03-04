import cv2              # pip install opencv-python
import pyzbar.pyzbar as pyzbar          # pip install pyzbar


def barcode_rec():
    print("recognition start!")
    cap = cv2.VideoCapture(0)
    bol, frame = cap.read()

    if bol:
        try:
            for code in pyzbar.decode(frame):
                barcode = code.data.decode('utf-8')
                print(f"Success: {barcode}")
                return barcode

        except Exception as e:
            print(f"Error: {e}")
            return "Error"

        # cv2.imshow('cam', frame)
        key = cv2.waitKey(1)
        if key == 27:
            print("No")
            return "No"

    cap.release()
    cv2.destroyAllWindows()


barcode_rec()
