import torch
from ultralytics import YOLO

# 載入 YOLOv8 模型
model = YOLO('yolov8n.pt')  # 可以替換成 yolov8s.pt, yolov8m.pt 等

if __name__ == "__main__":
    # 訓練模型
    model.train(
        data='yolo8/data.yaml',  # 設置為你的 data.yaml 文件路徑
        epochs=100,                # 訓練的迭代次數
        batch=16,                  # 每次訓練的批次大小
        imgsz=640,                 # 訓練的圖片大小
        device = torch.device("cuda:0"),                  # 設置為 GPU (如果可用)
        project='runs/train',      # 保存模型的位置
        name='PlayerCuda'                 # 訓練實驗名稱
    )

