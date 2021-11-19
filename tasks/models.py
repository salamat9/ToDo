from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[self.pk])


class Tag(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Task, related_name='tags', blank=True)

    def __str__(self):
        return self.name


