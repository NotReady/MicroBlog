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
# フォームヘルパ
from .forms import BlogForm
# ログインインターフェース
# mixinとはインターフェース
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

# 実装モデルのインポート
from .models import Blog

# リストビュー
class BlogListView(ListView):
    model = Blog
    # 1ページあたりの件数
    # paginate_by = None
    paginate_by = 5

    # テンプレートのモデルの参照名を変更
    # デフォルトobject_listも有効
    context_object_name = 'Blogs'

# 詳細ビュー
class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'

# 作成ビュー
# mininは先に指定するらしい
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    # ポストコンテンツはfieldsが必須
    # fields = ['content', ]
    # ポスト成功時のリダイレクト先
    success_url = reverse_lazy('index')
    template_name = 'blog/blog_create_form.html'

    # ログインのURL
    # 未ログイン状態時のリダイレクト先
    login_url = '/login'

    # モデルが保存された時のコールバックをオーバーライドする
    def form_valid(self, form):
        messages.success(self.request, "作成しました")
        # スーパークラスのデフォルトを実行する
        return super().form_valid(form)

    # モデルが保存に失敗した時のコールバックをオーバーライドする
    def form_invalid(self, form):
        messages.error(self.request, "作成に失敗しました")
        # スーパークラスのデフォルトを実行する
        return super().form_invalid(form)

# 更新ビュー
class BlogUpdateView(LoginRequiredMixin, UpdateView):

    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'

    login_url = './login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={"pk": blog_pk})
        return url

    # モデルが保存された時のコールバックをオーバーライドする
    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        # スーパークラスのデフォルトを実行する
        return super().form_valid(form)

    # モデルが保存に失敗した時のコールバックをオーバーライドする
    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        # スーパークラスのデフォルトを実行する
        return super().form_invalid(form)


class BlogDeleteView(LoginRequiredMixin,  DeleteView):
    model = Blog
    success_url = reverse_lazy('index')
    login_url = './login'

    # モデルが削除された時のコールバックをオーバーライドする
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        # スーパークラスのデフォルトを実行する
        return super().delete(request, args, kwargs)

