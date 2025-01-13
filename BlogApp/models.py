from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=40)
    publication_date = models.DateField(null=True)
    author = models.ForeignKey('UserApp.User', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    category = models.CharField(max_length=40)
    is_published = models.enums
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='tags' )
    def __str__(self):
        return self.name