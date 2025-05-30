# Pyhton外部モジュールのインポート
from langchain.globals import set_debug
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

# デバッグを有効化
set_debug(True)

# ChatBedrockを生成
# モデルを定義（Amazon Nova Pro 東京リージョン）
chat = ChatBedrock(
    credentials_profile_name="admin", 
    model_id = "apac.amazon.nova-pro-v1:0",
    model_kwargs={"max_tokens": 1000},
)

# メッセージを定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

# モデル呼び出し
response = chat.invoke(messages)

print(response.content)