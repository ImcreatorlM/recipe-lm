import streamlit as st
from recipe_json import get_recipe

st.set_page_config(page_title="家庭菜谱助手", page_icon="🍳")
st.title("🍳 家庭菜谱助手")
st.caption("输入菜名，生成结构化菜谱")

dish = st.text_input("菜名", placeholder="例如：青椒肉丝")

if st.button("生成菜谱", type="primary"):
    if not dish.strip():
        st.warning("请先输入菜名")
    else:
        with st.spinner("正在生成菜谱..."):
            try:
                recipe = get_recipe(dish.strip())
            except Exception as e:
                st.error(f"生成失败：{e}")
                recipe = None

        if recipe:
            st.subheader(recipe["title"])
            c1, c2 = st.columns(2)
            c1.metric("耗时", recipe["time"])
            c2.metric("难度", recipe["difficulty"])

            st.markdown("### 食材")
            for item in recipe["ingredients"]:
                st.markdown(f"- {item['name']}：{item['amount']}")

            st.markdown("### 步骤")
            for i, step in enumerate(recipe["steps"], 1):
                st.markdown(f"{i}. {step}")
