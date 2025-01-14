from django.db import models


class Comment(models.Model):
    comment_author = models.ForeignKey("UserApp.User", on_delete=models.CASCADE)
    blog = models.ForeignKey("BlogApp.Blog", on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment_author.username + " commented on " + self.blog.title
