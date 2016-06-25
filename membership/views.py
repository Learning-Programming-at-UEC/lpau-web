from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from util.views import CommonView
from util.views import CommonTemplateView
from django.views.generic import FormView
from util.views import CommonDetailView
from util.views import CommonListView
from datetime import datetime

from .models import Thread, Comment
from .forms import CommentForm


class IndexView(CommonTemplateView):
    template_name = 'membership/index.html'

class TeachersView(CommonListView):
    template_name = 'membership/teachers.html'
    context_object_name = 'teachers'
    teachers = [
        {'name': '小木曽 聖', 'kana': 'おぎそ あきら',
            'introduction': '趣味は読書とプログラミング\nおすすめの本はバーティミアス。Atcoder(プログラミングコンテスト)とかたまに出る。\n最近は料理とかスポーツにも手を出し始めた。',
            'to_students': '「好きこそものの上手なれ」ってことで、好きになるとこから始めよう！'},
        {'name': '山根 茂之', 'kana': 'やまね しげゆき',
            'introduction': '電気通信大学3年生。趣味はサイクリング。音声に興味を持ち始める。',
            'to_students': 'プログラミングは楽しいものですが、できるようになるには相当な時間が必要です。この教室でプログラミングの楽しさや難しさを学んでもらえたら嬉しいです。また家でちゃんと復習することも大切ですよ。'},
        {'name': '風間 健流', 'kana': 'かざま たける',
            'introduction': '機械いじりと釣りが趣味。\n最近のマイブームは古本屋巡りです。\nゲーム作成サークルのx680x0同好会に所属。',
            'to_students': 'プログラミングは最初は難しいかもしれません。でもコツをつかめばいろいろなことができるようになり、とてもおもしろくなります。一緒に頑張りましょう！'},
        {'name': '宮澤 修', 'kana': 'みやざわ おさむ',
            'introduction': '横浜市出身・在住\n情報理工学部　情報・通信工学科3年　コンピュータサイエンスコース（コンピュータの仕組みについて学ぶところです）\n好きなゲーム　星のカービィ、MOTHER(1, 2)',
            'to_students': 'プログラミングは一人でやるより、仲間と共にやっていく方が面白いし、上達します（体験談）。気軽に相談してください。一緒に楽しみながら腕を磨きましょう。'},
        {'name': '張 翌坤', 'kana': 'ちょう よくこん',
            'introduction': '中国から来た留学生です。テレビゲームが好きで、スマホゲームが嫌い。みんなに好かれる先生になりたいなぁ〜',
            'to_students': 'pythonは本当に簡単で優れた言語です。この教室を通して、最終的にこのプログラミング力がみんなの勉強や生活の助けになれるなら嬉しいです。'},
        {'name': '栁 裕太', 'kana': 'やなぎ ゆうた',
            'introduction': '学部2年総合情報学科\nプログラミングデビューは中3でした\n日々エラーとテストに頭を抱える日々',
            'to_students': '誰にでも凄いものが作れる時代になりました。\n自分は何が作れるのか、考えてみましょう。\nきっと、実現できますよ。'},
        {'name': '佐藤 海斗', 'kana': 'さとう かいと',
            'introduction': 'プログラミングは大学生から本格的に始める。アニメ・釣り・アウトドアなどが好きです。ロボメカ工房フライト部隊に所属。最近はドローンの制作や新入生に向けたArduino講習の準備をしています。',
            'to_students': 'プログラミングは最初のうちは楽しめないと思います。しかし、ある程度できるようになれば楽しくなってくると思うので頑張りましょう！一緒に頑張っていきましょう！'},
        {'name': '長安 尚之', 'kana': 'ながやす なおゆき',
            'introduction': '埼玉都民の長安です！\n趣味はアニメと落語（聞く方）。\nでも『じょしらく』はあんまり見てません。',
            'to_students': 'わかると楽しいのがプログラミング。\nわからないところがあったら、\n一緒に考えていこう！'},
        {'name': '南条 宏貴', 'kana': 'なんじょう ひろき',
            'introduction': 'うどんの王国、香川県出身の南条です！大学一年！趣味はバレーボールで、大学でもバレーボール部に入部しています！プログラミングも本格的に始めたのは大学に入ってからなので、初心者ですが一生懸命頑張ります！',
            'to_students': '楽しみながら自然と力がつく教室を目指しています！\n一緒に頑張りましょう！'},
    ]

    def get_queryset(self):
        return self.teachers

