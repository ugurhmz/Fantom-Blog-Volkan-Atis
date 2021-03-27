from django.contrib import admin
from posts.models import Post, Category,Tag, Comment


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_filter=['publishing_date']
    list_display=['title','publishing_date','image']
    list_display_links = ['title','publishing_date','image']
    search_fields = ['title','content']


    class Meta:
        model =Post


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_filter = ('publishing_date',)
    search_fields=('name','email','content','post__title')
    list_display=('name','email','publishing_date','post')
    list_display_links =('name','email','publishing_date','post')


    class Meta:
        model = Comment



admin.site.register(Category)
admin.site.register(Tag)