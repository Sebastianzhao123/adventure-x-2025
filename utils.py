import matplotlib.pyplot as plt
import json
from collections import Counter

def analyze_emotion_log(log_file='output/emotion_log.json'):
    """分析情绪日志并生成报告"""
    try:
        with open(log_file, 'r') as f:
            data = json.load(f)
        
        if not data:
            print("no emotion data found")
            return
            
        # 统计情绪分布
        emotions = [item['emotion'] for item in data]
        emotion_counts = Counter(emotions)
        
        # 生成饼图
        plt.figure(figsize=(10, 6))
        plt.pie(emotion_counts.values(), labels=emotion_counts.keys(), autopct='%1.1f%%')
        plt.title('emotion distribution statistics')
        plt.savefig('output/emotion_distribution.png')
        plt.close()
        
        # 生成时间线图（简化版）
        plt.figure(figsize=(12, 6))
        times = [i for i in range(len(data))]  # 使用索引代替时间
        emotions_timeline = [item['emotion'] for item in data]
        
        # 将情绪转换为数值
        emotion_to_num = {emotion: i for i, emotion in enumerate(set(emotions))}
        emotion_nums = [emotion_to_num[emotion] for emotion in emotions_timeline]
        
        plt.plot(times[::10], emotion_nums[::10], 'o-')
        plt.title('emotion change timeline')
        plt.xlabel('detection times')
        plt.ylabel('emotion type')
        plt.yticks(list(emotion_to_num.values()), list(emotion_to_num.keys()))
        plt.tight_layout()
        plt.savefig('output/emotion_timeline.png')
        plt.close()
        
        print("analysis report generated:")
        print("- emotion_distribution.png")
        print("- emotion_timeline.png")
        
        # 打印统计信息
        print(f"\ntotal detection times: {len(data)}")
        print("emotion distribution:")
        for emotion, count in emotion_counts.most_common():
            percentage = (count / len(data)) * 100
            print(f"  {emotion}: {count}次 ({percentage:.1f}%)")
            
    except FileNotFoundError:
        print(f"no log file found: {log_file}")
        print("please run main.py for emotion detection")
    except Exception as e:
        print(f"analysis error: {e}")