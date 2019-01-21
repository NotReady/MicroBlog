from django.shortcuts import render
# 汎用ビュー リストビューのインポート
from django.views.generic import ListView
# 実装モデルのインポート
from .models import Blog

class BlogListView(ListView):
    model = Blog
