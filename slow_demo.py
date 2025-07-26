import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 减少TensorFlow日志

import cv2
from deepface import DeepFace
import numpy as np
from datetime import datetime
import time

# M4 Pro优化
cv2.setNumThreads(8)

# 初始化摄像头
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)




# 情绪映射（中文）
emotion_map = {
    'angry': '😠 angry',
    'disgust': '🤢 disgust', 
    'fear': '😨 fear',
    'happy': '😊 happy',
    'sad': '😢 sad',
    'surprise': '😲 surprise',
    'neutral': '😐 neutral'
}

# 颜色映射
color_map = {
    'angry': (0, 0, 255),      
    'happy': (0, 255, 0),      
    'sad': (255, 0, 0),        
    'neutral': (128, 128, 128), 
    'surprise': (0, 255, 255),  
    'fear': (255, 0, 255),     
    'disgust': (0, 128, 255) }  


frame_count = 0
emotion_data = []
last_emotion = "neutral"
emotion_change_time = time.time()
current_emotion = "neutral"
emotion_confidence = 0.0
analysis_count = 0

print(f"📝 data saved to slow_demo_log.json")