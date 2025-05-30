
# Pyhton外部モジュールのインポート
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# タイトル
st.title("Bedrock チャット")

# ChatBedrockを生成
chat = ChatBedrock(    
    credentials_profile_name="admin", 
    model_id = "apac.amazon.nova-pro-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)
# Nova特別対応：出力が生成したテキストになるようにStrOutputParserを追加
chat = chat | StrOutputParser()

# セッションにメッセージを定義
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    ]

# メッセージを画面表示
for message in st.session_state.messages:
    if message.type != "system":
        with st.chat_message(message.type):
            st.markdown(message.content)

# チャット入力欄を定義
if prompt := st.chat_input("何でも聞いてください。"):
    # ユーザーの入力をメッセージに追加
    st.session_state.messages.append(HumanMessage(content=prompt))

    # ユーザーの入力を画面表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # モデルの呼び出しと結果の画面表示
    with st.chat_message("assistant"):
        response = st.write_stream(chat.stream(st.session_state.messages))
        
    # モデル呼び出し結果をメッセージに追加
    st.session_state.messages.append(AIMessage(content=response))