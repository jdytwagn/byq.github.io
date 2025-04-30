from PIL import Image
import numpy as np
from pathlib import Path

def process_ball_image(input_path, output_path):
    # 打開圖片
    img = Image.open(input_path)
    
    # 轉換為RGBA模式以支持透明度
    img = img.convert('RGBA')
    
    # 獲取圖片數據
    data = np.array(img)
    
    # 創建透明遮罩
    r, g, b, a = data.T
    
    # 假設背景是白色的，將白色區域設為透明
    white_areas = (r > 240) & (g > 240) & (b > 240)
    data[..., 3][white_areas.T] = 0
    
    # 創建新的圖片
    result = Image.fromarray(data)
    
    # 保存結果
    result.save(output_path, 'PNG')

# 確保輸出目錄存在
Path('ball.png').parent.mkdir(parents=True, exist_ok=True)

# 處理圖片
process_ball_image('original_ball.png', 'ball.png') 