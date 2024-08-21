import cv2

# 假設我們有一個影像 frame
frame = cv2.imread('01.jpg')

# 假設我們有檢測結果的座標
x1, y1, x2, y2 = 50, 100, 200, 200

# 繪製矩形框
cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 顯示影像
cv2.imshow('Image with Box', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
