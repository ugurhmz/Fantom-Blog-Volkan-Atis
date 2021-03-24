from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_filter=['publishing_date']
    list_display=['title','publishing_date','image']
    list_display_links = ['title','publishing_date','image']
    search_fields = ['title','content']


    class Meta:
        model =Post