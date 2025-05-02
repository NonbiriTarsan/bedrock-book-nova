# Python外部ライブラリをインポート
import json
import boto3

# AssumeRoleを実施
session = boto3.Session(profile_name="admin")

# Bedrockクライアントの作成
bedrock = session .client("bedrock-runtime")

# リクエストボディを定義
body = json.dumps(
    {
        "messages": [
            {
                "role": "user",
                "content": [{"text": "Bedrockってどういう意味？"}],
            }
        ],
        "inferenceConfig": {"max_new_tokens": 1000},
    }
)

# モデルを定義（Amazon Nova Pro）
modelId = "apac.amazon.nova-pro-v1:0"

# HTTPヘッダーを定義
accept = "application/json"
contentType = "application/json"

# レスポンスを定義
response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get("body").read())
#answer = response_body["content"][0]["text"]
answer = response_body["output"]["message"]["content"][0]["text"]

# 生成されたテキストをコンソールに表示
print(answer)