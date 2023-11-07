import cv2
import numpy as np
# 开运算
# 先腐蚀再膨胀
# 可在纤细点出分离物体。有助于消除噪音
# 读图
img = cv2.imread("data/2.jpg", 0)
print(img)
# 设置核
kernel = np.ones((5, 5), np.uint8)
print(kernel)
# 开运算
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 显示效果
cv2.imshow('src', img)
cv2.imshow('result', opening)
cv2.waitKey(0)