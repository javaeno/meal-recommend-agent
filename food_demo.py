import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'   # 加在这里
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document          # 注意这里
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. 连接 DeepSeek
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="sk-5dc3009549424066b12e3184ad0d279d",  # 你的 Key
    openai_api_base="https://api.deepseek.com/v1",
    temperature=0.7
)

# 2. 套餐文档（可以增加更多）
documents = [
    "学霸轻食套餐：价格12元，适合饭量小、不吃辣、喜欢清淡的学生，主要配菜：西兰花、鸡胸肉、糙米饭。",
    "硬汉盖饭套餐：价格18元，适合饭量大、重辣、无肉不欢的学生，包含：双份红烧肉、辣椒炒蛋、大碗米饭。",
    "均衡套餐：价格15元，饭量中等，辣度可选，两素一荤，适合大多数学生。"
]

# 3. 转换为 LangChain Document 并切分
docs = [Document(page_content=text) for text in documents]
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
chunks = text_splitter.split_documents(docs)

# 4. 使用本地 Embedding 模型（免费，无需 API）
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 5. 存入 Chroma 向量数据库
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

# 6. 检索函数（语义搜索）
def retrieve(query, k=2):
    results = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in results])

# 7. RAG 生成
def rag_recommend(user_query):
    context = retrieve(user_query)
    prompt = f"""根据以下校园套餐信息回答用户问题。

套餐信息：
{context}

用户问题：{user_query}
请推荐最合适的套餐并说明理由。"""
    response = llm.invoke(prompt)
    return response.content

# 8. 交互循环
if __name__ == "__main__":
    print("校园套餐助手已启动（输入 q 退出）")
    while True:
        user_input = input("\n请输入你的需求：")
        if user_input.lower() == 'q':
            break
        answer = rag_recommend(user_input)
        print("助手：", answer)