class ThreadView(FormView, CommonDetailView):
    template_name = 'membership/thread.html'
    model = Thread
    form_class = CommentForm
    success_url = './'

    def get_context_data(self, **kwargs):
        # 表示するスレッド
        context = super(FormView, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        context['comment_list'] = thread.comment_set.all().order_by('id')

        return context

    def form_valid(self, form):
        form.instance.username = self.request.user.username
        form.instance.thread = get_object_or_404(Thread, pk=self.kwargs.get(self.pk_url_kwarg))
        form.instance.save()

        return super(ThreadView, self).form_valid(form)


# 講義資料リスト: linkは django_project_root/files/documents/ の中を指している
# TODO: 表示時に順番が逆転してしまう可能性有
document_list = {
    'entry': [
        {'file_name': 'lpau_entry1_20160508.pptx', 'link': '1.pptx',
            'date': '20160508', 'datetime': datetime(2016, 5, 8)},
        {'file_name': 'lpau_entry2_20160512.pptx', 'link': '2.pptx',
            'date': '20160512', 'datetime': datetime(2016, 5, 12)},
        {'file_name': 'lpau_entry3_20160522.pptx', 'link': '3.pptx',
            'date': '20160522', 'datetime': datetime(2016, 5, 22)},
        {'file_name': 'lpau_entry4_20160529.pptx', 'link': '4.pptx',
            'date': '20160529', 'datetime': datetime(2016, 5, 29)},
        {'file_name': 'lpau_entry5_20160605.pptx', 'link': '5.pptx',
            'date': '20160605', 'datetime': datetime(2016, 6, 5)},
        {'file_name': 'lpau_entry6_20160612.pptx', 'link': '6.pptx',
            'date': '20160612', 'datetime': datetime(2016, 6, 12)},
        {'file_name': 'lpau_entry7_20160619.pptx', 'link': '7.pptx',
            'date': '20160619', 'datetime': datetime(2016, 6, 19)},
    ],
    'basic': [
        {'file_name': 'lpau_basic1_20160522.pdf', 'link': '1.pdf',
            'date': '20160522', 'datetime': datetime(2016, 5, 22)},
        {'file_name': 'lpau_basic2_20160529.pdf', 'link': '2.pdf',
            'date': '20160529', 'datetime': datetime(2016, 5, 29)},
        {'file_name': 'lpau_basic3_20160605.pdf', 'link': '3.pdf',
            'date': '20160605', 'datetime': datetime(2016, 6, 5)},
        {'file_name': 'lpau_basic4_20160619.pdf', 'link': '4.pdf',
            'date': '20160619', 'datetime': datetime(2016, 6, 19)},
    ],
}

class DownloadDocumentView(CommonListView):
    template_name = 'membership/download_document.html'
    context_object_name = 'document_list'

    def get_queryset(self):
        return document_list

class DownloadFileView(CommonView):
    def get(self, request, *args, **kwargs):
        date = kwargs['date']
        difficulty = kwargs['difficulty']
        for document in document_list[difficulty]:
            if document['date'] == date:
                link = document['link']
                file_name = document['file_name']

        response = HttpResponse(
            open('files/documents/' + difficulty + link, 'rb').read(),
            content_type='application/octet-stream'
        )
        response['Content-Disposition'] = 'attachment; filename = "' + file_name + '"'

        return response
