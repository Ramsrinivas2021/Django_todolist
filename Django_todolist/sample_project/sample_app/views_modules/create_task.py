from django.shortcuts import render, redirect
from ..forms import TaskForm

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