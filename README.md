# 🍳 家庭菜谱助手 (Recipe App)

一个基于大语言模型（智谱 GLM-4-Flash）和 Streamlit 的极简家庭菜谱生成工具。输入菜名，一键生成结构化菜谱（包含耗时、难度、食材清单和制作步骤）。

## 功能特点
- 极简 Web 界面，无需输入复杂的提示词
- 大模型直接返回 JSON 格式数据，前端结构化展示
- 完善的异常处理（拦截 API 错误、非 JSON 响应）

## 本地运行指南

### 1. 安装依赖
确保你已安装 Python 3.9+，然后运行：
```bash
python3 -m pip install -r requirements.txt
I_KEY=
python3 -m streamlit run app.py
cat .env
