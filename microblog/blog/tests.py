from django.test import TestCase, Client

class BlogTestCase(TestCase):

    # @override テスト前
    def setUp(self):
        # テストクライアントを作成
        self.c = Client()

    # python manage.py test でテスト実行
    # 以下のテストケース関数をシーケンス的に実行

    # ページにアクセス成功するか
    def test_index_access(self):
        # クライアントを使ってルートにアクセス
        res = self.c.get('/')

        # レスポンスのステータスコードを検証
        # status code => 200 OK
        # status code => 404 Not Fount
        # status code => 302 Redirect
        self.assertEqual(200, res.status_code)

    # 存在しないページがNotFountとなるか
    def test_fail_access(self):
        res = self.c.get('/unknow')
        self.assertEqual(404, res.status_code)