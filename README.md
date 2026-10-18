# AI 学习助手

一个基于 **RAG（检索增强生成）+ Agent 工具调用** 的智能问答应用，前端使用 Streamlit 构建。它能够基于你自己的课程笔记回答问题，还能调用计算、搜索等工具完成更复杂的任务。

## 功能特性

- 📚 **知识库问答**：基于私有课程资料（`my_notes.txt`）回答问题，回答有依据、不编造
- 🧮 **工具调用**：Agent 自动调用加、减、乘、除等计算工具
- 🔍 **模拟搜索**：提供"联网搜索"风格的信息检索工具
- 🚫 **拒绝编造**：知识库和工具都找不到答案时，明确告知用户，不胡编乱造
- 🌐 **云端可访问**：已部署到 Streamlit Cloud，任何设备打开链接即可使用

## 系统架构

```
用户提问
   │
   ▼
┌─────────────┐
│ Streamlit 前端 │  app.py：网页界面，接收问题、展示答案
└─────────────┘
   │
   ▼
┌─────────────┐
│    Agent    │  agent.py：判断该用哪个工具，循环调用直到得到答案
└─────────────┘
   │            │
   ▼            ▼
┌──────────┐  ┌──────────┐
│ RAG 检索  │  │ 工具调用  │  rag.py：从知识库找相关资料
└──────────┘  └──────────┘  tools.py：计算 / 模拟搜索
   │            │
   ▼            ▼
┌──────────────────────────┐
│   DeepSeek 大模型（LLM）  │  结合检索结果与工具结果生成最终回答
└──────────────────────────┘
```

## 项目结构

```
ai_assistant/
├── app.py              # Streamlit 前端入口（运行它启动应用）
├── agent.py            # Agent 模块：组装检索 + 工具 + 大模型
├── rag.py              # RAG 模块：文档切分、向量库构建、检索
├── tools.py            # 工具模块：加/减/乘/除、模拟搜索
├── my_notes.txt        # 私有课程资料（知识库数据来源）
├── requirements.txt    # 依赖清单
├── .env                # 本地 API Key 配置（已被 .gitignore 排除，不会上传）
├── .gitignore          # 排除敏感文件与临时文件
└── README.md           # 项目文档
```

## 本地运行

### 1. 环境准备

```bash
# 创建虚拟环境（Windows）
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 API Key

在项目根目录创建 `.env` 文件：

```
DEEPSEEK_API_KEY = "sk-你的密钥"
```

> 从 [DeepSeek 开放平台](https://platform.deepseek.com/) 获取 API Key。

### 3. 启动应用

```bash
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`。

## 云端部署（Streamlit Cloud）

1. 将代码推送到 GitHub 仓库
2. 打开 [share.streamlit.io](https://share.streamlit.io)，点击 **Deploy an app**
3. 选择你的 GitHub 仓库、分支 `main`、主文件 `app.py`，点击 **Deploy**
4. 部署完成后，进入 **Manage app → Settings → Secrets**，配置：

```
DEEPSEEK_API_KEY = "sk-你的密钥"
```

5. 保存后点击 **Rerun**，应用即可正常使用

## 使用示例

| 提问 | 期望行为 |
|------|----------|
| "什么是链表？" | 基于笔记内容回答 |
| "3.5 * 2 + 1 等于多少？" | 调用计算工具算出答案 |
| "今天杭州天气怎么样？" | 调用模拟搜索工具给出结果 |
| "介绍一下量子力学？" | 资料中没有，明确说明不知道，不编造 |

## 技术栈

- **Streamlit**：前端界面
- **LangChain**：Agent 框架、工具调用、LCEL
- **ChromaDB**：本地向量数据库（知识库）
- **DeepSeek API**：大模型（OpenAI 兼容接口）
