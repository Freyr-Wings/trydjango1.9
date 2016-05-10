from django.contrib import admin

# Register your models here.
from .models import Post
#the same as
#from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","content","updated"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["content","updated"]
    search_fields = ["title", "content"]
#     class Meta:
#         model = Post
#?????????What's the use of this???????????
#refer https://docs.djangoproject.com/en/1.9/ref/contrib/admin/

admin.site.register(Post, PostModelAdmin)#connect Post with PostModelAdmin