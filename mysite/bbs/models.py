from django.db import models
from datetime import datetime


class Thread(models.Model):
    title = models.CharField("タイトル", max_length=200, blank=False)
    message = models.TextField("メッセージ", blank=False)
    pub_date = models.DateTimeField("登録日", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "スレッド"

    def __unicode__(self):
        return self.massage


class Comment(models.Model):
    thread = models.ForeignKey(Thread, verbose_name="スレッド")
    usrname = models.CharField("お名前", max_length=100, blank=False)
    message = models.CharField("メッセージ", max_length=200, blank=False)
    pub_date = models.DateTimeField("登録日", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "コメント"

    def __unicode__(self):
        return self.message
