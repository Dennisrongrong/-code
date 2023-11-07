import cv2
import numpy as np
# 闭运算
# 先膨胀后腐蚀
# 用于排除前景对象中的小孔或对象上的小黑点
# 读图
img = cv2.imread("data/2.jpg", 0)
print(img)
# 设置核
kernel = np.ones((5, 5), np.uint8)
print(kernel)
# 开运算
opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 显示效果
cv2.imshow('src', img)
cv2.imshow('result', opening)
cv2.waitKey(0)