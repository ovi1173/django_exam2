from django.contrib import admin

# Register your models here.
from todo_app.models import TaskModel

admin.site.register(TaskModel)