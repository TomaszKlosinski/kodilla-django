from django.contrib import admin
from posts.models import Post, Author

class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "content", "created", "modified", "author_id"]
   list_filter = ["title"]
   search_fields = ["title", "author_id"]


admin.site.register(Post, PostAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email']
