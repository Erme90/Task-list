from django.db import models

class Task (models.Model):

    STATUS = (
        ('Fazendo', 'Doing'),
        ('Feito', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=7, 
        choices= STATUS,
        )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title