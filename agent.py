import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from rag import search
from tools import add,subtract,multiply,divide,search_info

load_dotenv()

@tool
def retrieve_notes(question:str)->str:
    """根据问题从课程知识库中检索相关笔记。回答课程内容的问题时，必须先调用本工具获取资料。"""
    docs=search(question,k=3)
    return "\n".join(docs)

tools=[retrieve_notes,add,subtract,multiply,divide,search_info]

llm=ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0.3
)

prompt=ChatPromptTemplate.from_messages([
    ("system","你是 AI 学习助手。回答课程问题时，先调用 retrieve_notes 获取资料再回答；"
              "需要计算时调用计算工具；资料里没有答案就直说不知道，不要编造。"),
    ("human","{input}"),
    ("placeholder","{agent_scratchpad}"),
])

agent=create_tool_calling_agent(llm,tools,prompt)
executor=AgentExecutor(agent=agent,tools=tools,verbose=True)

def ask(question:str)->str:
    result=executor.invoke({"input":question})
    return result["output"]

if __name__=='__main__':
    print(ask("栈和队列有什么区别？"))

