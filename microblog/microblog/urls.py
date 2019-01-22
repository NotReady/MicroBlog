"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView

# リクエスト ⇒ urls.py ⇒ views ⇒ テンプレート ⇒ レスポンス

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(マッチするアドレス, 呼び出すview関数、アドレスにつけるニックネーム)
    # ニックネーム呼び出しとすると後のURLの変更による影響を受けない設計ができる
    # http://localhost:8000/ サイトルートへのリクエストに対して
    # BlogListViewのas_view()メソッドを紐付ける
    # ニックネームをindexと設定する
    path('', BlogListView.as_view(), name="index"),
    # <int:pk>　int なんかしらの整数
    # <int:pk>　pk整数が代入される変数 整数値がpk変数に代入される(プライマリキー)
    path('detail/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('create', BlogCreateView.as_view(), name='create'),
]
