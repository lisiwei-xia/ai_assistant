import os
import chromadb
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

DATA_FILE="mynotes.txt"
DB_DIR="kb"

def build_kb():
    with open(DATA_FILE,"r",encoding="utf-8")as f:
        text=f.read()

    splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=30)
    chunks=splitter.split_text(text)

    client=chromadb.PersistentClient(path=DB_DIR)
    collection=client.get_or_create_collection("notes")

    try:
        collection.delete(where={})
    except Exception:
        pass


    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks
    )
    print(f"知识库已建立:{len(chunks)}段")

def search(question,k=3):
    client=chromadb.PersistentClient(path=DB_DIR)
    collection=client.get_or_create_collection("notes")
    result=collection.query(query_texts=[question],n_results=k)
    return result["documents"][0]

if __name__=="__main__":
    build_kb()
    print("\n测试检索[栈是什么]的结果:")
    docs=search("栈是什么")
    for d in docs:
        print("-",d)
