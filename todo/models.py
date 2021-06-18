from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS = (
        ('ongoing', 'ongoing'),
        ('done', 'done')
    )
    MODE = (
        ('issues', 'issues'),
        ('goal', 'goal')
    )
    todo_name = models.CharField(max_length=200)
    todo_description = models.TextField(max_length=250)
    todo_status = models.TextField(choices=STATUS)
    todo_mode = models.TextField(choices=MODE)
    todo_created = models.DateTimeField(auto_now_add=True)
    todo_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo_name
    