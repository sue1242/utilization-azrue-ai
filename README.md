# Microsoft AzureではじめるAI活用（画像編）
Microsoft Azure Cognitive Servicesを使って、画像に対してAIでどのようなことができるかを解説した技術同人誌に掲載しているコードと必要なデータの一覧です。

[書籍はこちら](https://techbookfest.org/product/kjTaWvpP97pfYKuubhBVZN?productVariantID=9ZQ9jg9WZ6mkmZKz8Cni4j)

コードとデータは以下の節のものが対象です。

## 5-2 OCRで文字を取り出してみよう
この節ではForm Recgnizerを使って請求書のどの箇所に何の情報が書いているかを自動で判別させます。

書籍内での解説はGUIで動作するツールでの操作のみにのため、公開しているものは使用するデータのみです。  

## 5-3 写真に何が写っているかを自動判定してみよう
この節ではCognitive ServicesのComputer VisionとCustom Visionを使って、写真に何が写っているかを識別させます。

Custom VisionはGUIで動作するツールでモデルにデータを学習させるので、コード単独では動作しません。
GUIで動作するツールの使用方法は書籍を参照願います。

## 5-4 写真に写っている人を識別させてみよう
この節ではCognitive ServicesのFaceサービスを使って、写真から以下のものを抽出します。

- 写っている人の情報
- 特定の人が写っているかどうかの判別結果

この節のコードは、コード単独で動作します.
