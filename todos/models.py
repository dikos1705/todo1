from django.db import models



class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_done = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title