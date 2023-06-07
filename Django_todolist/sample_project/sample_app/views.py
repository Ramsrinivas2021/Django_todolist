from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    initial_data = {'title': 'sdadsadsd', 'description': 'sadasdsad', 'completed': True}
    task = Task(title=initial_data['title'], description=initial_data['description'], completed=initial_data['completed'])
    # tasks = [task]
    task.save()
    tasks = Task.objects.all()
    # tasks[0] = task
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        
        form = TaskForm()
        # Manually create a Task object with the initial data
        
        
    return render(request, 'create_task.html', {'form': form})

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})
