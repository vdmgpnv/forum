from django.contrib import admin

from .models import Section, Post, Thread


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name')
    list_display_links = ('id', 'section_name')


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread_name', 'section_id')
    list_filter = ('section_id',)
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'tread_id', 'created_at', 'show_post')
    list_filter = ('user_id', 'tread_id')
    search_fields = ('id','user_id__username', 'tread_id__thread_name')
    list_per_page = 10

admin.site.register(Section, SectionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Thread, ThreadAdmin)

# Register your models here.
