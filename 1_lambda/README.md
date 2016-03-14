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

できたzipをアップロードして、handlerは「post_chatwork_at_lambda.lambda_handler」にする。


### スケジュールトリガにする場合は

cron expression欄を「0 * * * ? *」などにする
