import os
import streamlit as st
from agent import ask

try:
    os.environ["DEEPSEEK_API_KEY"]=st.secrets["DEEPSEEK_API_KEY"]
except Exception:
    pass

@st.cache_resource
def init_kb():
    from rag import build_kb
    build_kb()
    return True

init_kb()

st.set_page_config(page_title="AI学习助手")
st.title("AI学习助手")

st.caption("基于 DeepSeek + langchain + RAG的知识问答助手")

question =st.text_input("输入你的问题")

if st.button("提问",type="primary"):
    if question.strip():
        with st.spinner("思考中..."):
            answer=ask(question)
        st.success("回答完成")
        st.write(answer)
    else:
        st.warning("请输入问题")
st.divider()
st.markdown("**试试问：** 栈和队列有什么区别？ / 12 + 34 等于多少？")

