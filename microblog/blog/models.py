from django.db import models

# ブログ記事のモデル
class Blog(models.Model): # フレームワークを継承

    # 属性
    # マイグレーションのサポートは***Fieldで属性を定義する

    # 記事
    content = models.CharField(max_length=140)
    # 投稿日時 投稿日時を自動的にアサイン
    # auto_now_add  初回登録時のみ設定
    # auto_now      更新タイミングで上書き
    posted_date = models.DateTimeField(auto_now_add=True)

    # 自動的に昇順のid属性(プライマリキー)が付与される。idは永久欠番。
    # id = 1, 2, ...
