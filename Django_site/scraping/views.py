from audioop import reverse
from django.shortcuts import render
from .forms import LinkForm
from django.http import HttpResponse
from .app.bs4_ieee import search
from .app.bs4_ieee import download


class Index:
    def __init__(self):
        self.data = []
        self.key = ''
        self.label_key = ''
        self.reverse = -1

    def index_form(self,request):
        html = 'scraping/index.html'

        if request.method == 'GET':
            form = LinkForm()
            context = { 'form': form }
            return render(request, html, context)

        elif request.method == 'POST':
            form = LinkForm(request.POST)
            if not form.is_valid():
                return render(request, html)

            url = form.cleaned_data['URL']

            if 'submit1' in request.POST and 'https' in url:
                try:
                    self.key, data = search(url)
                    self.data.extend(data)
                    self.label_key = f'key word : {self.key}'
                    self.data = list(dict.fromkeys(self.data))
                except:
                    pass

            if 'submit2' in request.POST and len(self.data) > 1:
                self.data = sorted(self.data)[::self.reverse]
                self.reverse *= -1

            if 'submit3' in request.POST:
                self.data = []
                self.key = ''
                self.label_key = self.key

            if 'submit4' in request.POST and len(self.data) > 0:
                response = HttpResponse(content_type='text/csv')
                filename = 'ReferenceList.csv'
                response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
                download([self.key, self.data],response)
                return response
                
            context = { 'form': form, 'message':self.label_key, 'data':self.data }
            return render(request, html, context)

        # 未対応のメソッド
        else:
            return HttpResponse('不正なメソッドです', status=500)

