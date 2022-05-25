from django.contrib import admin
from blog.models import Post,Category,comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy="created_date"
    empty_value_display='-empty-'
    list_display=('title','author','contact_views','published_date','created_date','status')
    list_filter=('status','author')
    search_fields=['title','content']
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display='-empty-'
    list_display=('name','post','approved','created_date')
    list_filter=('post','approved')
    search_fields=['name','post']


admin.site.register(comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)



# Register your models here.
