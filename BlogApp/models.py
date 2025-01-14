from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=40)
    publication_date = models.DateField(null=True)
    author = models.ForeignKey('UserApp.User', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField()
    tags = models.ManyToManyField(Tag,related_name="blog_list")
    def __str__(self):
        return self.title
    

    