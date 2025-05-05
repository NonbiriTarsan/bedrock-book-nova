# Lamdbaレイヤーを作成する

Amazon Novaは「langchain-aws==0.2.9」以上でないと動きません。

```
mkdir python
pip install -t python langchain==0.3.15 langchain-aws==0.2.9 langchain-community==0.3.0 python-dateutil==2.8.2
rm -r python/boto*
zip -r9 langchain-layer.zip python
```
