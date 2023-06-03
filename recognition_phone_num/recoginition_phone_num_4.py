import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model('model.h5')

img = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("test", img)
cv2.waitKey(0)

_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
x = img_to_array(img)/255.0
x = np.expand_dims(x[:,:,0], axis=0)

prediction = model.predict(x)
print(f"예측된 숫자: {np.argmax(prediction)}")