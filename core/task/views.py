from flask import render_template
from . import task
from .forms import TaskForm
from .models import Category
from core.models import Todo

@task.route("/create-task")
def create_task():
    form = TaskForm()
    categories = Category.query.all()
    todos = Todo.query.all()
    return render_template("task/tasks.html", form=form, categories=categories, todos=todos)
