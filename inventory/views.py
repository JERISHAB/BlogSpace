from django.shortcuts import render,redirect
from articles.models import Article
from articles.forms import CreateArticle  # Ensure you import the correct form
from django.http import HttpResponse
from articles.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

#inventory display

@login_required(login_url="accounts:login")
def inventory_display(request):
    articles = Article.objects.filter(author=request.user)
    return render(request,'inventory/inv_display.html',{'articles':articles})   

#inventory update

@login_required(login_url="accounts:login")
def article_update(request,slug):
    article = Article.objects.get(slug=slug)
    print(article.title)

    if request.method == 'POST':
        form = CreateArticle(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('inventory:display')  # Redirect to article list after update
    else:
        form = CreateArticle(instance=article)

    return render(request, 'articles/article_create.html', {'form': form, 'article': article})

#inventory delete confirm

def article_delete_confirm(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'inventory/delete_confirm.html',{'article':article})



def article_delete(request,slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('inventory:display')
    return redirect('inventory:display')