from django.views.generic import ListView

class IndexView(ListView):
    template_name = 'external/index.html'
    context_object_name = 'menu_list'
    menu_list = [
      {'name': 'プログラミング教室憲章', 'link': '#', 'disable': True},
      {'name': '書類ダウンロード', 'link': '#', 'disable': True},
      {'name': '年間スケジュール', 'link': '#', 'disable': True},
      {'name': '運営組織', 'link': '#', 'disable': True},
      {'name': '教室情報', 'link': '#', 'disable': True},
    ]

    def get_queryset(self):
        return self.menu_list
