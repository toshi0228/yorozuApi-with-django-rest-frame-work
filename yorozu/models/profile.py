from django.db import models
from .plan import Tag


# # よろず屋プロフィール

class Profile(models.Model):
    class Meta:
        # 管理画面でアプリのタイトルの名前を変更
        verbose_name_plural = "プロフィール"
        # app_label = 'yorozu'

    nickname = models.CharField("ニックネーム", max_length=10)
    yorozuya_name = models.CharField("万事屋の名前", max_length=10, default="")
    profile_image = models.ImageField("プロフィール画像", upload_to='', default="")
    yorozu_main_image = models.ImageField("万屋メイン画像", upload_to='', default="")
    profile_description = models.TextField("プロフィール説明", max_length=255)
    review_score = models.IntegerField("レビュースコア")

    twitter_account = models.CharField(
        "twitterのアカウント", max_length=80, default="", blank=True)

    instagram_account = models.CharField(
        "instagramのアカウント", max_length=80, default="", blank=True)

    facebook_account = models.CharField(
        "facebookのアカウント", max_length=80, default="", blank=True)

    def __str__(self):
        # タイトルの名前を押して詳細に入ったときの名前を変更できる
        return self.nickname
