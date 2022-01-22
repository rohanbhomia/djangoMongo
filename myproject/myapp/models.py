
from matplotlib.pyplot import title
from djongo import models

# Create your models here.

class Todo(models.Model):
    title = models.TextField()
    description = models.TextField()
    gender = models.TextField()
    demo = models.JSONField()

    def __str__(self) -> str:
        return self.title
