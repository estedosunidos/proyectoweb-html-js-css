from django.shortcuts import render
from Blog.models import Post,Categoria
# Create your views here.
def blog(request):
    post=Post.objects.all()
    return render(request, 'Blogs/blog.html',{"post":post})
def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    post=Post.objects.filter(categoria=categoria)
    return render(request, 'Blogs/Categoria.html',{"categoria":categoria,"post":post})
    