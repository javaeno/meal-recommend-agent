# 🍱 校园套餐智能推荐助手

基于 LangChain + DeepSeek API 的 RAG 应用，根据用户的口味、预算和饭量推荐校园套餐。

## 功能
- 自然语言输入（如“饭量小，不吃辣，便宜点”）
- 关键词检索 + 大模型生成推荐理由
- Streamlit 网页界面，即开即用

## 技术栈
- Python 3.11
- LangChain
- DeepSeek API（兼容 OpenAI）
- Streamlit
- 关键词匹配（可升级为向量检索）

## 运行方法
```bash
streamlit run meal_app.py
