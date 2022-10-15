import pytesseract
import cv2 # OpenCV


def display_image():
    cv2.imshow('image', img)  # BGR (RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread('D:/Users/z127776/Desktop/image_tesseract.PNG')

    img_to_rgb_format = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(img_to_rgb_format)

    print(text)