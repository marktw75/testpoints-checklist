import json
import os
import glob

def merge_modules():
    """
    合併所有模組JSON文件為一個文件
    """
    # 獲取所有模組JSON文件
    module_files = glob.glob('modules/*.json')
    
    # 讀取並合併所有模組
    all_modules = []
    for file_path in module_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            module = json.load(f)
            all_modules.append(module)
    
    # 保存合併後的文件
    with open('modules.json', 'w', encoding='utf-8') as f:
        json.dump({
            "modules": all_modules,
            "total_modules": len(all_modules)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"已合併 {len(all_modules)} 個模組到 modules.json")

if __name__ == "__main__":
    merge_modules() 