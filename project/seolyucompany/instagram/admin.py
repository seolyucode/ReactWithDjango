from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# 등록법 #1
# admin.site.register(Post)  #기본 ModelAdmin으로 동작

@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 여러개 가능
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"