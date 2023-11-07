import cv2
import numpy as np
#形态学梯度
#膨胀图与腐蚀图之差
#用于保留目标物体的边缘轮廓
# 读图
img = cv2.imread("data/2.jpg", 0)
# 设置核
kernel = np.ones((5, 5), np.uint8)
# 形态学梯度调用
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 显示效果
cv2.imshow('src', img)
cv2.imshow('result', gradient)
cv2.waitKey()