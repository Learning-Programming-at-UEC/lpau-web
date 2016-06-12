from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Thread, Comment
from .forms import CommentForm


class IndexView(generic.ListView):
    template_name = 'bbs/thread_list.html'
    context_object_name = 'Thread_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Thread.objects.all().order_by('-id')


class ThreadFormView(generic.edit.CreateView):
    model = Thread
    fields = ['title', 'message']
    template_name = 'bbs/thread_form.html'


def thread_detail(request, thread_id):
    '''
    指定したスレッドを表示する。
    @param thread_id: スレッドID
    '''
    # 表示するスレッド
    thread = get_object_or_404(Thread, pk=thread_id)
    # コメントの登録処理
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # コメントを登録
            comment = form.save(commit=False)
            comment.thread = thread
            comment.save()
            form = CommentForm()  # フォームの初期化
    else:
        form = CommentForm()
    # スレッドのコメント
    comment_list = thread.comment_set.all().order_by('id')
    return render_to_response('bbs/thread_detail.html',
                              {'thread': thread,
                               'comment_list': comment_list,
                               'form': form})
