## デプロイ手順

詳細はマニュアル参照
http://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

### requestsモジュールを追加

```
pip install requests -t <this directory>
```

### zip圧縮する

これがデプロイ対象のパッケージとなる。
（ディレクトリではなく、ディレクトリの中身を圧縮すること）

### lambdaに登録する

できたzipをアップロードして、handlerは「post_chatwork_at_lambda_with_s3.lambda_handler」にする。

EventSourceを追加を選び、以下を設定して保存

* EventSourceType：S3
* Bucket：トリガにしたいBucket
* EventType：ファイル作成／削除などトリガにしたいイベント

### S3にファイルを置いてみる

