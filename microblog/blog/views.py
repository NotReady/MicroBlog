from django.shortcuts import render
# クラスベースビュー リストビューのインポート
from django.views.generic import ListView
# クラスベースビュー 詳細ビューのインポート
from django.views.generic import DetailView
# クラスベース汎用ビュー 作成ビューのインポート
from django.views.generic import CreateView
# ニックネームの解決関数
from django.urls import reverse_lazy
# クラスベース汎用ビュー 更新ビューのインポート
from django.views.generic import UpdateView

# 実装モデルのインポート
from .models import Blog

# リストビュー
class BlogListView(ListView):
    model = Blog

# 詳細ビュー
class BlogDetailView(DetailView):
    model = Blog

# 作成ビュー
class BlogCreateView(CreateView):
    model = Blog
    # ポストコンテンツはfieldsが必須
    fields = ['content', ]
    # ポスト成功時のリダイレクト先
    success_url = reverse_lazy('index')

# 更新ビュー
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['content', ]

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={"pk": blog_pk})
        return url
