import json
import os
import xml.etree.ElementTree as ET
from datetime import datetime

def create_mindmap(modules_data, output_file):
    """
    將模組數據轉換為FreeMind心智圖格式
    """
    # 創建根元素
    root = ET.Element("map")
    root.set("version", "1.0.1")
    
    # 創建主節點
    main_node = ET.SubElement(root, "node")
    main_node.set("TEXT", "測試點總結")
    main_node.set("CREATED", str(int(datetime.now().timestamp() * 1000)))
    main_node.set("MODIFIED", str(int(datetime.now().timestamp() * 1000)))
    main_node.set("STYLE", "bubble")
    
    # 添加模組
    for module in modules_data["modules"]:
        module_node = ET.SubElement(main_node, "node")
        module_node.set("TEXT", module["name"])
        module_node.set("STYLE", "fork")
        
        # 添加測試項目
        for item in module["test_items"]:
            item_node = ET.SubElement(module_node, "node")
            item_node.set("TEXT", item["name"])
            item_node.set("STYLE", "fork")
            
            # 添加測試點
            for point in item["test_points"]:
                point_node = ET.SubElement(item_node, "node")
                point_node.set("TEXT", point)
                point_node.set("STYLE", "fork")
    
    # 創建XML樹
    tree = ET.ElementTree(root)
    
    # 寫入文件
    tree.write(output_file, encoding="utf-8", xml_declaration=True)

def generate_mindmap():
    """
    從modules.json生成心智圖
    """
    # 確保輸出目錄存在
    os.makedirs("exports", exist_ok=True)
    
    # 讀取模組數據
    with open("modules.json", "r", encoding="utf-8") as f:
        modules_data = json.load(f)
    
    # 生成輸出文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"exports/測試點總結_{timestamp}.mm"
    
    # 創建心智圖
    create_mindmap(modules_data, output_file)
    print(f"已生成心智圖：{output_file}")

if __name__ == "__main__":
    generate_mindmap() 