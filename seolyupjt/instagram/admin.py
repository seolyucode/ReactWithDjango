from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"