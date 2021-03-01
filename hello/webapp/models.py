from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

# Create your models here.

class List(models.Model):
    describe = models.TextField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=150, null=False, blank=False, choices=status_choices, default='new')
    date_of_completion = models.DateField(null=True, blank=True, default=' ')
    class Meta:
        db_table = 'To-Do list'
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задачи'

    def __str__(self):
        return f'{self.id}. {self.status} {self.date_of_completion}'