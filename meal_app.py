import streamlit as st
from food_demo import rag_recommend

st.set_page_config(page_title="校园套餐助手", page_icon="🍱")
st.title("🍱 校园套餐智能推荐助手")
st.markdown("告诉我你的口味、预算和饭量，我来推荐最适合你的套餐。")

user_input = st.text_input("说说你的需求", placeholder="例如：饭量小、不吃辣、便宜点")
if user_input:
    with st.spinner("正在为你量身推荐..."):
        result = rag_recommend(user_input)
    st.success("推荐结果")
    st.write(result)