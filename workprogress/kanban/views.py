from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Task
from django.contrib.auth.decorators import login_required
from .models import UrgentTask
from .forms import UrgentTaskForm




# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    priority_filter = request.GET.get('priority', '')  # Get priority from query params
    tasks = Task.objects.filter(created_by=request.user)
    
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)  # Apply priority filter if selected

    tasks = tasks.order_by('-priority', '-created_at')  # Sort by priority and creation time
    return render(request, 'dashboard.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST.get('priority')  # Retrieve the priority from the form
        Task.objects.create(title=title, description=description, status='todo',priority= priority, created_by=request.user)
        return redirect('dashboard')
    print(request.POST.get('priority'))
    return render(request, 'add_task.html')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('dashboard')
    return render(request, 'edit_task.html', {'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    task.delete()
    return redirect('dashboard')

@login_required
def move_task(request, task_id, new_status):
    task = get_object_or_404(Task, id=task_id, created_by=request.user)
    task.status = new_status
    task.save()
    return redirect('dashboard')


def urgent_tasks(request):
    tasks = UrgentTask.objects.all().order_by('-created_at')
    return render(request, 'urgent_tasks.html', {'tasks': tasks})

def add_urgent_task(request):
    if request.method == 'POST':
        form = UrgentTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('urgent_tasks')
    else:
        form = UrgentTaskForm()
    return render(request, 'add_urgent_task.html', {'form': form})

def edit_urgent_task(request, task_id):
    task = get_object_or_404(UrgentTask, id=task_id)
    if request.method == 'POST':
        form = UrgentTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('urgent_tasks')
    else:
        form = UrgentTaskForm(instance=task)
    return render(request, 'edit_urgent_task.html', {'form': form})

def delete_urgent_task(request, task_id):
    task = get_object_or_404(UrgentTask, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('urgent_tasks')
    return render(request, 'delete_urgent_task.html', {'task': task})



