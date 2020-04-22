from django.db import models

class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message
    
    # admin단에 구현도 가능함
    # def message_length(self):    # 인자없는 함수만 가능
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"  # 이름도 변경 가능