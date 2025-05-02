# Python外部ライブラリのインポート
import json
import boto3

# AssumeRoleを実施
session = boto3.Session(profile_name="admin")

# Bedrockクライアントの作成
#bedrock_runtime = boto3.client("bedrock-runtime")
bedrock_runtime = session .client("bedrock-runtime")

# リクエストボディを定義
body = json.dumps(
    {
        "messages": [
            {
                "role": "user",
                "content": [{"text": "いろは歌を教えて"}],
            }
        ],
        "inferenceConfig": {"max_new_tokens": 1000},
    }
)

# モデルを定義（Amazon Nova Pro 東京リージョン）
modelId = "apac.amazon.nova-pro-v1:0"

# レスポンスを定義
response = bedrock_runtime.invoke_model_with_response_stream(body=body, modelId=modelId)

# ストリーミング出力
for event in response.get("body"):
    chunk = json.loads(event["chunk"]["bytes"])
    
    if "contentBlockDelta" in chunk:
        print(chunk["contentBlockDelta"]["delta"]["text"], end="")

# ストリーミング終了後に改行
print()