import torch
from ultralytics import YOLO
from PIL import Image

# 載入訓練好的 YOLOv8 模型
model = YOLO('runs/train/PlayerCuda/weights/best.pt')  # 替換成你的模型路徑

# 讀取圖片
image_path = 'x.jpg'  # 替換成你的圖片路徑
image = Image.open(image_path)

# 進行預測
results = model.predict(source=image, save=True)

# 顯示每個結果
for result in results:
    result.show()
