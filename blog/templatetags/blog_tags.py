from django import template
from blog.models import Post

register=template.Library()

@register.simple_tag(name='totalpost')
def function ():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.inclusion_tag("popularposts.html")
def popularposts():
    posts=Post.objects.filter(status=1).order_by('contact_views')[:2]
    return {'posts':posts}

@register.inclusion_tag("blog/blog-popular-post.html")
def latestposts():
    posts=Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts':posts}
    