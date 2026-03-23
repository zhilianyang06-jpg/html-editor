import streamlit as st
import streamlit.components.v1 as components

# 页面配置
st.set_page_config(
    page_title="HTML 可视化编辑器",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏 Streamlit 默认样式
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 读取 HTML 编辑器文件
def load_html_editor():
    with open('html_editor_standalone.html', 'r', encoding='utf-8') as f:
        return f.read()

# 渲染 HTML 编辑器
html_content = load_html_editor()
components.html(html_content, height=1000, scrolling=True)
