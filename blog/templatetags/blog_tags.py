from django import template


from blog.models import Post,Category

register=template.Library()

@register.simple_tag(name='totalpost')
def function ():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.inclusion_tag("blog/blog-popular-post.html")
def popularposts():
    posts=Post.objects.filter(status=1).order_by('contact_views')[:3]
    return {'posts':posts}

@register.inclusion_tag("website/website_latest_post.html")
def latestposts():
    posts=Post.objects.filter(status=1).order_by('published_date').reverse()[:6]
    categories=Category.objects.all()
    return {'posts':posts,'categories':categories}

@register.inclusion_tag("blog/blog-post-category.html")
def postcategory():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return{'categories':cat_dict}


    