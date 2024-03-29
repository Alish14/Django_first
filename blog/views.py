from django.shortcuts import get_object_or_404, render,redirect
from blog.models import Post,comment
from django.db.models import F
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect



def blog_view(request,**kwargs):
    posts=Post.objects.filter(status=1).order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])


    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context ={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    posts=Post.objects.filter(pk=pid).update(contact_views=F("contact_views")+1)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your comment submited")
  
        else:
            messages.add_message(request,messages.ERROR,"your comment did'nt submited")
    if Post.objects.filter(pk=pid+1).exists():
            has_next=True
    else:
            has_next=False
    if Post.objects.filter(pk=pid-1).exists():
            has_previous=True
    else:
            has_previous=False
    form=CommentForm()
    next_pid=pid+1
    previous_pid=pid-1
    if not Post.login_require:
        comments=comment.objects.filter(post=pid,approved=True).order_by('-created_date')
        posts=get_object_or_404(Post,pk=pid,status=1)
        context={'post':posts,'pid':pid,'has_next':has_next,'has_previous':has_previous,'next_pid':next_pid,'previous_pid':previous_pid,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def test(request):
    # posts=Post.objects.filter()
    posts=Post.objects.filter(status=1)
    context = {'post':posts}
    return render(request,'test.html',context)
def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=Post.objects.filter(category__name=cat_name)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)







    
