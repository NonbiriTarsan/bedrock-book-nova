import streamlit as st
from langchain_aws import ChatBedrock
from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import boto3

# AssumeRoleを実施
boto3_session = boto3.Session(profile_name="admin")

# 検索手段を指定
retriever = AmazonKnowledgeBasesRetriever(
    credentials_profile_name="admin", 
    knowledge_base_id="XXXXXXX",  # ここにナレッジベースIDを記載する
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
)

# プロンプトのテンプレートを定義
prompt = ChatPromptTemplate.from_template(
    "以下のcontextに基づいて回答してください: {context} / 質問: {question}"
)

# LLMを指定
model = ChatBedrock(
    credentials_profile_name="admin", 
    model_id = "apac.amazon.nova-pro-v1:0",
    model_kwargs={"max_tokens": 1000},
)

# チェーンを定義（検索 → プロンプト作成 → LLM呼び出し → 結果を取得）
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# フロントエンドを記述
st.title("おしえて！Bedrock")
question = st.text_input("質問を入力")
button = st.button("質問する")

# ボタンが押されたらチェーン実行結果を表示
if button:
    st.write(chain.invoke(question))
