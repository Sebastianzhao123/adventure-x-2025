#!/bin/bash
echo "🎭 情绪识别系统演示"
echo "=" * 40

cd ~/Desktop/emotion-recognition

echo "chose:"
echo 
echo 
echo 

read -p "chose (1/2/3): " choice

case $choice in
    1)
        echo "waht.."
        python main.py
        ;;
    2)
        echo "slow down ..."
        echo "   30 frames"
        echo "   terminals "
        echo "   need to learn"
        echo ""
        python slow_demo.py
        ;;
    3)
        echo "fast ..."
        
        sed -i '' 's/frame_count % 15 == 0/frame_count % 3 == 0/g' main.py
        python main.py
        slow
        sed -i '' 's/frame_count % 3 == 0/frame_count % 15 == 0/g' main.py
        ;;
    *)
        echo "what the fuck."
        python main.py
        ;;
esac

echo ""
echo "it is over！"