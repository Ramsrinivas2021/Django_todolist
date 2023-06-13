from django.shortcuts import render
from ..models import Task
# from forms import TaskForm

def task_list(request):
    initial_data = {'title': 'sdadsadsd', 'description': 'sadasdsad', 'completed': True}
    
    tasks = Task.objects.all()
    
    if not tasks.exists():
        task = Task(title=initial_data['title'], description=initial_data['description'], completed=initial_data['completed'])
    # tasks = [task]
        task.save()
        tasks = [task] 
    # tasks = Task.objects.all()
    # tasks[0] = task
    return render(request, 'task_list.html', {'tasks': tasks})