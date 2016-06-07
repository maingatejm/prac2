from django.contrib import admin
from django.contrib.humaize.templatetags.humanize import intcomma
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'content_size', 'created_at']

	def content_size(self, post):
		return '%자' % intcomma(len(post.content))

admin.site.register(Post, PostAdmin)