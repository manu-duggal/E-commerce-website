from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blogpost

# Create your views here.
def index(request):
    blogs = Blogpost.objects.all()
    params = {'blogs': blogs}
    return render(request, 'blog/index.html', params)

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)
    print(post)
    return render(request, 'blog/blogpost.html', {'post': post})