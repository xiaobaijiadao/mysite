from django.contrib import admin

from .models import User, Blog, Comment, Pic
# Register your models here.

class PicInline(admin.StackedInline):
	model = Pic
	extra = 1

class ComInline(admin.StackedInline):
	model = Comment
	extra = 1


class BlogAdmin(admin.ModelAdmin):
	inlines = [PicInline, ComInline]
	list_display = ('title', 'author', 'date', 'kind', 'tag', 'clickTimes','isReprint')
	radio_fields = {
        'kind': admin.HORIZONTAL,
        'tag': admin.HORIZONTAL
    }
	list_filter = ['tag']
	search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
	inlines = [ComInline]
	list_display = ('id','date', 'author', 'blog', 'isPass')
	list_filter = ['date']
	search_fields = ['blog']
	
class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'power')
	radio_fields = {
        'power': admin.HORIZONTAL,
    }
	list_filter = ['power']
	search_fields = ['name']
		

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)