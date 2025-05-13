from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('ongoing', 'Ongoing'),
    ('success', 'Success'),
    ('failure', 'Failure'),
)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def is_overdue(self):
        return timezone.now() > self.deadline and self.status == 'ongoing'

    def __str__(self):
        return self.title
