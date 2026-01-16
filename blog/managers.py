from django.db import models
from django.db.models import Q

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="PUBLISHED")

    def search(self, term: str):
        return self.get_queryset().filter(
            Q(title__icontains=term) | Q(body__icontains=term)
        )
