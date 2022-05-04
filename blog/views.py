from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.db.models import F
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now())
    context ={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=Post.objects.update(contact_views=F("contact_views")+1)
    posts=get_object_or_404(Post,pk=pid)
    context={'post':posts,'pid':pid}
    return render(request,'blog/blog-single.html',context)
def test(request,name):
    # posts=Post.objects.filter()
    context = {'name':name}
    return render(request,'test.html',context)
    
    

# Create your views here.
