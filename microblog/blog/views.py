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
# クラスベース汎用ビュー 削除ビューのインポート
from django.views.generic import DeleteView
from .forms import BlogForm

# 実装モデルのインポート
from .models import Blog

# リストビュー
class BlogListView(ListView):
    model = Blog
    # テンプレートのモデルの参照名を変更
    # デフォルトobject_listも有効
    context_object_name = 'Blogs'

# 詳細ビュー
class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

# 作成ビュー
class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # ポストコンテンツはfieldsが必須
    # fields = ['content', ]
    # ポスト成功時のリダイレクト先
    success_url = reverse_lazy('index')
    template_name = 'blog/blog_create_form.html'

# 更新ビュー
class BlogUpdateView(UpdateView):

    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={"pk": blog_pk})
        return url

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('index')