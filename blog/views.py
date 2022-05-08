from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.db.models import F
# from django.core.paginator import Paginator

def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now())
    context ={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=get_object_or_404(Post,pk=pid,status=1)
    posts=Post.objects.update(contact_views=F("contact_views")+1)
    if Post.objects.filter(pk=pid+1).exists():
        has_next=True
        
        
    else:
        has_next=False
    if Post.objects.filter(pk=pid-1).exists():
        has_previous=True
        
    else:
        has_previous=False
    next_pid=pid+1
    previous_pid=pid-1
    context={'post':posts,'pid':pid,'has_next':has_next,'has_previous':has_previous,'next_pid':next_pid,'previous_pid':previous_pid}
    return render(request,'blog/blog-single.html',context)
def test(request,pid):
    # posts=Post.objects.filter()
    list_post=list(Post.objects.all())
    posts=get_object_or_404(Post,pk=pid,status=1)
    next_post=get_object_or_404(Post,pk=pid+1)
    prev_post=get_object_or_404(Post,pk=pid-1)

    context = {'list_post':list_post,'post':posts,'next_post':next_post,'prev_post':prev_post}
    return render(request,'test.html',context)
    
    

# Create your views here.
