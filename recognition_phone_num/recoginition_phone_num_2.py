import tensorflow as tf
import cv2

mnist  = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

img1 = X_train[0]
img2 = X_train[1]

img1_enlarged = cv2.resize(img1, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
img2_enlarged = cv2.resize(img2, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

cv2.imshow('sample', img1_enlarged)
cv2.waitKey(0)

cv2.imshow('sample', img2_enlarged)
cv2.waitKey(0)

label1 = y_train[0]
label2 = y_train[1]
print(label1, label2)