import xml.etree.ElementTree as ET
import json
import os

def parse_mindmap_to_json(mindmap_file):
    """
    將FreeMind心智圖文件轉換為JSON格式
    """
    tree = ET.parse(mindmap_file)
    root = tree.getroot()
    
    # 獲取根節點
    root_node = root.find('.//node')
    if root_node is None:
        raise ValueError("Invalid mindmap file: no root node found")
    
    # 解析模組
    module = {
        "name": root_node.get('TEXT', ''),
        "description": "",
        "test_items": []
    }
    
    # 解析測試項目
    for test_item_node in root_node.findall('.//node'):
        test_item = {
            "name": test_item_node.get('TEXT', ''),
            "description": "",
            "test_points": []
        }
        
        # 解析測試點
        for test_point_node in test_item_node.findall('.//node'):
            test_point = test_point_node.get('TEXT', '')
            if test_point:
                test_item["test_points"].append(test_point)
        
        module["test_items"].append(test_item)
    
    return module

def save_module_to_json(module, output_file):
    """
    將模組保存為JSON文件
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(module, f, ensure_ascii=False, indent=2)

def import_mindmap(mindmap_file, output_dir):
    """
    導入心智圖文件並保存為JSON
    """
    # 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 解析心智圖
    module = parse_mindmap_to_json(mindmap_file)
    
    # 生成輸出文件名
    output_file = os.path.join(
        output_dir,
        f"{module['name']}.json"
    )
    
    # 保存為JSON
    save_module_to_json(module, output_file)
    return output_file

if __name__ == "__main__":
    # 使用範例
    mindmap_file = "data/初版測試點总结.mm"
    output_dir = "modules"
    output_file = import_mindmap(mindmap_file, output_dir)
    print(f"已將心智圖轉換為JSON並保存到: {output_file}") 