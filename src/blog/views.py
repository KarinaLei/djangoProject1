from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleForm

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    # success_url = '/'           # override the redirect page (by default, it goes to the detail page)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    # success_url = '/'           # override the redirect page (by default, it goes to the detail page)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# Create your views here.
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()        # <app_name>/<model_name>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()
    # ^ have to uncomment this and change attr to "pk" if you do not wish to override pk to id.
    # in which you don't have to use get_object method.

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "articles/article_detail.html", context)
#
# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "articles/article_list.html", context)