from test.model import predict as ocr_predict
import cv2
from PIL import Image



if __name__ == '__main__':

    img = cv2.imread('./img/03.jpg')
    image = Image.fromarray(img).convert('L')
    sim_pred = ocr_predict(image)
    print sim_pred