from django.db import models
from datetime import datetime


class Message(models.Model):
    '''メッセージモデル'''

    class Meta:
        verbose_name_plural = "メッセージ"

    message_content = models.TextField("メッセージ内容", max_length=10)
    target_id = models.CharField("送り先のID", max_length=10)
    source_id = models.CharField("送り手のID", max_length=10)
    created_at = models.DateTimeField(default=datetime.now)
