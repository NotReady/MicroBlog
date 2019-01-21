from django.shortcuts import render
# クラスベースビュー リストビューのインポート
from django.views.generic import ListView
# クラスベースビュー 詳細ビューのインポート
from django.views.generic import DetailView

# 実装モデルのインポート
from .models import Blog

# リストビュー
class BlogListView(ListView):
    model = Blog

# 詳細ビュー
class BlogDetailView(DetailView):
    model = Blog
