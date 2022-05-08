from django.contrib import admin
from blog.models import Post,Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy="created_date"
    empty_value_display='-empty-'
    list_display=('title','author','contact_views','published_date','created_date','status')
    list_filter=('status','author')
    # ordering=['created_date']
    search_fields=['title','content']
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category)




# Register your models here.
