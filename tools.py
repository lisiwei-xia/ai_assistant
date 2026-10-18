from langchain_core.tools import tool

@tool
def add(a:int,b:int)->int:
    """计算两个数的和"""
    return a+b

@tool
def subtract(a:int,b:int)->int:
    """计算两个数的差"""
    return a-b

@tool
def multiply(a:int,b:int)->int:
    """计算两个数的积"""
    return a*b

@tool
def divide(a:int,b:int)->int:
    """计算两个数的商，除数为0时返回错误提示"""
    if b==0:
        return "除数不能为0"
    return a/b

@tool
def search_info(keyword:str)->str:
    """根据关键词搜索信息"""
    return f"[模拟搜索]关于「{keyword}」：这是工具返回的示例内容，实际项目可换成真实搜索 API。"

if __name__=="__main__":
    print("加法:",add.invoke({"a": 3,"b": 5}))
    print("减法:", subtract.invoke({"a": 5, "b": 3}))
    print("乘法:", multiply.invoke({"a": 3, "b": 4}))
    print("除法:", divide.invoke({"a": 10, "b": 2}))
    print("搜索:", search_info.invoke({"keyword": "数据结构"}))