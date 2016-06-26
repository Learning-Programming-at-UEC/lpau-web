from datetime import timedelta
from unittest import mock

from django.shortcuts import resolve_url
from django.test import TestCase
from django.utils import timezone


from .models import DataFile


class FileManagerTest(TestCase):

    def test_was_recently(self):
        # 1日よりも少しだけ古い
        obj = DataFile(pub_date=timezone.now() - timedelta(days=1, minutes=1))
        self.assertFalse(obj.was_published_recently(), '1日と1分前に公開')

        # 1日よりも少しだけ新しい
        obj = DataFile(pub_date=timezone.now() -
                       timedelta(days=1) + timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '1日と1分後に公開')

        # つい最近公開
        obj = DataFile(pub_date=timezone.now() - timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), '1分前に公開')

        # もうちょっとしたら公開
        obj = DataFile(pub_date=timezone.now() + timedelta(minutes=1))
        self.assertFalse(obj.was_published_recently(), '1分後公開')
