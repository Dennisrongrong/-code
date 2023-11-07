import cv2
import numpy as np
# 黑帽
# 闭运算图-原图像
# 分离比邻近点暗的斑块，突出原图像中比周围暗的区域
#读图
img = cv2.imread("data/2.jpg", 0)
#设置核
kernel = np.ones((5,5),np.uint8)
#黑帽调用
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#显示效果
cv2.imshow('src',img)
cv2.imshow('show',blackhat)
cv2.waitKey()