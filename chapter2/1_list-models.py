# Pyhton外部モジュールのインポート
import boto3

# AssumeRoleを実施
session = boto3.Session(profile_name="admin")

# Bedrockクライアントの作成
bedrock = session.client("bedrock")

# モデル一覧取得APIの呼び出し
result = bedrock.list_foundation_models()

# 結果をコンソールに表示
print(result)