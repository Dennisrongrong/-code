import cv2
import numpy as np
#顶帽
#原图与开运算图之差
#分离比邻近点亮的斑块，用于突出原图像中比周围亮的区域
#读图
img = cv2.imread("data/2.jpg", 0)
#设置核
kernel = np.ones((5,5),np.uint8)
#顶帽调用
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#显示效果
cv2.imshow('src',img)
cv2.imshow('show',tophat)
cv2.waitKey()