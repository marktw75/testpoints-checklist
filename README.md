# 測試點檢查清單系統

這是一個幫助QA團隊管理和生成測試點的系統。

## 專案結構

```
testpoints-checklist/
│
├── modules/                # 存放模組 JSON，每個模組獨立成一檔
│   ├── 基本功能測試.json
│   ├── 測試點模板.json
│   └── ...
│
├── importers/              # 放心智圖 → JSON 的轉換程式碼
│   └── freemind_parser.py
│
├── data/                   # 原始心智圖檔（.mm, .xmind）
│   └── 初版測試點总结.mm
│
├── docs/                   # 未來放圖解、使用教學
│
├── modules.json            # 整合過的模組集合
├── merge_modules.py        # 合併模組的腳本
├── README.md
└── requirements.txt        # 依賴的 Python 套件
```

## 功能特點

- 使用JSON文件存儲測試點，易於維護和修改
- 支援從心智圖文件導入測試點
- 模組化管理測試點
- 提供測試點模板
- 支援合併多個模組

## 安裝說明

1. 安裝Python依賴：
```bash
pip install -r requirements.txt
```

2. 導入心智圖（可選）：
```bash
python importers/freemind_parser.py
```

3. 合併模組（可選）：
```bash
python merge_modules.py
```

## 使用說明

### 1. 管理測試點

在`modules/`目錄下創建或修改JSON文件來管理測試點。每個JSON文件代表一個測試模組，包含：
- 模組名稱
- 模組描述
- 測試項目列表
- 每個測試項目包含測試點列表

### 2. 使用模板

`測試點模板.json`提供了常見的測試點模板，可以作為新增測試點的參考。模板包含：
- 表單輸入測試點
- 搜索功能測試點
- 文件上傳測試點
- 數據分頁測試點
- 安全性測試點

### 3. 合併模組

使用`merge_modules.py`腳本可以將所有模組合併為一個文件：
```bash
python merge_modules.py
```

合併後的文件會保存在`modules.json`中。

### 4. 從心智圖導入

系統支援從FreeMind心智圖文件導入測試點：

1. 將心智圖文件放在`data/`目錄下
2. 運行導入腳本：
```bash
python importers/freemind_parser.py
```

## 貢獻指南

歡迎提交Pull Request來改進這個專案。請確保：

1. 代碼符合專案的編碼規範
2. 添加適當的測試
3. 更新相關文檔

## 授權

MIT License
