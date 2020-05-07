from django.db import models
from datetime import datetime


class Message(models.Model):
    '''メッセージモデル'''

    class Meta:
        verbose_name_plural = "メッセージ"

    message_content = models.TextField("メッセージ内容", max_length=10)
    target_id = models.CharField("送り先のID", max_length=10)
    source_id = models.CharField("送り手のID", max_length=10)
    created_at = models.DateTimeField("作成日", default=datetime.now)
    # 最終的にアップデート_　更新のつき

    def __str__(self):
        return f'送り主:{self.source_id}'

    # def __str__(self):
    #     # タイトルの名前を押して詳細に入ったときの名前を変更できる
    #     return self.nickname
