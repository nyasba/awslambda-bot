## ApiGatewayの設定方法

### Lambdaから設定

1. API endpointsを開く
2. Add API endpoint
3. [API Gateway]を選択
4. デフォルトの通り設定※

※簡単に試すためには、MethodをGET、SecurityをOpenにすると楽ですが、自己責任で。

作成したらLambda側でエンドポイントURLが表示されているので、GET/認証なしならクリックするだけで実行可能。


### API Gateway側でTest実行

API Gatewayのメニューを見てみると、[LambdaMicroservice]というのができている。

開くと、先ほど作成したAPIパスおよびMethodが表示されているのでクリック。

MethodExecutionで[Test]を押すとテスト実行される

