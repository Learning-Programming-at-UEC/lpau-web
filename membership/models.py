from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    title = models.CharField("タイトル", max_length=200, blank=False)
    message = models.TextField("メッセージ", blank=False)
    pub_date = models.DateTimeField("作成日時", auto_now_add=True, editable=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "スレッド"
        verbose_name_plural = "スレッド"

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザ")
    thread = models.ForeignKey(Thread, verbose_name="スレッド")
    message = models.CharField("メッセージ", max_length=500, blank=False)
    pub_date = models.DateTimeField("投稿日時", auto_now_add=True, editable=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "コメント"
        verbose_name_plural = "コメント"

class StudentWork(models.Model):
    """生徒の作品"""
    user = models.ForeignKey(User, verbose_name="ユーザ")
    file_name = models.CharField("ファイル名", max_length=50)
    data = models.FileField("データ", upload_to='student_works')
    pub_date = models.DateTimeField("アップロード日時", auto_now_add=True, editable=False)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = verbose_name_plural = "生徒の作品"
