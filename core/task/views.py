from flask import render_template, request, redirect, url_for
from . import task
from .forms import TaskForm
from .models import Category
from core.models import Todo
from core import db

@task.route("/create-task", methods=["GET", "POST"])
def tasks():
    form = TaskForm()
    check = None
    todo = Todo.query.all()

    if request.method == "POST":
        # DELETE TASK
        if request.form.get('taskDelete') is not None:
            deleteTask = request.form.get('checkedbox')
            if deleteTask is not None:
                todo_item = Todo.query.filter_by(id=int(deleteTask)).one()
                db.session.delete(todo_item)
                db.session.commit()
                return redirect(url_for('task.tasks'))
            else:
                check = 'Please check-box of task to be deleted'

        # CREATE TASK
        elif form.validate_on_submit():
            selected = form.category.data
            category = Category.query.get(selected)
            todo_item = Todo(
                title=form.title.data,
                date=form.date.data,
                time=form.time.data,
                category=category.name
            )
            db.session.add(todo_item)
            db.session.commit()
            return redirect(url_for('task.tasks'))

    return render_template(
        "tasks.html",
        title="Create Tasks",
        form=form,
        todo=todo,
        check=check
    )
