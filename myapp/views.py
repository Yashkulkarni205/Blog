from django.shortcuts import render,redirect
from .models import Article
from .forms import RegistrationForm, ArticleForm
from django.views.generic import DeleteView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def owner_only(func):
    def wrap(request, *args, **kwargs):
        if Article.objects.get(id = kwargs['pk']).user == request.user:
            return func(request, *args, **kwargs)
        else:
            return render(request,'myapp/not_authorized.html')
    return wrap

class AdminOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if Article.objects.get(id = kwargs['pk']).user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request,'myapp/not_authorized.html')

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Successfully created for {username}")
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'myapp/register.html', { 'form': form })

@login_required
def my_articles(request):
    articles = Article.objects.filter(user = request.user)
    return render(request, 'myapp/articles.html', { 'articles': articles })

@login_required
def all_articles(request):
    articles = Article.objects.filter(privacy = 'public')
    return render(request, 'myapp/articles.html', { 'articles': articles })

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f"Article - {name} Successfully created.")
            return redirect('my-articles')
    
    else:
        form = ArticleForm()

    return render(request, 'myapp/create_article.html', { 'form': form })

@owner_only
def update_article(request,pk):
    
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f"Article - {name} Successfully Updated.")
            return redirect('my-articles')

    return render(request, 'myapp/update_article.html', { 'form': form })

class DeleteArticle(AdminOnlyMixin, DeleteView):
    model = Article
    template_name = 'myapp/delete_article.html'
    context_object_name = 'article'
    success_url = '/my-articles'
    
class DetailArticle(DetailView):
    model = Article
    template_name = 'myapp/detail_article.html'
    context_object_name = 'article'